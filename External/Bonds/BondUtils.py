# 缘分系统工具模块
# 提供统一的缘分判定和效果处理方法

from typing import List, Tuple, Optional
from Generals.JDI_Hero import Hero
from External.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.JDI_Soul import Soul
from BattleField.Team.JDI_Team import Team
from Control.Log.JDI_Log import Log
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from External.Bonds.Enum.BondsList_Enum import BondsName_Enum

# 导出缘分常用的类和枚举，供缘分文件直接使用
__all__ = [
    'BondUtils', 'Hero', 'SkillInfo', 'Skill', 'SkillType', 'Fitting_List_Enum',
    'SoulResponseTime', 'SoulSourceType', 'SoulEffectType', 'Soul', 'Log', 'Generals_Name_Enum',
    'BondsName_Enum'
]

class BondUtils:
    """缘分系统工具类，提供通用的缘分处理方法"""
    
    @staticmethod
    def check_bond_activation(soul, battlefield, status_requirement=None) -> Tuple[Optional[Team], List[Hero], bool]:
        """
        检查缘分是否能够激活
        
        Args:
            soul: 缘分Soul对象
            battlefield: 战场对象
            status_requirement: 响应时机要求，默认为战法布阵开始时
            
        Returns:
            Tuple[Team, List[Hero], bool]: (所属队伍, 符合条件的缘分武将列表, 是否激活成功)
        """
        from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
        
        # 检查响应时机
        if status_requirement is None:
            status_requirement = SoulResponseTime.战法布阵开始时
            
        # 先判断是哪个 team
        team = None
        if soul in battlefield.team1.缘分soul列表:
            team = battlefield.team1
        elif soul in battlefield.team2.缘分soul列表:
            team = battlefield.team2
        else:
            return None, [], False

        # 获取缘分配置信息
        skill: Skill = soul.skill
        skillInfo: SkillInfo = skill.get_战法信息()
        缘分武将列表 = skillInfo.缘分武将
        缘分武将生效数量 = skillInfo.缘分武将生效数量
        
        # 判断未击溃缘分武将是否足够
        effect_hero_list = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in 缘分武将列表 and hero.get_被击溃状态() != True:
                effect_hero_list.append(hero)

        # 检查是否满足激活条件
        is_activated = len(effect_hero_list) >= 缘分武将生效数量
        
        return team, effect_hero_list, is_activated
    
    @staticmethod
    def log_bond_activation(team: Team, bond_name: str, target_hero: Hero, is_success: bool):
        """
        记录缘分激活日志
        
        Args:
            team: 队伍对象
            bond_name: 缘分名称
            target_hero: 目标武将
            is_success: 是否激活成功
        """
        if is_success:
            Log().battle_L1('[{}]获得【{}】强化效果'.format(team.teamInfo.teamName, bond_name))
        else:
            Log().battle_L1('[{}]发动失败'.format(bond_name))
    
    @staticmethod
    def get_alive_team_heroes(team: Team) -> List[Hero]:
        """
        获取队伍中所有未击溃的武将
        
        Args:
            team: 队伍对象
            
        Returns:
            List[Hero]: 未击溃的武将列表
        """
        alive_heroes = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_被击溃状态() != True:
                alive_heroes.append(hero)
        return alive_heroes
    
    @staticmethod
    def standard_bond_response(soul, status, battlefield=None, hero=None, sourceSoul=None, 
                             bond_name: str = None, effect_callback=None):
        """
        标准的缘分响应处理流程
        
        Args:
            soul: 缘分Soul对象
            status: 响应状态
            battlefield: 战场对象
            hero: 武将对象
            sourceSoul: 来源Soul
            bond_name: 缘分名称（用于日志）
            effect_callback: 效果回调函数，接收(team, effect_hero_list)参数
        """
        from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
        
        # 检查响应时机
        if status != SoulResponseTime.战法布阵开始时:
            return
            
        # 检查缘分激活条件
        team, effect_hero_list, is_activated = BondUtils.check_bond_activation(soul, battlefield, status)
        
        if team is None:
            return
            
        # 记录日志
        if bond_name is None:
            bond_name = "未知缘分"
        BondUtils.log_bond_activation(team, bond_name, soul.target, is_activated)
        
        # 如果激活成功且有效果回调，则执行效果
        if is_activated and effect_callback:
            effect_callback(team, effect_hero_list)
