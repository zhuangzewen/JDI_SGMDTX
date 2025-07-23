# HeroInfoKey.武将名称:HeroName.董袭,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:85,
# HeroInfoKey.武力成长:1.55,
# HeroInfoKey.初始智力:56,
# HeroInfoKey.智力成长:0.87,
# HeroInfoKey.初始统帅:88,
# HeroInfoKey.统帅成长:1.70,
# HeroInfoKey.初始先攻:58,
# HeroInfoKey.先攻成长:1.43,
# HeroInfoKey.自带战法:Fitting_List_Enum.飞身断虹

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 董袭_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.董袭
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 85
        self.武力成长 = 1.55
        self.初始智力 = 56
        self.智力成长 = 0.87
        self.初始统帅 = 88
        self.统帅成长 = 1.70
        self.初始先攻 = 58
        self.先攻成长 = 1.43
        self.自带战法 = Fitting_List_Enum.飞身断虹
        self.缘分列表 = []