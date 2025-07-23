# HeroInfoKey.武将名称:HeroName.EX皇甫嵩,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:89,
# HeroInfoKey.武力成长:1.83,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:1.96,
# HeroInfoKey.初始统帅:111,
# HeroInfoKey.统帅成长:2.36,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.93,
# HeroInfoKey.自带战法:SkillName.兵动若神

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class EX皇甫嵩_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.EX皇甫嵩
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 89
        self.武力成长 = 1.83
        self.初始智力 = 85
        self.智力成长 = 1.96
        self.初始统帅 = 111
        self.统帅成长 = 2.36
        self.初始先攻 = 65
        self.先攻成长 = 1.93
        self.自带战法 = Fitting_List_Enum.兵动若神
        self.缘分列表 = []
