
from JDI_Hero import Hero

class TeamInfo():
    def __init__(self, formation, firstHeroInfo, secondHeroInfo, thirdHeroInfo, teamName='', supply=100):
        self.formation = formation
        self.firstHeroInfo = firstHeroInfo
        self.secondHeroInfo = secondHeroInfo
        self.thirdHeroInfo = thirdHeroInfo
        self.teamName = teamName
        self.supply = supply

class Team():
    def __init__(self, teamInfo: TeamInfo, firstHero: Hero, secondHero: Hero, thirdHero: Hero):
        self.teamInfo = teamInfo
        self.firstHero = firstHero
        self.secondHero = secondHero
        self.thirdHero = thirdHero