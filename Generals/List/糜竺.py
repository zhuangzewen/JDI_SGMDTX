
# HeroInfoKey.武将名称:HeroName.糜竺,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:36,
# HeroInfoKey.武力成长:0.52,
# HeroInfoKey.初始智力:87,
# HeroInfoKey.智力成长:1.80,
# HeroInfoKey.初始统帅:72,
# HeroInfoKey.统帅成长:1.33,
# HeroInfoKey.初始先攻:37,
# HeroInfoKey.先攻成长:1.40,
# HeroInfoKey.自带战法:SkillName.见机行事

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 糜竺_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.糜竺
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 36
        self.武力成长 = 0.52
        self.初始智力 = 87
        self.智力成长 = 1.80
        self.初始统帅 = 72
        self.统帅成长 = 1.33
        self.初始先攻 = 37
        self.先攻成长 = 1.40
        self.自带战法 = Fitting_List_Enum.见机行事
        self.缘分列表 = []  # TODO: 待补充糜竺缘分关系