
# HeroInfoKey.武将名称:Generals_Name_Enum.赵云,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.骑,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:117,
# HeroInfoKey.武力成长:2.65,
# HeroInfoKey.初始智力:77,
# HeroInfoKey.智力成长:1.52,
# HeroInfoKey.初始统帅:107,
# HeroInfoKey.统帅成长:2.15,
# HeroInfoKey.初始先攻:66,
# HeroInfoKey.先攻成长:2.29,
# HeroInfoKey.自带战法:Fitting_List_Enum.七进七出

from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum

class 赵云_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.赵云
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        self.初始武力 = 117
        self.武力成长 = 2.65
        self.初始智力 = 77
        self.智力成长 = 1.52
        self.初始统帅 = 107
        self.统帅成长 = 2.15
        self.初始先攻 = 66
        self.先攻成长 = 2.29
        self.自带战法 = Fitting_List_Enum.七进七出