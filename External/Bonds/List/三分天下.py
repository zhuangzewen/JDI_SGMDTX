# 战法名称: 三分天下
# 战法类型: 缘分

# 三分天下:
# 曹操 刘备 孙权
# 缘分关系3人在同一队伍时激活效果
# 部队中缘分武将收到伤害降低6%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType, Fitting_List_Enum,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Log, Generals_Name_Enum, msg_实际减伤系数
)

class 三分天下_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.三分天下
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.曹操, Generals_Name_Enum.刘备, Generals_Name_Enum.孙权]
        self.缘分武将生效数量 = 3  # 需要3人在同一队伍时激活
        
class 三分天下_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero, 
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 三分天下_effect(team, effect_hero_list):
            # 三分天下效果：缘分武将受到伤害降低6%
            Log().battle_L1('[{}]获得【三分天下】强化效果'.format(team.teamInfo.teamName))
            
            for effect_hero in effect_hero_list:

                伤害减免soul = Soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effect_type=SoulEffectType.受到伤害,
                    effect_value=msg_实际减伤系数(hero, -0.06),  # 负值表示减少伤害
                    source_soul=self,
                    battleField=battleField
                )
                伤害减免soul.deploy_initial()
                effect_hero.get_响应Soul列表().append(伤害减免soul)
        
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="三分天下",
            effect_callback=三分天下_effect
        )


class 三分天下_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def check_缘分(self, team = None):
        存在缘分武将 = []
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in self.get_战法信息().缘分武将:
                存在缘分武将.append(hero)

        if len(存在缘分武将) < 3:
            return False

        return True

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        三分天下soul = 三分天下_soul(
                            target=持有者and响应者, 
                            initiator=持有者and响应者, 
                            skill=self)
        return 三分天下soul
