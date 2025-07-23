# HeroInfoKey.武将名称:HeroName.张飞,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:112,
# HeroInfoKey.武力成长:2.70,
# HeroInfoKey.初始智力:75,
# HeroInfoKey.智力成长:1.20,
# HeroInfoKey.初始统帅:90,
# HeroInfoKey.统帅成长:1.80,
# HeroInfoKey.初始先攻:65,
# HeroInfoKey.先攻成长:1.50,
# HeroInfoKey.自带战法:SkillName.咆哮

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 张飞_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.张飞
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 112
        self.武力成长 = 2.70
        self.初始智力 = 75
        self.智力成长 = 1.20
        self.初始统帅 = 90
        self.统帅成长 = 1.80
        self.初始先攻 = 65
        self.先攻成长 = 1.50
        self.自带战法 = Fitting_List_Enum.咆哮
        self.缘分列表 = [Fitting_List_Enum.桃园结义]
