
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