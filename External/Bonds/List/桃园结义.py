# 战法名称: 桃园结义
# 战法类型: 缘分

# 桃园结义:
# 关羽、张飞、刘备
# 缘分关系3人在同一队伍时激活效果
# 第3回合时,队伍中缘分武将行动前驱散自身全部负面状态

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)
from External.SkillBaseTemplate import BaseSkillSoul
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from BattleField.Team.JDI_Team import Team
from Control.Log.JDI_Log import Log

class 桃园结义_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.桃园结义
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.关羽, Generals_Name_Enum.张飞, Generals_Name_Enum.刘备]
        self.缘分武将生效数量 = 3
        
class 桃园结义_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        # 检查是否在第3回合
        if battleField.current_round != 3:
            return

        def 桃园结义_effect(team, effect_hero_list):
            
            
            
            for effect_hero in effect_hero_list:
                effect_hero: Hero

                驱散异常响应soul = 桃园结义_驱散异常soul(
                    target=effect_hero,
                    initiator=effect_hero,
                    skill=self.skill,
                    source_soul=self,
                    battleField=battleField
                )
                effect_hero.get_响应Soul列表().append(驱散异常响应soul)
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=SoulResponseTime.战法布阵开始时,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="桃园结义",
            effect_callback=桃园结义_effect
        )

    

class 桃园结义_驱散异常soul(BaseSkillSoul):
    def 驱散负面状态(self, hero: Hero):

        # 遍历并移除负面状态
        要移除的soul = []
        for soul in hero.get_响应Soul列表():
            soul: Soul
            if soul.sourceType == SoulSourceType.控制状态效果:
                要移除的soul.append(soul)

        for soul in hero.get_响应Soul列表():
            soul: Soul
            if soul.sourceType == SoulSourceType.异常状态效果:
                要移除的soul.append(soul)

        for soul in hero.get_响应Soul列表():
            soul: Soul
            if soul.sourceType == SoulSourceType.负面状态效果:
                要移除的soul.append(soul)

        for soul in 要移除的soul:
            soul: Soul
            soul.restore_initial()
            hero.get_响应Soul列表().remove(soul)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        # 检查是否在第3回合
        if battleField.current_round != 3:
            return

        # 检查是否在武将行动前
        if status != SoulResponseTime.武将回合重置阶段 or hero != self.target:
            return

        def 桃园结义_effect(team, effect_hero_list):
            # 为缘分武将驱散负面状态
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    # 驱散所有负面状态
                    self.驱散负面状态(effect_hero)
                    Log().battle_L1('[{}]的【桃园结义】效果触发，{}驱散了自身全部负面状态'.format(
                        team.teamInfo.teamName, effect_hero.get_武将名称()))
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=SoulResponseTime.战法布阵开始时,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="桃园结义",
            effect_callback=桃园结义_effect
        )

class 桃园结义_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        桃园结义soul = 桃园结义_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 桃园结义soul