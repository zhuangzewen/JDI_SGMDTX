
# 战法名称: 十二奇策
# 战法类型: 主动
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 0.6

# 十二奇策:
# 对敌军随机两人造成220%谋略伤害,并施加随机1种异常状态(优先施加未持有的状态),持续两回合

# 异常状态:特殊负面状态
# 包括:震慑、缴械、技穷、混乱、嘲讽、虚弱、断粮、洪水、火攻、风暴、畏惧、妖术,共计12种

from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import WeaponType
from External.Fitting.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Soul.JDI_Soul import Soul
from Log.JDI_Log import Log
from Calcu.JDI_Calculate import *

class 十二奇策_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.十二奇策
        self.战法类型 = SkillType.主动
        self.战法特性 = SkillFeature.谋略
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 0.6

class 十二奇策_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if status == SoulResponseTime.主动战法行动时 and hero == self.target:

            实际发动率 = (1 + self.target.get_主动战法发动率降低()) * self.skill.get_战法信息().发动率

            # 判断是否发动
            if random.random() > 实际发动率:
                Log().show_battle_info('        [{}]因几率未发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                return
            Log().show_battle_info('        [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

            attacked_heroes = 对敌方所有目标生效(self.target, battleField)
            for _ in range(2):

                if len(attacked_heroes) == 0:
                    break

                attacked: Hero = 从队列确定受击武将(attacked_heroes)
                attacked_heroes.remove(attacked)

                damageModel = 计算伤害(battleField, self.target, attacked, SoulDamageType.谋略, SkillType.指挥, 伤害值= 2.2)
                damage_soul = Soul(target=attacked,
                                    initiator=self.target,
                                    sourceType=SoulSourceType.武将战法,
                                    skill= self.skill,
                                    effect_type=SoulEffectType.损失兵力,
                                    effect_value=damageModel.damage_value,
                                    source_soul=self,
                                    battleField=battleField,
                                    damage=damageModel)
                damage_soul.deploy_initial()

                # 创建一个异常soul
                exception_soul = Soul(target=attacked,
                                        initiator=self.target,
                                        sourceType=SoulSourceType.武将战法,
                                        skill=self.skill,
                                        duration=2,
                                        effect_type=SoulEffectType.震慑,
                                        effect_value=1,
                                        source_soul=self,
                                        battleField=battleField)
                exception_soul.deploy_initial()


class 十二奇策_skill(Skill):
    def __init__(self, hero, skillName):
        # 调用父类的构造函数
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        十二奇策soul = 十二奇策_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=SoulResponseTime.内置待响应,
            effect_type=SoulEffectType.无影响,
            effect_value=0,
            battleField=None)
        self.get_Soul_list().append(十二奇策soul)
        self.get_持有者().get_持有Soul列表().append(十二奇策soul)
        self.get_持有者().get_响应Soul列表().append(十二奇策soul)