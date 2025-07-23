# HeroInfoKey.武将名称:HeroName.貂蝉,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:20,
# HeroInfoKey.武力成长:0.41,
# HeroInfoKey.初始智力:104,
# HeroInfoKey.智力成长:2.22,
# HeroInfoKey.初始统帅:97,
# HeroInfoKey.统帅成长:1.75,
# HeroInfoKey.初始先攻:55,
# HeroInfoKey.先攻成长:2.03,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 貂蝉_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.貂蝉
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 0
        self.初始武力 = 20
        self.武力成长 = 0.41
        self.初始智力 = 104
        self.智力成长 = 2.22
        self.初始统帅 = 97
        self.统帅成长 = 1.75
        self.初始先攻 = 55
        self.先攻成长 = 2.03
        self.自带战法 = Fitting_List_Enum.闭月
        self.缘分列表 = []