# HeroInfoKey.武将名称:HeroName.孙策,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.枪,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:108,
# HeroInfoKey.武力成长:2.50,
# HeroInfoKey.初始智力:82,
# HeroInfoKey.智力成长:1.40,
# HeroInfoKey.初始统帅:98,
# HeroInfoKey.统帅成长:2.10,
# HeroInfoKey.初始先攻:85,
# HeroInfoKey.先攻成长:2.30,
# HeroInfoKey.自带战法:SkillName.英魂

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 孙策_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.孙策
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 108
        self.武力成长 = 2.50
        self.初始智力 = 82
        self.智力成长 = 1.40
        self.初始统帅 = 98
        self.统帅成长 = 2.10
        self.初始先攻 = 85
        self.先攻成长 = 2.30
        self.自带战法 = Fitting_List_Enum.英魂
        self.缘分列表 = []
