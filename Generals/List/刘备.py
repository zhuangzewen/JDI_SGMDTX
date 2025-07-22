
# HeroInfoKey.武将名称:HeroName.刘备,
# HeroInfoKey.武将阵营:Faction.蜀,
# HeroInfoKey.武将兵种:WeaponType.盾,
# HeroInfoKey.武将性别:1,
# HeroInfoKey.初始武力:53,
# HeroInfoKey.武力成长:1.43,
# HeroInfoKey.初始智力:125,
# HeroInfoKey.智力成长:2.31,
# HeroInfoKey.初始统帅:104,
# HeroInfoKey.统帅成长:2.12,
# HeroInfoKey.初始先攻:61,
# HeroInfoKey.先攻成长:1.72,
# HeroInfoKey.自带战法:SkillName.携民渡江

from Generals.JDI_Hero import HeroInfo
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from Generals.Enum.Generals_Enum import Faction, WeaponType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum


class 刘备_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.刘备
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 53
        self.武力成长 = 1.43
        self.初始智力 = 125
        self.智力成长 = 2.31
        self.初始统帅 = 104
        self.统帅成长 = 2.12
        self.初始先攻 = 61
        self.先攻成长 = 1.72
        self.自带战法 = Fitting_List_Enum.携民渡江
        self.缘分列表 = [Fitting_List_Enum.仁义昭烈, Fitting_List_Enum.三分天下, Fitting_List_Enum.桃园结义, Fitting_List_Enum.缘系皇思, Fitting_List_Enum.珠联璧合]
