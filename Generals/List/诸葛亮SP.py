
from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 诸葛亮SP_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.诸葛亮SP
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 53
        self.武力成长 = 0.56
        self.初始智力 = 125
        self.智力成长 = 3.00
        self.初始统帅 = 104
        self.统帅成长 = 2.24
        self.初始先攻 = 61
        self.先攻成长 = 1.71
        self.自带战法 = Fitting_List_Enum.星罗棋布
        self.缘分列表 = [BondsName_Enum.西蜀之智, BondsName_Enum.国之栋梁, BondsName_Enum.才堪相配, BondsName_Enum.薪火相传]
