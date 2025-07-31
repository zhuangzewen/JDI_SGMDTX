from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 甘夫人_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.甘夫人
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 25
        self.武力成长 = 0.29
        self.初始智力 = 102
        self.智力成长 = 1.95
        self.初始统率 = 106
        self.统率成长 = 1.62
        self.初始先攻 = 90
        self.先攻成长 = 1.68
        self.自带战法 = Fitting_List_Enum.皇思淑仁
        self.缘分列表 = [BondsName_Enum.缘系皇思, BondsName_Enum.乱世红颜]
