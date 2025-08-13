# 战法名称: 夺射锦袍
# 战法类型: 缘分

# 夺射锦袍:
# 许褚 徐晃
# 缘分关系2人在同一队伍时激活效果
# 队伍中缘分武将破甲提升5%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Log, Generals_Name_Enum, BondsName_Enum
)

class 夺射锦袍_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.夺射锦袍
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.许褚, Generals_Name_Enum.徐晃]
        self.缘分武将生效数量 = 2
        
class 夺射锦袍_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 夺射锦袍_effect(team, effect_hero_list):
            
            for effect_hero in effect_hero_list:
                破甲提升soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effect_type=SoulEffectType.破甲,
                    effect_value=0.05,
                    source_soul=self,
                )
                破甲提升soul.deploy_initial()
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="夺射锦袍",
            effect_callback=夺射锦袍_effect
        )


class 夺射锦袍_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        夺射锦袍soul = 夺射锦袍_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 夺射锦袍soul