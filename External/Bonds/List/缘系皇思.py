# 战法名称: 缘系皇思
# 战法类型: 缘分

# 缘系皇思:
# 刘备
# 缘分关系X人在同一队伍时激活效果
# 【具体效果待补充】

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
from External.SkillBaseTemplate import BaseSkillSoul, BaseSkill
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from External.Bonds.BondUtils import BondUtils

class 缘系皇思_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.缘系皇思
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备]  # 待补充其他缘分武将
        self.缘分武将生效数量 = 1  # 待确认实际数量要求
        
class 缘系皇思_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 缘系皇思_effect(team, effect_hero_list):
            # TODO: 添加具体的效果逻辑
            # 这里需要根据缘系皇思的具体效果来实现
            pass
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="缘系皇思",
            effect_callback=缘系皇思_effect
        )


class 缘系皇思_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 1:
            return False

        return True

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        缘系皇思soul = 缘系皇思_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 缘系皇思soul
