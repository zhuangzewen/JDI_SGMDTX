# JDI_SGMDTX 项目全局导入头文件
# 统一管理所有模块的导入，简化项目中的 import 语句
# 使用方式: from Control.Imports.global_imports import *

# ================================
# 标准库导入
# ================================
from enum import Enum

# ================================
# 日志系统
# ================================
from Control.Log.JDI_Log import Log

# ================================
# 武将系统
# ================================
from Generals.JDI_Hero import HeroInfo, Hero, get_hero_info
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType, HeroInfoKey

# ================================
# 战场系统
# ================================
from BattleField.JDI_BattleField import BattleField
from BattleField.Team.JDI_Team import TeamInfo, Team, Formation

# ================================
# 技能系统
# ================================
from External.JDI_Skill import Skill, get_skill
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingInfoKey_Enum import SkillInfoKey

# ================================
# 魂灵(效果)系统
# ================================
from Soul.JDI_Soul import Soul
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Soul.Class.Damage_Class import Damage

# ================================
# 计算系统
# ================================
from Calcu.JDI_Calculate import *
from Calcu.JDI_RanVal import *

# ================================
# 羁绊系统
# ================================
from External.Bonds.Enum.BondsList_Enum import BondsList_Enum

# ================================
# 导出所有常用类和枚举
# ================================
__all__ = [
    # 基础类
    'Enum', 'Log',
    
    # 武将系统
    'HeroInfo', 'Hero', 'get_hero_info', 'Generals_Name_Enum', 
    'Faction', 'WeaponType', 'HeroInfoKey',
    
    # 战场系统
    'BattleField', 'TeamInfo', 'Team', 'Formation',
    
    # 技能系统
    'Skill', 'get_skill', 'Fitting_List_Enum', 'SkillType', 'SkillInfoKey',
    
    # 魂灵系统
    'Soul', 'SoulEffectType', 'SoulSourceType', 'SoulResponseTime', 
    'SoulDamageType', 'Damage',
    
    # 羁绊系统
    'BondsList_Enum',
]
