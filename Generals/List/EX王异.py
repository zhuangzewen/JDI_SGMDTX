# HeroInfoKey.武将名称:HeroName.EX王异,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:17,
# HeroInfoKey.武力成长:0.21,
# HeroInfoKey.初始智力:110,
# HeroInfoKey.智力成长:2.58,
# HeroInfoKey.初始统帅:94,
# HeroInfoKey.统帅成长:1.92,
# HeroInfoKey.初始先攻:86,
# HeroInfoKey.先攻成长:1.76,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX王异_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX王异
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 17
        self.武力成长 = 0.21
        self.初始智力 = 110
        self.智力成长 = 2.58
        self.初始统帅 = 94
        self.统帅成长 = 1.92
        self.初始先攻 = 86
        self.先攻成长 = 1.76
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.巧策引锋