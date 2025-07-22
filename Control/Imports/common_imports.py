# JDI_SGMDTX 项目常用导入头文件
# 包含最常用的类和枚举，适用于大部分文件
# 使用方式: from Control.Imports.common_imports import *

# ================================
# 最常用的导入
# ================================
from enum import Enum
from Control.Log.JDI_Log import Log

# 武将系统 - 核心
from Generals.JDI_Hero import get_hero_info
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType

# 战场系统 - 核心  
from BattleField.JDI_BattleField import BattleField
from BattleField.Team.JDI_Team import TeamInfo, Formation

# 技能系统 - 核心
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum

# 魂灵系统 - 核心
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime

# ================================
# 导出常用类和枚举
# ================================
__all__ = [
    'Enum', 'Log', 'get_hero_info', 'Generals_Name_Enum', 
    'Faction', 'WeaponType', 'BattleField', 'TeamInfo', 'Formation',
    'Fitting_List_Enum', 'SoulEffectType', 'SoulSourceType', 'SoulResponseTime'
]
