
from JDI_Hero import Hero
from JDI_Log import Log

class TeamInfo():
    def __init__(self, formation, firstHeroInfo, secondHeroInfo, thirdHeroInfo, teamName='', supply=100):
        self.formation = formation
        self.firstHeroInfo = firstHeroInfo
        self.secondHeroInfo = secondHeroInfo
        self.thirdHeroInfo = thirdHeroInfo
        self.teamName = teamName
        self.supply = supply

        Log().show_debug_info('DEBUG------- 队伍信息初始化完成: {}'.format(self.teamName))
        Log().show_debug_info('DEBUG------- 队伍信息: {}'.format(self.__dict__))

class Team():
    def __init__(self, teamInfo: TeamInfo, firstHero: Hero, secondHero: Hero, thirdHero: Hero):
        self.teamInfo = teamInfo
        self.firstHero = firstHero
        self.secondHero = secondHero
        self.thirdHero = thirdHero