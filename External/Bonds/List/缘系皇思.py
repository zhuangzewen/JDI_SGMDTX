# 战法名称: 缘系皇思
# 战法类型: 缘分

# 缘系皇思:
# 刘备、甘夫人
# 缘分关系2人在同一队伍时激活效果
# 部队中缘分武将受到兵刃伤害降低6%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 缘系皇思_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.缘系皇思
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备, Generals_Name_Enum.甘夫人]
        self.缘分武将生效数量 = 2
        
class 缘系皇思_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 缘系皇思_effect(team, effect_hero_list):
            # 为缘分武将添加兵刃伤害降低效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    兵刃伤害降低soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effectType=SoulEffectType.受到兵刃伤害降低,
                        effectValue= -0.06,
                        sourceSoul=self,
                        battleField=battleField
                    )
                    兵刃伤害降低soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="缘系皇思",
            effect_callback=缘系皇思_effect
        )


class 缘系皇思_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        缘系皇思soul = 缘系皇思_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 缘系皇思soul