
from enum import Enum
from Generals.JDI_Hero import Hero, HeroInfo

class Formation(Enum):
    一字阵 = '一字阵'
    萁型阵 = '萁型阵'
    雁型阵 = '雁型阵'
    方圆阵 = '方圆阵'
    锥型阵 = '锥型阵'
    鱼鳞阵 = '鱼鳞阵'
    钩型阵 = '钩型阵'
    偃月阵 = '偃月阵'

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

class Team():
    def __init__(self, teamInfo: TeamInfo, firstHero: Hero, secondHero: Hero, thirdHero: Hero):
        self.teamInfo = teamInfo
        self.firstHero = firstHero
        self.secondHero = secondHero
        self.thirdHero = thirdHero
        self.重置队伍状态()


    def 重置队伍状态(self):
        self.造成伤害降低 = 0
        self.全队累计治疗量 = 0
        self.缘分soul列表 = []
        self.初始化缘分soul列表()

    def 初始化缘分soul列表(self):

        缘分名称列表 = []
        for hero in self.firstHero, self.secondHero, self.thirdHero:
            hero: Hero
            缘分_list = hero.get_缘分列表()
            for f in 缘分_list:
                if f not in 缘分名称列表:
                    缘分名称列表.append(f)

        for f in 缘分名称列表:
            from External.JDI_Skill import get_skill_info
            缘分info = get_skill_info(f)
            
            # 检查缘分info是否有必要的属性
            if not hasattr(缘分info, '缘分武将') or not hasattr(缘分info, '缘分武将生效数量'):
                continue
                
            缘分武将数量 = 0
            for hero in self.firstHero, self.secondHero, self.thirdHero:
                hero: Hero
                if hero.get_武将名称() in 缘分info.缘分武将:
                    缘分武将数量 += 1

            if 缘分武将数量 >= 缘分info.缘分武将生效数量:
                from External.JDI_Skill import get_skill
                缘分skill = get_skill(f, None)
                创建soul = 缘分skill.fill_init_soul()
                self.缘分soul列表.append(创建soul)
