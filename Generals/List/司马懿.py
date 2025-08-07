from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 司马懿_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.司马懿
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 69
        self.武力成长 = 0.34
        self.初始智力 = 119
        self.智力成长 = 2.8
        self.初始统率 = 114
        self.统率成长 = 2.11
        self.初始先攻 = 47
        self.先攻成长 = 1.54
        self.自带战法 = Fitting_List_Enum.临机制胜
        self.缘分列表 = [BondsName_Enum.国之栋梁, BondsName_Enum.枭鸾同谋]  # 国之栋梁和泉商同谋未在BondsName_Enum中找到
