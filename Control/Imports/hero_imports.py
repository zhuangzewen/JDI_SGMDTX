# 武将系统专用导入模块
# 包含武将系统开发所需的所有导入
# 使用方式: from Control.Imports.hero_imports import *

from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType, HeroInfoKey
from External.JDI_Skill import get_skill
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Calcu.JDI_Calculate import *
from Control.Log.JDI_Log import Log
from External.Bonds.Enum.BondsList_Enum import BondsName_Enum

__all__ = [
    'Generals_Name_Enum', 'Faction', 'WeaponType', 'HeroInfoKey', 
    'get_skill', 'Fitting_List_Enum', 'SoulResponseTime', 'SoulDamageType', 'Log',
    'BondsName_Enum'
]
