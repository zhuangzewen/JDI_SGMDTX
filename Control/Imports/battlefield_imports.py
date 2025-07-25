# 战场系统专用导入模块
# 包含战场系统开发所需的所有导入
# 使用方式: from Control.Imports.battlefield_imports import *

import random
from enum import Enum
from Control.Log.JDI_Log import Log

# 魂灵系统
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulSourceType_Enum import SoulSourceType  
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.JDI_Soul import Soul

# 武将系统
from Generals.Enum.Generals_Enum import WeaponType, HeroInfoKey
from Generals.JDI_Hero import Hero

# 队伍系统
from BattleField.Team.JDI_Team import TeamInfo, Team, Formation

# 技能系统
from External.Fitting.JDI_Skill import Skill
from External.Fitting.Enum.FittingType_Enum import SkillType

# 计算系统 - 明确导入需要的函数
from Calcu.JDI_Calculate import (
    武将行动队列, msg_实际减伤系数, msg_过滤掉被击溃的武将, 
    msg_判断己方前排武将数量, msg_对我方的单前排生效, 
    msg_对我方统帅最低的武将, msg_对我方智力最高的武将,
    对己方所有目标生效, 对己方阵型强化SOUL生效, 实际受击率,
    从队列确定受击单位, 对敌方所有目标生效, 生效未施加的异常状态
)

__all__ = [
    'random', 'Enum', 'Log', 'SoulEffectType', 'SoulSourceType', 'SoulResponseTime', 'Soul',
    'WeaponType', 'HeroInfoKey', 'Hero', 'TeamInfo', 'Team', 'Formation', 'Skill', 'SkillType',
    '武将行动队列', 'msg_实际减伤系数', 'msg_过滤掉被击溃的武将', 'msg_判断己方前排武将数量',
    'msg_对我方的单前排生效', 'msg_对我方统帅最低的武将', 'msg_对我方智力最高的武将',
    '对己方所有目标生效', '对己方阵型强化SOUL生效', '实际受击率', '从队列确定受击单位',
    '对敌方所有目标生效', '生效未施加的异常状态'
]
