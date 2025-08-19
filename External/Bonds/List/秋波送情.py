# 战法名称: 秋波送情
# 战法类型: 缘分

# 秋波送情:
# 吕布、貂蝉
# 缘分关系2人在同一队伍时激活效果
# 队伍中缘分武将受到普通攻击伤害降低12%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 秋波送情_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.秋波送情
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.吕布, Generals_Name_Enum.貂蝉]
        self.缘分武将生效数量 = 2
        
class 秋波送情_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 秋波送情_effect(team, effect_hero_list):
            # 为缘分武将添加受到普通攻击伤害降低效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    普通攻击减伤soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effectType=SoulEffectType.受到普通攻击伤害降低,
                        effectValue= -0.12,
                        sourceSoul=self,
                        battleField=battleField
                    )
                    普通攻击减伤soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="秋波送情",
            effect_callback=秋波送情_effect
        )


class 秋波送情_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        秋波送情soul = 秋波送情_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 秋波送情soul