# HeroInfoKey.武将名称:HeroName.孔融,
# HeroInfoKey.武将阵营:Faction.群,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:5,
# HeroInfoKey.武力成长:0.05,
# HeroInfoKey.初始智力:98,
# HeroInfoKey.智力成长:1.76,
# HeroInfoKey.初始统帅:71,
# HeroInfoKey.统帅成长:1.33,
# HeroInfoKey.初始先攻:38,
# HeroInfoKey.先攻成长:1.34,
# HeroInfoKey.自带战法:SkillName.言辞激烈

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 孔融_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.孔融
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 5
        self.武力成长 = 0.05
        self.初始智力 = 98
        self.智力成长 = 1.76
        self.初始统帅 = 71
        self.统帅成长 = 1.33
        self.初始先攻 = 38
        self.先攻成长 = 1.34
        self.自带战法 = Fitting_List_Enum.言辞激烈
        self.缘分列表 = []