# HeroInfoKey.武将名称:HeroName.于禁,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:88,
# HeroInfoKey.武力成长:1.50,
# HeroInfoKey.初始智力:70,
# HeroInfoKey.智力成长:0.79,
# HeroInfoKey.初始统帅:102,
# HeroInfoKey.统帅成长:2.05,
# HeroInfoKey.初始先攻:44,
# HeroInfoKey.先攻成长:1.50,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 于禁_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.于禁
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 88
        self.武力成长 = 1.50
        self.初始智力 = 70
        self.智力成长 = 0.79
        self.初始统帅 = 102
        self.统帅成长 = 2.05
        self.初始先攻 = 44
        self.先攻成长 = 1.50
        self.缘分列表 = []
        self.自带战法 = Fitting_List_Enum.持军毅重