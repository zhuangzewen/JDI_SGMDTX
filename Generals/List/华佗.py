# HeroInfoKey.武将名称:HeroName.华佗,
# HeroInfoKey.武将阵营:Faction.汉,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:60,
# HeroInfoKey.武力成长:0.80,
# HeroInfoKey.初始智力:120,
# HeroInfoKey.智力成长:2.80,
# HeroInfoKey.初始统帅:85,
# HeroInfoKey.统帅成长:1.90,
# HeroInfoKey.初始先攻:70,
# HeroInfoKey.先攻成长:2.00,
# HeroInfoKey.自带战法:SkillName.妙手回春

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 华佗_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.华佗
        self.武将阵营 = Faction.汉
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 60
        self.武力成长 = 0.80
        self.初始智力 = 120
        self.智力成长 = 2.80
        self.初始统帅 = 85
        self.统帅成长 = 1.90
        self.初始先攻 = 70
        self.先攻成长 = 2.00
        self.自带战法 = Fitting_List_Enum.妙手回春
        self.缘分列表 = []
