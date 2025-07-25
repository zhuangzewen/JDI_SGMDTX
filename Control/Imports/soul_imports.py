# 魂灵系统专用导入模块
# 包含魂灵系统开发所需的所有导入
# 使用方式: from Control.Imports.soul_imports import *

from Control.Log.JDI_Log import Log
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Class.Damage_Class import Damage
from Calcu.JDI_Calculate import msg_移除响应

# 为了避免循环导入，这些类将在运行时导入
# from External.JDI_Skill import Skill
# from Generals.JDI_Hero import Hero

__all__ = [
    'Log', 'SoulEffectType', 'HeroInfoKey', 'SoulSourceType', 'SoulResponseTime',
    'Fitting_List_Enum', 'Damage', 'msg_移除响应'
]
