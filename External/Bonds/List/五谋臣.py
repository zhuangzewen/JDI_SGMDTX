# 战法名称: 五谋臣
# 战法类型: 缘分

# 五谋臣:
# 荀彧、荀攸、程昱、贾诩、郭嘉
# 缘分关系3人在同一队伍时激活效果
# 部队中缘分武将特技被提升5%，受到伤害降低4%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum, Log
)

class 五谋臣_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.五谋臣
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.荀彧,
            Generals_Name_Enum.荀攸,
            Generals_Name_Enum.程昱,
            Generals_Name_Enum.贾诩,
            Generals_Name_Enum.郭嘉
        ]
        self.缘分武将生效数量 = 3
        
class 五谋臣_soul(Soul):

   def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 五谋臣_effect(team, effect_hero_list):
            # 为缘分武将添加特技提升和伤害降低效果
            for effect_hero in effect_hero_list:
                破甲提升 = 0.05
                伤害降低 = -0.04

                破甲提升soul = Soul(
                    target = effect_hero,
                    initiator = self.target, 
                    skill = self.skill, 
                    effect_type = SoulEffectType.破甲,
                    effect_value = 破甲提升,
                    source_soul = self,
                    battleField = battleField
                )
                破甲提升soul.deploy_initial()

                伤害降低soul = Soul(
                    target = effect_hero,
                    initiator = self.target, 
                    skill = self.skill, 
                    effect_type = SoulEffectType.受到伤害降低,
                    effect_value = 伤害降低,
                    source_soul = self,
                    battleField = battleField
                )
                伤害降低soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="五谋臣",
            effect_callback=五谋臣_effect
        )


class 五谋臣_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者:Hero = self.get_持有者()
        五谋臣soul = 五谋臣_soul(
                            target=持有者, 
                            initiator=持有者, 
                            skill=self)
        return 五谋臣soul