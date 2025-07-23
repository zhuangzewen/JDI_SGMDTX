# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:34,
# HeroInfoKey.武力成长:0.35,
# HeroInfoKey.初始智力:88,
# HeroInfoKey.智力成长:1.85,
# HeroInfoKey.初始统帅:83,
# HeroInfoKey.统帅成长:1.35,
# HeroInfoKey.初始先攻:71,
# HeroInfoKey.先攻成长:1.65,
# HeroInfoKey.自带战法:Fitting_List_Enum.捷对

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 杨修_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.杨修
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 34
        self.武力成长 = 0.35
        self.初始智力 = 88
        self.智力成长 = 1.85
        self.初始统帅 = 83
        self.统帅成长 = 1.35
        self.初始先攻 = 71
        self.先攻成长 = 1.65
        self.自带战法 = Fitting_List_Enum.捷对
        self.缘分列表 = []