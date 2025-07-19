
# 战法名称: 裸衣血战
# 战法类型: 被动
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 裸衣血战:
# 战斗开始时,自身先攻和武力提升20点,连击率提升100%,统率降低15点。自身造成伤害额外提升0%

# 满阶裸衣血战:
# 战斗开始时,自身先攻和武力提升22点,连击率提升100%,统率降低15点。自身造成伤害额外提升5%

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
# 模仿草船借箭 完成这页的实现

class 裸衣血战_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.裸衣血战
        self.战法类型 = SkillType.被动
        self.战法特性 = SkillFeature.兵刃
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 裸衣血战_soul(Soul):
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

        msg_移除响应(self)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

            裸衣血战先攻soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.先攻, 
                            effect_value=self.skill.裸衣血战_先攻_提升系数())
            裸衣血战先攻soul.deploy_initial()
            self.soul持有列表.append(裸衣血战先攻soul)

            裸衣血战武力soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.武力, 
                            effect_value=self.skill.裸衣血战_武力_提升系数())
            裸衣血战武力soul.deploy_initial()
            self.soul持有列表.append(裸衣血战武力soul)

            裸衣血战连击率soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.连击几率, 
                            effect_value=self.skill.裸衣血战_连击率_提升系数())
            裸衣血战连击率soul.deploy_initial()
            self.soul持有列表.append(裸衣血战连击率soul)

            裸衣血战统帅soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.统帅, 
                            effect_value=-self.skill.裸衣血战_统帅_降低系数(),
                            battleField=battleField)
            裸衣血战统帅soul.deploy_initial()
            self.soul持有列表.append(裸衣血战统帅soul)

            裸衣血战造成伤害soul = Soul(target=self.target,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.造成伤害, 
                            effect_value=self.skill.裸衣血战_造成伤害_提升系数())
            裸衣血战造成伤害soul.deploy_initial()
            self.soul持有列表.append(裸衣血战造成伤害soul)

class 裸衣血战_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        裸衣血战soul = 裸衣血战_soul(target=持有者and响应者, 
                                     initiator=持有者and响应者, 
                                     sourceType=SoulSourceType.武将战法, 
                                     skill=self, 
                                     response_time=SoulResponseTime.战法布阵开始时, 
                                     effect_type=SoulEffectType.无影响)
        持有者and响应者.get_持有Soul列表().append(裸衣血战soul)
        持有者and响应者.get_响应Soul列表().append(裸衣血战soul)

    def 裸衣血战_先攻_提升系数(self):
        rankUp = self.get_战法升阶()
        value = 20 + rankUp * 0.4
        return value
    
    def 裸衣血战_武力_提升系数(self):
        rankUp = self.get_战法升阶()
        value = 20 + rankUp * 0.4
        return value
    
    def 裸衣血战_连击率_提升系数(self):
        return 1
    
    def 裸衣血战_统帅_降低系数(self):
        return 15
    
    def 裸衣血战_造成伤害_提升系数(self):
        rankUp = self.get_战法升阶()
        return rankUp * 0.01

