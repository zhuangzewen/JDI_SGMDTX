# 战法名称: 五虎上将
# 战法类型: 缘分

# 五虎上将:
# 关羽、张飞、马超、赵云、黄忠
# 缘分关系3人在同一队伍时激活效果
# 队伍中缘分武将会心几率提升10%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum
)

class 五虎上将_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.五虎上将
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.关羽, Generals_Name_Enum.张飞, Generals_Name_Enum.马超, Generals_Name_Enum.赵云, Generals_Name_Enum.黄忠]
        self.缘分武将生效数量 = 3
        
class 五虎上将_soul(Soul):

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 五虎上将_effect(team, effect_hero_list):
            # 为缘分武将添加会心几率提升效果
            for effect_hero in effect_hero_list:
                if effect_hero.get_武将名称() in self.skill.get_战法信息().缘分武将:
                    会心几率提升soul = Soul(
                        target=effect_hero,
                        initiator=self.target,
                        skill=self.skill,
                        effect_type=SoulEffectType.会心几率,
                        effect_value= 0.10,
                        source_soul=self,
                        battleField=battleField
                    )
                    会心几率提升soul.deploy_initial()
                
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="五虎上将",
            effect_callback=五虎上将_effect
        )


class 五虎上将_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        五虎上将soul = 五虎上将_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 五虎上将soul