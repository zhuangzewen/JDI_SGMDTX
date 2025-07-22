
# 战法名称: 仁义昭烈
# 战法类型: 缘分

# 仁义昭烈:
# 刘备
# 缘分关系1人在同一部队时激活效果
# 问鼎赛季时,我军全体激活的阵营加成 -【蜀】效果提升50%


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
from Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum

class 仁义昭烈_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.仁义昭烈
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [Generals_Name_Enum.刘备]
        self.缘分武将生效数量 = 1
        
class 仁义昭烈_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        
        if hero != self.initiator:
            return
        
        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.target == self.target:
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

        if self.soul持有列表.__len__() <= 0:
            return

        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                soul.restore_initial()
                soul_to_remove.append(soul)

        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)

        msg_移除响应(self)

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
            Log().show_battle_info('缘分发动失败: [{}]缘分武将数量: {}，满足条件: {}'.format(
                self.target.get_武将名称().value, num_缘分武将, 缘分武将生效数量))
            return

        Log().show_battle_info('    [{}]获得【仁义昭烈】强化效果'.format(team.teamInfo.teamName))

        # 确认目标


class 仁义昭烈_skill(Skill):
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
        仁义昭烈soul = 仁义昭烈_soul(target=持有者and响应者, 
                             initiator=持有者and响应者, 
                             sourceType=SoulSourceType.武将战法, 
                             skill=self, 
                             response_time=SoulResponseTime.内置待响应, 
                             effect_type=SoulEffectType.无影响)
        return 仁义昭烈soul
    

