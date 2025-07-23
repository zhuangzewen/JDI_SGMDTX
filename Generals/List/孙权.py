# HeroInfoKey.武将名称:HeroName.孙权,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:90,
# HeroInfoKey.武力成长:1.91,
# HeroInfoKey.初始智力:96,
# HeroInfoKey.智力成长:2.08,
# HeroInfoKey.初始统帅:101,
# HeroInfoKey.统帅成长:2.09,
# HeroInfoKey.初始先攻:74,
# HeroInfoKey.先攻成长:2.33,
# HeroInfoKey.自带战法:SkillName.虎踞江东

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 孙权_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.孙权
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 90
        self.武力成长 = 1.91
        self.初始智力 = 96
        self.智力成长 = 2.08
        self.初始统帅 = 101
        self.统帅成长 = 2.09
        self.初始先攻 = 74
        self.先攻成长 = 2.33
        self.自带战法 = Fitting_List_Enum.虎踞江东
        self.缘分列表 = [Fitting_List_Enum.三分天下]
