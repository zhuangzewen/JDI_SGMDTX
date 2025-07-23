# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:91,
# HeroInfoKey.武力成长:2.01,
# HeroInfoKey.初始智力:30,
# HeroInfoKey.智力成长:0.26,
# HeroInfoKey.初始统帅:77,
# HeroInfoKey.统帅成长:1.39,
# HeroInfoKey.初始先攻:78,
# HeroInfoKey.先攻成长:1.83,
# HeroInfoKey.自带战法:Fitting_List_Enum.五溪蛮力

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 沙摩柯_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.沙摩柯
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 91
        self.武力成长 = 2.01
        self.初始智力 = 30
        self.智力成长 = 0.26
        self.初始统帅 = 77
        self.统帅成长 = 1.39
        self.初始先攻 = 78
        self.先攻成长 = 1.83
        self.自带战法 = Fitting_List_Enum.五溪蛮力
        self.缘分列表 = []