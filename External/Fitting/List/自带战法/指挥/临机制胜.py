
# 战法名称: 临机制胜
# 战法类型: 指挥
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 临机制胜:
# 战斗中,敌我全体被施加异常状态时,有70%概率触发制胜:立刻对敌军随机两人造成60%谋略伤害。
# 每回合制胜最多触发4次。累积触发4次制胜后,恢复我军全体兵力(治疗率40%,受智力影响)

# 满阶临机制胜:
# 战斗中,敌我全体被施加异常状态时,有70%概率触发制胜:立刻对敌军随机两人造成69%谋略伤害。
# 每回合制胜最多触发4次。累积触发4次制胜后,恢复我军全体兵力(治疗率46%,受智力影响)

# 异常状态:
# 特殊负面状态包括:震慑、缴械、技穷、混乱、嘲讽、虚弱、断粮、洪水、火攻、风暴、畏惧、妖术,共计12种

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

class 临机制胜_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.临机制胜
        self.战法类型 = SkillType.指挥
        self.战法特性 = SkillFeature.谋略
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 临机制胜_soul(Soul):

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
        self.临机制胜发动次数 = 0
        self.临机制胜发动总次数 = 0

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        
        if hero != self.initiator:
            return

        msg_移除响应(self)

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

        elif status == SoulResponseTime.回合重置阶段:
            self.临机制胜发动次数 = 0
            

        elif status == SoulResponseTime.被施加异常时 or status == SoulResponseTime.被施加控制时:

            if self.临机制胜发动次数 < 4:
                if random.random() > 0.7:
                    Log().show_debug_info('        [{}]发动来自【{}】的[临机制胜-制胜]效果, 但因几率未触发'.format(hero.get_武将名称().value, self.skill.get_战法名称().value))
                    return
                
                # [张曼成]执行来自【临机制胜】的「临机制胜-制胜」效果
                Log().show_battle_info('        [{}]执行来自【{}】的[临机制胜-制胜]效果'.format(hero.get_武将名称().value, self.skill.get_战法名称().value))

                self.临机制胜发动次数 += 1
                self.临机制胜发动总次数 += 1

                atta_hero = self.target
                attacked_times = msg_对敌方所有目标生效_number(self.target, battleField, 2)
                attacked_heroes = 对敌方所有目标生效(self.target, battleField)
                for _ in range(attacked_times):

                    if len(attacked_heroes) == 0:
                        break

                    attacked: Hero = 从队列确定受击武将(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
                    damageModel = 计算伤害(battleField, atta_hero, attacked, SoulDamageType.谋略, SkillType.指挥, 伤害值= self.skill.临机制胜_伤害系数())
                    damageModel.skillEffectName = "临机制胜-制胜"

                    # 创建一个伤害 SOUL
                    damage_soul = Soul(target=attacked,
                                        initiator=atta_hero,
                                        sourceType=SoulSourceType.武将战法,
                                        skill= self.skill,
                                        effect_type=SoulEffectType.损失兵力,
                                        effect_value=damageModel.damage_value,
                                        source_soul=self,
                                        battleField=battleField,
                                        damage=damageModel)
                    damage_soul.deploy_initial()
                
                if self.临机制胜发动总次数 % 4 == 0:
                    # [周瑜]执行来自【临机制胜】的「临机制胜-恢复」效果
                    Log().show_battle_info('        [{}]执行来自【{}】的[临机制胜-恢复]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                    treatment_times = msg_对己方所有目标生效_number(self.target, battleField, 3)
                    treatment_heroes = 对己方所有目标生效(self.target, battleField)
                    for _ in range(treatment_times):
                        if len(treatment_heroes) == 0:
                            break

                        treatment: Hero = 从队列确定受击武将(treatment_heroes, skill=self.skill, hero=self.target, battleField=battleField)
                        treatmentValue = 治疗计算(battleField, atta_hero, treatment, self.skill.临机制胜_治疗系数())

                        # 创建一个治疗 SOUL
                        treatment_soul = Soul(target=treatment,
                                              initiator=atta_hero,
                                              effect_type=SoulEffectType.恢复兵力,
                                              effect_value=treatmentValue,
                                              source_soul=self,
                                              battleField=battleField)
                        treatment_soul.deploy_initial()

            



class 临机制胜_skill(Skill):

    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        临机制胜soul = 临机制胜_soul(target=持有者and响应者, 
                                    initiator=持有者and响应者, 
                                    sourceType=SoulSourceType.武将战法, 
                                    skill=self, 
                                    response_time=SoulResponseTime.战法布阵开始时, 
                                    effect_type=SoulEffectType.无影响)
        持有者and响应者.get_持有Soul列表().append(临机制胜soul)
        持有者and响应者.get_响应Soul列表().append(临机制胜soul)

    def 临机制胜_伤害系数(self):
        # 初始值为 60%
        # 每一级升阶提升基础初始值为 1.4%
        rankUp = self.get_战法升阶()
        value = 0.6 + rankUp * 0.014
        return value
    
    def 临机制胜_治疗系数(self):
        # 初始值为 40%
        # 每一级升阶提升基础初始值为 1.2%
        rankUp = self.get_战法升阶()
        value = 0.4 + rankUp * 0.012
        return value