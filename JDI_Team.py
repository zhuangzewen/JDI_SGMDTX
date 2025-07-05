
from JDI_Hero import Hero, HeroInfo
from JDI_Log import Log

class TeamInfo():
    def __init__(self, formation, firstHeroInfo, secondHeroInfo, thirdHeroInfo, teamName='', supply=100):
        self.formation = formation
        self.firstHeroInfo: HeroInfo = firstHeroInfo
        self.firstHeroInfo.set_team_name(teamName)
        self.secondHeroInfo: HeroInfo = secondHeroInfo
        self.secondHeroInfo.set_team_name(teamName)
        self.thirdHeroInfo: HeroInfo = thirdHeroInfo
        self.thirdHeroInfo.set_team_name(teamName)
        self.teamName = teamName
        self.supply = supply

        Log().show_debug_info('DEBUG------- 队伍信息初始化完成: {}'.format(self.teamName))
        Log().show_debug_info('DEBUG------- 队伍信息: {}'.format(self.__dict__))
        Log().show_debug_info('DEBUG------- 队伍名称: {}'.format(teamName))

class Team():
    def __init__(self, teamInfo: TeamInfo, firstHero: Hero, secondHero: Hero, thirdHero: Hero):
        self.teamInfo = teamInfo
        self.firstHero = firstHero
        self.secondHero = secondHero
        self.thirdHero = thirdHero
        self.造成伤害降低 = 0
        self.全队累计治疗量 = 0