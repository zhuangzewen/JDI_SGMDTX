# 战法名称: 国之栋梁
# 战法类型: 缘分

# 国之栋梁:
# 司马懿、诸葛亮、SP诸葛亮、周瑜
# 缘分关系3人在同一队伍时激活效果
# 战斗中造成的前3次谋略伤害提升50%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum, Log
)
from Soul.Enum.SoulDamageType_Enum import SoulDamageType

class 国之栋梁_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.国之栋梁
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.司马懿,
            Generals_Name_Enum.诸葛亮,
            Generals_Name_Enum.诸葛亮SP,
            Generals_Name_Enum.周瑜
        ]
        self.缘分武将生效数量 = 3
        
class 国之栋梁_soul(Soul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill=skill)


    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 国之栋梁_effect(team, effect_hero_list):
            pass
                    
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="国之栋梁",
            effect_callback=国之栋梁_effect
        )

class 国之栋梁_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者:Hero = self.get_持有者()
        国之栋梁soul = 国之栋梁_soul(
                            target=持有者, 
                            initiator=持有者, 
                            skill=self)
        return 国之栋梁soul