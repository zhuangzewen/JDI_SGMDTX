
# 战法名称: 才堪相配
# 战法类型: 缘分

# 才堪相配:
# 诸葛亮 SP诸葛亮 黄月英
# 缘分关系2人在同一队伍时激活效果
# 部队中缘分武将收到的治疗效果提升8%


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
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum

class 才堪相配_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.才堪相配
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.诸葛亮, Generals_Name_Enum.SP诸葛亮, Generals_Name_Enum.黄月英]
        
class 才堪相配_soul(Soul):
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

class 才堪相配_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        模版_soul = 模版_soul(target=持有者and响应者, 
                                     initiator=持有者and响应者, 
                                     sourceType=SoulSourceType.武将战法, 
                                     skill=self, 
                                     response_time=SoulResponseTime.内置待响应, 
                                     effect_type=SoulEffectType.无影响)
        持有者and响应者.get_持有Soul列表().append(模版_soul)
        持有者and响应者.get_响应Soul列表().append(模版_soul)

    def 模版_系数(self):
        rankUp = self.get_战法升阶()
        value = 20 + rankUp * 0.4
        return value
    

