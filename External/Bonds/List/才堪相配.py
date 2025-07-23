
# 战法名称: 才堪相配
# 战法类型: 缘分

# 才堪相配:
# 诸葛亮 SP诸葛亮 黄月英
# 缘分关系2人在同一队伍时激活效果
# 部队中缘分武将收到的治疗效果提升8%


from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import WeaponType
from External.Fitting.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Soul.JDI_Soul import Soul
from External.SkillBaseTemplate import BaseSkillSoul, BaseSkill
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum

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

        if status != SoulResponseTime.战法布阵开始时:
            return
        
        # 先判断是哪个 team
        if self in battleField.team1.缘分soul列表:
            team = battleField.team1
        elif self in battleField.team2.缘分soul列表:
            team = battleField.team2

        # 判断未击溃缘分武将是否足够
        num_缘分武将 = 0
        effect_hero_list = []
        skill: Skill = self.skill
        skillInfo: SkillInfo = skill.get_战法信息()
        缘分武将列表 = skillInfo.缘分武将
        缘分武将生效数量 = skillInfo.缘分武将生效数量
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if hero.get_武将名称() in 缘分武将列表 and hero.get_被击溃状态() != True:
                num_缘分武将 += 1
                effect_hero_list.append(hero)

        if num_缘分武将 < 缘分武将生效数量:
            Log().show_battle_info('    [{}]发动失败'.format(self.target.get_武将名称().value))
            return

        Log().show_battle_info('    [{}]获得【才堪相配】强化效果'.format(team.teamInfo.teamName))

        # 确认目标
        for effect_hero in effect_hero_list:
            治疗效果soul = Soul(target=effect_hero,
                                    initiator=self.target,
                                    sourceType=SoulSourceType.不溯源,
                                    skill=self.skill,
                                    response_time=SoulResponseTime.无响应阶段,
                                    duration=-1,
                                    effect_type=SoulEffectType.受治疗效果,
                                    effect_value=0.08,
                                    source_soul=self,
                                    battleField=battleField)
            治疗效果soul.deploy_initial()
            effect_hero.get_响应Soul列表().append(治疗效果soul)


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
