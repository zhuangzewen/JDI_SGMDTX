from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 姜维_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.姜维
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 101
        self.武力成长 = 2.39
        self.初始智力 = 111
        self.智力成长 = 2.52
        self.初始统率 = 91
        self.统率成长 = 2.01
        self.初始先攻 = 76
        self.先攻成长 = 1.99
        self.自带战法 = Fitting_List_Enum.九伐中原
        self.缘分列表 = [BondsName_Enum.薪火相传]