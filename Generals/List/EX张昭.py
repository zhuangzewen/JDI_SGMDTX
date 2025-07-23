# HeroInfoKey.武将名称:HeroName.EX张昭,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:16,
# HeroInfoKey.武力成长:0.23,
# HeroInfoKey.初始智力:103,
# HeroInfoKey.智力成长:2.30,
# HeroInfoKey.初始统帅:83,
# HeroInfoKey.统帅成长:1.65,
# HeroInfoKey.初始先攻:87,
# HeroInfoKey.先攻成长:1.79,
# HeroInfoKey.自带战法:Fitting_List_Enum.直谏固政

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX张昭_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX张昭
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 16
        self.武力成长 = 0.23
        self.初始智力 = 103
        self.智力成长 = 2.30
        self.初始统帅 = 83
        self.统帅成长 = 1.65
        self.初始先攻 = 87
        self.先攻成长 = 1.79
        self.自带战法 = Fitting_List_Enum.直谏固政
        self.缘分列表 = []