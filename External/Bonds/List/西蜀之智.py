# 战法名称: 西蜀之智
# 战法类型: 缘分

# 西蜀之智:
# 法正、诸葛亮、庞统、徐庶、SP诸葛亮
# 缘分关系3人在同一队伍时激活效果
# 部队中缘分武将受到谋略伤害降低8%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 西蜀之智_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.西蜀之智
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.法正,
            Generals_Name_Enum.诸葛亮,
            Generals_Name_Enum.庞统,
            Generals_Name_Enum.徐庶,
            Generals_Name_Enum.诸葛亮SP
        ]
        self.缘分武将生效数量 = 3
        
class 西蜀之智_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 西蜀之智_effect(team, effect_hero_list):
            # 为缘分武将添加受到谋略伤害降低效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    受到谋略伤害降低soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effect_type=SoulEffectType.受到谋略伤害降低,
                        effect_value= -0.08,  # 降低8%
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
            bond_name="西蜀之智",
            effect_callback=西蜀之智_effect
        )


class 西蜀之智_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        西蜀之智soul = 西蜀之智_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 西蜀之智soul