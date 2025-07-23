# HeroInfoKey.武将名称:HeroName.关羽,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:115,
# HeroInfoKey.武力成长:2.85,
# HeroInfoKey.初始智力:85,
# HeroInfoKey.智力成长:1.50,
# HeroInfoKey.初始统帅:95,
# HeroInfoKey.统帅成长:2.00,
# HeroInfoKey.初始先攻:70,
# HeroInfoKey.先攻成长:1.70,
# HeroInfoKey.自带战法:SkillName.武圣

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 关羽_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.关羽
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 115
        self.武力成长 = 2.85
        self.初始智力 = 85
        self.智力成长 = 1.50
        self.初始统帅 = 95
        self.统帅成长 = 2.00
        self.初始先攻 = 70
        self.先攻成长 = 1.70
        self.自带战法 = Fitting_List_Enum.武圣
        self.缘分列表 = [Fitting_List_Enum.桃园结义]
