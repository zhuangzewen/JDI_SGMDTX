# HeroInfoKey.武将名称:HeroName.孙坚,
# HeroInfoKey.武将阵营:Faction.吴,
# HeroInfoKey.武将兵种:WeaponType.刀,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:92,
# HeroInfoKey.武力成长:2.1,
# HeroInfoKey.初始智力:78,
# HeroInfoKey.智力成长:1.7,
# HeroInfoKey.初始统帅:95,
# HeroInfoKey.统帅成长:2.2,
# HeroInfoKey.初始先攻:85,
# HeroInfoKey.先攻成长:1.8,

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 孙坚_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.孙坚
        self.武将阵营 = Faction.吴
        self.武将兵种 = WeaponType.刀
        self.武将性别 = 1
        self.初始武力 = 92
        self.武力成长 = 2.1
        self.初始智力 = 78
        self.智力成长 = 1.7
        self.初始统帅 = 95
        self.统帅成长 = 2.2
        self.初始先攻 = 85
        self.先攻成长 = 1.8
        self.缘分列表 = []