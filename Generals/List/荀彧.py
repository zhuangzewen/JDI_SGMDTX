# HeroInfoKey.武将名称:HeroName.荀彧,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:45,
# HeroInfoKey.武力成长:1.0,
# HeroInfoKey.初始智力:105,
# HeroInfoKey.智力成长:2.6,
# HeroInfoKey.初始统帅:92,
# HeroInfoKey.统帅成长:2.1,
# HeroInfoKey.初始先攻:68,
# HeroInfoKey.先攻成长:1.4,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 荀彧_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.荀彧
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 45
        self.武力成长 = 1.0
        self.初始智力 = 105
        self.智力成长 = 2.6
        self.初始统帅 = 92
        self.统帅成长 = 2.1
        self.初始先攻 = 68
        self.先攻成长 = 1.4
        self.缘分列表 = []