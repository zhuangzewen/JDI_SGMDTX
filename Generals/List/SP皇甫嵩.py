# HeroInfoKey.武将名称:HeroName.SP皇甫嵩,
# HeroInfoKey.武将阵营:Faction.汉,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:85,
# HeroInfoKey.武力成长:1.50,
# HeroInfoKey.初始智力:95,
# HeroInfoKey.智力成长:2.20,
# HeroInfoKey.初始统帅:105,
# HeroInfoKey.统帅成长:2.40,
# HeroInfoKey.初始先攻:60,
# HeroInfoKey.先攻成长:1.80,
# HeroInfoKey.自带战法:SkillName.威严制敌

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class SP皇甫嵩_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.SP皇甫嵩
        self.武将阵营 = Faction.汉
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 85
        self.武力成长 = 1.50
        self.初始智力 = 95
        self.智力成长 = 2.20
        self.初始统帅 = 105
        self.统帅成长 = 2.40
        self.初始先攻 = 60
        self.先攻成长 = 1.80
        self.自带战法 = Fitting_List_Enum.威严制敌
        self.缘分列表 = []
