# 战法名称: 虎卫御侮
# 战法类型: 缘分

# 虎卫御侮:
# 许褚 典韦 曹操
# 缘分关系3人在同一队伍时激活效果
# 队伍中缘分武将普通攻击伤害提升12%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Log, Generals_Name_Enum, BondsName_Enum
)

class 虎卫御侮_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.虎卫御侮
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.许褚, Generals_Name_Enum.典韦, Generals_Name_Enum.曹操]
        self.缘分武将生效数量 = 3
        
class 虎卫御侮_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 虎卫御侮_effect(team, effect_hero_list):
            
            for effect_hero in effect_hero_list:
                普攻伤害提升soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effectType=SoulEffectType.普通攻击造成伤害提升,
                    effectValue=0.12,
                    sourceSoul=self,
                )
                普攻伤害提升soul.deploy_initial()
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="虎卫御侮",
            effect_callback=虎卫御侮_effect
        )


class 虎卫御侮_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        虎卫御侮soul = 虎卫御侮_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 虎卫御侮soul