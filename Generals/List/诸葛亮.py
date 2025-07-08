
# HeroInfoKey.武将名称:HeroName.诸葛亮,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:50,
# HeroInfoKey.武力成长:0.52,
# HeroInfoKey.初始智力:125,
# HeroInfoKey.智力成长:3.00,
# HeroInfoKey.初始统帅:111,
# HeroInfoKey.统帅成长:2.30,
# HeroInfoKey.初始先攻:57,
# HeroInfoKey.先攻成长:1.65,
# HeroInfoKey.自带战法:SkillName.草船借箭

from Generals.JDI_Hero import HeroInfo
from Generals.Enum.Generals_List_Enum import Generals_Name_Enum
from JDI_Enum import Faction, WeaponType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum

class 诸葛亮_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.诸葛亮
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 50
        self.武力成长 = 0.52
        self.初始智力 = 125
        self.智力成长 = 3.00
        self.初始统帅 = 111
        self.统帅成长 = 2.30
        self.初始先攻 = 57
        self.先攻成长 = 1.65
        self.自带战法 = Fitting_List_Enum.草船借箭
