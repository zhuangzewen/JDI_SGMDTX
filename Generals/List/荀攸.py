
# HeroInfoKey.武将名称:HeroName.荀攸,
# HeroInfoKey.武将阵营:Faction.魏,
# HeroInfoKey.武将兵种:WeaponType.弓,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:41,
# HeroInfoKey.武力成长:0.59,
# HeroInfoKey.初始智力:114,
# HeroInfoKey.智力成长:2.45,
# HeroInfoKey.初始统帅:87,
# HeroInfoKey.统帅成长:1.69,
# HeroInfoKey.初始先攻:59,
# HeroInfoKey.先攻成长:2.15,
# HeroInfoKey.自带战法:SkillName.十二奇策

from Generals.JDI_Hero import HeroInfo
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum

class 荀攸_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.荀攸
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 41
        self.武力成长 = 0.59
        self.初始智力 = 114
        self.智力成长 = 2.45
        self.初始统帅 = 87
        self.统帅成长 = 1.69
        self.初始先攻 = 59
        self.先攻成长 = 2.15
        self.自带战法 = Fitting_List_Enum.十二奇策

