
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

    def __init__(self, target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        pass

class 临机制胜_skill(Skill):

    def __init__(self, name, info, init_rate, max_level, levelup_rate, cost_list, effect_list, description):
        super().__init__(name, info, init_rate, max_level, levelup_rate, cost_list, effect_list, description)

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