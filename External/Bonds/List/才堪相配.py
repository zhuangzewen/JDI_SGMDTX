
# 战法名称: 才堪相配
# 战法类型: 缘分

# 才堪相配:
# 诸葛亮 SP诸葛亮 黄月英
# 缘分关系2人在同一队伍时激活效果
# 部队中缘分武将收到的治疗效果提升8%


from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Log, Generals_Name_Enum
)

class 才堪相配_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.才堪相配
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.诸葛亮, Generals_Name_Enum.SP诸葛亮, Generals_Name_Enum.黄月英]
        self.缘分武将生效数量 = 2
        
class 才堪相配_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 才堪相配_effect(team, effect_hero_list):
            # 才堪相配效果：缘分武将受治疗效果提升8%
            Log().battle_L1('[{}]获得【才堪相配】强化效果'.format(team.teamInfo.teamName))
            
            for effect_hero in effect_hero_list:
                Log().battle_L1('        [{}]的【受治疗效果】提升8.00%({}%)'.format(
                    effect_hero.get_武将名称().value, 
                    (effect_hero.get_受治疗效果() + 0.08) * 100
                ))
                
                治疗效果soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    sourceType=SoulSourceType.不溯源,
                    skill=self.skill,
                    response_time=SoulResponseTime.无响应阶段,
                    duration=-1,
                    effect_type=SoulEffectType.受治疗效果,
                    effect_value=0.08,
                    source_soul=self,
                    battleField=battleField
                )
                治疗效果soul.deploy_initial()
                effect_hero.get_响应Soul列表().append(治疗效果soul)
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="才堪相配",
            effect_callback=才堪相配_effect
        )


class 才堪相配_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 2:
            return False

        return True

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        才堪相配soul = 才堪相配_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 才堪相配soul
