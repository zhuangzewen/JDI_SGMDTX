# HeroInfoKey.武将名称:HeroName.潘璋,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:84,
# HeroInfoKey.武力成长:1.58,
# HeroInfoKey.初始智力:82,
# HeroInfoKey.智力成长:1.05,
# HeroInfoKey.初始统帅:83,
# HeroInfoKey.统帅成长:1.55,
# HeroInfoKey.初始先攻:69,
# HeroInfoKey.先攻成长:1.33,
# HeroInfoKey.自带战法:SkillName.驰军截刃

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 潘璋_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.潘璋
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 84
        self.武力成长 = 1.58
        self.初始智力 = 82
        self.智力成长 = 1.05
        self.初始统帅 = 83
        self.统帅成长 = 1.55
        self.初始先攻 = 69
        self.先攻成长 = 1.33
        self.自带战法 = Fitting_List_Enum.驰军截刃
        self.缘分列表 = []