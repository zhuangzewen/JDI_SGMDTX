from hero_imports import *
from Generals.Enum.Generals_Enum import Faction, WeaponType, HeroInfoKey
from Generals.Enum.GeneralsList_Enum import Generals_Name_Enum
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum

class 田丰_info(HeroInfo):
    def __init__(self):
        super().__init__()
        self.武将名称 = Generals_Name_Enum.田丰
        self.武将阵营 = Faction.群
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 1
        self.初始武力 = 51
        self.初始智力 = 95
        self.初始统帅 = 73
        self.初始先攻 = 76
        self.武力成长 = 0.33
        self.智力成长 = 2.24
        self.统帅成长 = 1.67
        self.先攻成长 = 2.12
        self.自带战法 = Fitting_List_Enum.荐计阻敌
        self.缘分列表 = []
        self.武将分类 = ["辅助", "后排"]