# 战法名称: 乱世红颜
# 战法类型: 缘分

# 乱世红颜:
# 甘夫人、貂蝉、蔡文姬、邹氏、王异、甄洛、孙尚香
# 缘分关系3人在同一队伍时激活效果
# 战斗开始时，队伍中缘分武将获得2层抵御

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 乱世红颜_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.乱世红颜
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.甘夫人,
            Generals_Name_Enum.貂蝉,
            Generals_Name_Enum.蔡文姬,
            Generals_Name_Enum.邹氏,
            Generals_Name_Enum.王异,
            Generals_Name_Enum.甄洛,
            Generals_Name_Enum.孙尚香
        ]
        self.缘分武将生效数量 = 3
        
class 乱世红颜_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 乱世红颜_effect(team, effect_hero_list):
            # 为缘分武将添加抵御效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    抵御soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effect_type=SoulEffectType.抵御,
                        effect_value= 2,  # 2层抵御
                        source_soul=self,
                        battleField=battleField
                    )
                    抵御soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="乱世红颜",
            effect_callback=乱世红颜_effect
        )


class 乱世红颜_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 3:
            return False

        return True

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        乱世红颜soul = 乱世红颜_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 乱世红颜soul