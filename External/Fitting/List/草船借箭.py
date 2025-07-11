
# 战法名称: 草船借箭
# 战法类型: 指挥
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 草船借箭:
# 自身攻心提升24%,自身受到或造成伤害时,有50%概率对敌方随机单体造成80%谋略伤害,每回合可触发5次

# 满阶草船借箭:
# 自身攻心提升27.5%,自身受到或造成伤害时,有50%概率对敌方随机单体造成92%谋略伤害,每回合可触发5次

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

class 草船借箭_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.草船借箭
        self.战法类型 = SkillType.指挥
        self.战法特性 = SkillFeature.谋略
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1
        self.战法响应时机列表 = [SoulResponseTime.战法布阵开始时, SoulResponseTime.每回合重置阶段, SoulResponseTime.造成伤害时, SoulResponseTime.受到伤害时]

class 草船借箭_soul(Soul):
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
        self.soul持有列表 = []
        self.草船借箭发动次数 = 0

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        
        if hero != self.initiator:
            return
        
        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.target == self.target:
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

        if self.soul持有列表.__len__() <= 0:
            return

        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                soul.restore_initial()
                soul_to_remove.append(soul)

        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):

        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
            草船借箭攻心soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.攻心, 
                            effect_value=self.skill.草船借箭_攻心提升系数())
            草船借箭攻心soul.deploy_initial()
            self.soul持有列表.append(草船借箭攻心soul)

        elif status == SoulResponseTime.每回合重置阶段:
            self.草船借箭发动次数 = 0

        elif status == SoulResponseTime.造成伤害时 or status == SoulResponseTime.受到伤害时:

            if hero != self.target:
                return
            
            if status == SoulResponseTime.造成伤害时 and sourceSoul == self:
                return

            

            if self.草船借箭发动次数 < 5:
                if random.random() > 0.5:
                    return
                
                Log().show_battle_info('        [{}]执行来自【{}】的[草船借箭]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

                self.草船借箭发动次数 += 1

                atta_hero = self.target
                attaHero_name = atta_hero.get_武将名称()
                attacked_heroes = 对敌方所有目标生效(atta_hero, battleField)
                attacked: Hero = 从队列确定受击武将(attacked_heroes)

                damageModel = 计算伤害(battleField, atta_hero, attacked, SoulDamageType.谋略, SkillType.指挥, 伤害值= self.skill.草船借箭_借箭伤害系数())
                damageModel.skillEffectName = "草船借箭"

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

class 草船借箭_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)
        self.当前回合发动次数 = 0

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        草船借箭soul = 草船借箭_soul(target=持有者and响应者, 
                                    initiator=持有者and响应者, 
                                    sourceType=SoulSourceType.武将战法, 
                                    skill=self, 
                                    response_time=SoulResponseTime.战法布阵开始时, 
                                    effect_type=SoulEffectType.无影响)
        持有者and响应者.get_持有Soul列表().append(草船借箭soul)
        持有者and响应者.get_响应Soul列表().append(草船借箭soul)

    def 草船借箭_攻心提升系数(self):
        # 初始值为 24%
        # 每一级升阶提升基础初始值为 0.7%

        rankUp = self.get_战法升阶()
        value = 0.24 + rankUp * 0.007
        return value
    
    def 草船借箭_借箭伤害系数(self):
        # 初始值为 80%
        # 每一级升阶提升基础初始值为 2.4%

        rankUp = self.get_战法升阶()
        value = 0.8 + rankUp * 0.024
        return value