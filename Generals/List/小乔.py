# HeroInfoKey.武将名称:HeroName.小乔,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:0,
# HeroInfoKey.初始武力:32,
# HeroInfoKey.武力成长:0.9,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:2.1,
# HeroInfoKey.初始统帅:68,
# HeroInfoKey.统帅成长:1.5,
# HeroInfoKey.初始先攻:75,
# HeroInfoKey.先攻成长:1.7,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 小乔_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.小乔
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        self.初始武力 = 32
        self.武力成长 = 0.9
        self.初始智力 = 85
        self.智力成长 = 2.1
        self.初始统帅 = 68
        self.统帅成长 = 1.5
        self.初始先攻 = 75
        self.先攻成长 = 1.7
        self.缘分列表 = []