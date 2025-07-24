# HeroInfoKey.武将名称:HeroName.邓艾,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:94,
# HeroInfoKey.武力成长:1.80,
# HeroInfoKey.初始智力:101,
# HeroInfoKey.智力成长:2.10,
# HeroInfoKey.初始统帅:100,
# HeroInfoKey.统帅成长:1.73,
# HeroInfoKey.初始先攻:66,
# HeroInfoKey.先攻成长:1.75,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 邓艾_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.邓艾
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 94
        self.武力成长 = 1.80
        self.初始智力 = 101
        self.智力成长 = 2.10
        self.初始统帅 = 100
        self.统帅成长 = 1.73
        self.初始先攻 = 66
        self.先攻成长 = 1.75
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.屯田令
