# 战法名称: 仁义昭烈
# 战法类型: 缘分

# 仁义昭烈:
# 刘备
# 缘分关系1人在同一队伍时激活效果
# 问鼎赛季时,我军全体激活的阵营加成 -【蜀】效果提升50%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 仁义昭烈_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.仁义昭烈
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备]
        self.缘分武将生效数量 = 1
        
class 仁义昭烈_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 仁义昭烈_effect(team, effect_hero_list):
            # 遍历所有武将，找到蜀阵营加成soul并提升50%
            alive_heroes = BondUtils.get_alive_team_heroes(team)
            for hero in alive_heroes:
                # 遍历该武将的所有soul，找到蜀阵营加成相关的soul
                for soul in hero.get_响应Soul列表():
                    # 检查是否是蜀阵营加成soul
                    if hasattr(soul, 'sourceType') and soul.sourceType == SoulSourceType.蜀阵营加成:
                        # 对现有的蜀阵营加成效果提升50%
                        原始效果值 = soul.effectValue
                        提升值 = 原始效果值 * 0.5  # 提升50%
                        
                        # 创建额外的提升soul
                        蜀加成提升soul = Soul(target=hero,
                                            initiator=self.target,
                                            skill=self.skill,
                                            effectType=soul.effectType,
                                            effectValue=提升值,
                                            sourceSoul=self,
                                            battleField=battleField)
                        蜀加成提升soul.deploy_initial()
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="仁义昭烈",
            effect_callback=仁义昭烈_effect
        )


class 仁义昭烈_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        仁义昭烈soul = 仁义昭烈_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 仁义昭烈soul

