# HeroInfoKey.武将名称:HeroName.丁奉,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.兵刃,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:81,
# HeroInfoKey.武力成长:1.65,
# HeroInfoKey.初始智力:84,
# HeroInfoKey.智力成长:0.80,
# HeroInfoKey.初始统帅:88,
# HeroInfoKey.统帅成长:1.35,
# HeroInfoKey.初始先攻:51,
# HeroInfoKey.先攻成长:1.37,
# HeroInfoKey.自带战法:Fitting_List_Enum.奋勇当先

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 丁奉_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.丁奉
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 81
        self.武力成长 = 1.65
        self.初始智力 = 84
        self.智力成长 = 0.80
        self.初始统帅 = 88
        self.统帅成长 = 1.35
        self.初始先攻 = 51
        self.先攻成长 = 1.37
        self.自带战法 = Fitting_List_Enum.奋勇当先
        self.缘分列表 = []