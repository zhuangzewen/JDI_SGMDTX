# 战法名称: 珠联璧合
# 战法类型: 缘分

# 珠联璧合:
# 刘备、孙尚香
# 缘分关系2人在同一队伍时激活效果
# 队伍中缘分武将受到谋略伤害降低6%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 珠联璧合_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.珠联璧合
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备, Generals_Name_Enum.孙尚香]
        self.缘分武将生效数量 = 2
        
class 珠联璧合_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 珠联璧合_effect(team, effect_hero_list):
            # 为缘分武将添加受到谋略伤害降低效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    受到谋略伤害降低soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effect_type=SoulEffectType.受到谋略伤害降低,
                        effect_value= -0.06,
                        source_soul=self,
                        battleField=battleField
                    )
                    受到谋略伤害降低soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="珠联璧合",
            effect_callback=珠联璧合_effect
        )


class 珠联璧合_skill(Skill):
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
        持有者and响应者:Hero = self.get_持有者()
        珠联璧合soul = 珠联璧合_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 珠联璧合soul