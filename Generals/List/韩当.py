# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:96,
# HeroInfoKey.武力成长:1.86,
# HeroInfoKey.初始智力:71,
# HeroInfoKey.智力成长:0.86,
# HeroInfoKey.初始统帅:85,
# HeroInfoKey.统帅成长:1.35,
# HeroInfoKey.初始先攻:53,
# HeroInfoKey.先攻成长:1.72,
# HeroInfoKey.自带战法:Fitting_List_Enum.猿臂善射

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 韩当_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.韩当
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 96
        self.武力成长 = 1.86
        self.初始智力 = 71
        self.智力成长 = 0.86
        self.初始统帅 = 85
        self.统帅成长 = 1.35
        self.初始先攻 = 53
        self.先攻成长 = 1.72
        self.自带战法 = Fitting_List_Enum.猿臂善射
        self.缘分列表 = []