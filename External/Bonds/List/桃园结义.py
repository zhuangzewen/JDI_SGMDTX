# 战法名称: 桃园结义
# 战法类型: 缘分

# 桃园结义:
# 刘备
# 缘分关系X人在同一队伍时激活效果
# 【具体效果待补充】

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, Soul, Generals_Name_Enum
)

class 桃园结义_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.桃园结义
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备]  # 待补充其他缘分武将
        self.缘分武将生效数量 = 1  # 待确认实际数量要求
        
class 桃园结义_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 桃园结义_effect(team, effect_hero_list):
            # TODO: 添加具体的效果逻辑
            # 这里需要根据桃园结义的具体效果来实现
            pass
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="桃园结义",
            effect_callback=桃园结义_effect
        )


class 桃园结义_skill(Skill):
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
        桃园结义soul = 桃园结义_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 桃园结义soul
