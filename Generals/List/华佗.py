# HeroInfoKey.武将名称:HeroName.华佗,
# HeroInfoKey.武将阵营:Faction.汉,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:13,
# HeroInfoKey.武力成长:0.35,
# HeroInfoKey.初始智力:106,
# HeroInfoKey.智力成长:2.35,
# HeroInfoKey.初始统帅:68,
# HeroInfoKey.统帅成长:1.60,
# HeroInfoKey.初始先攻:55,
# HeroInfoKey.先攻成长:1.73,
# HeroInfoKey.自带战法:麻沸散

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 华佗_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.华佗
        self.武将阵营 = Faction.汉
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 13
        self.武力成长 = 0.35
        self.初始智力 = 106
        self.智力成长 = 2.35
        self.初始统帅 = 68
        self.统帅成长 = 1.60
        self.初始先攻 = 55
        self.先攻成长 = 1.73
        self.自带战法 = Fitting_List_Enum.麻沸散
        self.缘分列表 = []
