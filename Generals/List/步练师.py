# HeroInfoKey.武将名称:HeroName.步练师,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:40,
# HeroInfoKey.武力成长:1.1,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:2.2,
# HeroInfoKey.初始统帅:78,
# HeroInfoKey.统帅成长:1.9,
# HeroInfoKey.初始先攻:68,
# HeroInfoKey.先攻成长:1.5,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 步练师_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.步练师
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 40
        self.武力成长 = 1.1
        self.初始智力 = 85
        self.智力成长 = 2.2
        self.初始统帅 = 78
        self.统帅成长 = 1.9
        self.初始先攻 = 68
        self.先攻成长 = 1.5
        self.缘分列表 = []
