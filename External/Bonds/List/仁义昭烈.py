
# 战法名称: 仁义昭烈
# 战法类型: 缘分

# 仁义昭烈:
# 刘备
# 缘分关系1人在同一队伍时激活效果
# 问鼎赛季时,我军全体激活的阵营加成 -【蜀】效果提升50%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Log, Generals_Name_Enum
)

class 仁义昭烈_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.仁义昭烈
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备]
        self.缘分武将生效数量 = 1
        
class 仁义昭烈_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

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
                        原始效果值 = soul.effect_value
                        提升值 = 原始效果值 * 0.5  # 提升50%
                        
                        # 创建额外的提升soul
                        蜀加成提升soul = Soul(target=hero,
                                            initiator=self.target,
                                            sourceType=SoulSourceType.不溯源,
                                            skill=self.skill,
                                            response_time=SoulResponseTime.无响应阶段,
                                            duration=-1,
                                            effect_type=soul.effect_type,  # 使用相同的效果类型
                                            effect_value=提升值,
                                            source_soul=self,
                                            battleField=battleField)
                        蜀加成提升soul.deploy_initial()
                        hero.get_响应Soul列表().append(蜀加成提升soul)
                        
                        Log().battle_L2('[{}]的【{}】提升{:.2f}({:.2f})'.format(
                            hero.get_武将名称().value, 
                            soul.effect_type.value if hasattr(soul.effect_type, 'value') else str(soul.effect_type),
                            提升值,
                            原始效果值 + 提升值
                        ))
        
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

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 1:
            return False

        return True

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        仁义昭烈soul = 仁义昭烈_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 仁义昭烈soul

