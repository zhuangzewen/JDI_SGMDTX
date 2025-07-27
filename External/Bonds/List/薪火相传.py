# 战法名称: 薪火相传
# 战法类型: 缘分

# 薪火相传:
# 姜维、诸葛亮、SP诸葛亮
# 缘分关系2人在同一队伍时激活效果
# 部队中缘分武将智力和统率提升6%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum, Log
)

class 薪火相传_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.薪火相传
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.姜维,
            Generals_Name_Enum.诸葛亮,
            Generals_Name_Enum.诸葛亮SP
        ]
        self.缘分武将生效数量 = 2
        
class 薪火相传_soul(Soul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill)

    def response(self, status = SoulResponseTime.无响应阶段, battlefield=None, hero = None, sourceSoul=None):
        def 薪火相传_effect(team, effect_hero_list):
            # 为缘分武将添加智力和统率提升效果
            for effect_hero in effect_hero_list:
                # 智力提升6%
                智力提升soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effect_type=SoulEffectType.智力,
                    effect_value= 0.06,  # 提升6%
                    source_soul=self,
                    battlefield=battlefield,
                    duration=99  # 持续战斗结束
                )
                智力提升soul.deploy_initial()
                
                # 统率提升6%
                统率提升soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effect_type=SoulEffectType.统率,
                    effect_value= 0.06,  # 提升6%
                    source_soul=self,
                    battlefield=battlefield,
                    duration=99  # 持续战斗结束
                )
                统率提升soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battlefield,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="薪火相传",
            effect_callback=薪火相传_effect
        )


class 薪火相传_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 2:
            return False

        return True

    def fill_init_soul(self):
        持有者:Hero = self.get_持有者()
        薪火相传soul = 薪火相传_soul(
                            target=持有者, 
                            initiator=持有者, 
                            skill=self)
        return 薪火相传soul