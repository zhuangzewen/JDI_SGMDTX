# HeroInfoKey.武将名称:HeroName.蒋钦,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:88,
# HeroInfoKey.武力成长:1.72,
# HeroInfoKey.初始智力:87,
# HeroInfoKey.智力成长:1.68,
# HeroInfoKey.初始统帅:86,
# HeroInfoKey.统帅成长:1.62,
# HeroInfoKey.初始先攻:40,
# HeroInfoKey.先攻成长:1.41,
# HeroInfoKey.自带战法:Fitting_List_Enum.武略江洪

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 蒋钦_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.蒋钦
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 88
        self.武力成长 = 1.72
        self.初始智力 = 87
        self.智力成长 = 1.68
        self.初始统帅 = 86
        self.统帅成长 = 1.62
        self.初始先攻 = 40
        self.先攻成长 = 1.41
        self.自带战法 = Fitting_List_Enum.武略江洪
        self.缘分列表 = []