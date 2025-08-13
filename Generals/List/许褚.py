from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 许褚_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.许褚
        self.武将阵营 = Faction.魏
        self.武将兵种 = WeaponType.枪
        self.武将性别 = 1
        self.初始武力 = 114
        self.武力成长 = 2.75
        self.初始智力 = 45
        self.智力成长 = 0.43
        self.初始统率 = 95
        self.统率成长 = 1.64
        self.初始先攻 = 69
        self.先攻成长 = 2.6
        self.自带战法 = Fitting_List_Enum.裸衣血战
        self.缘分列表 = [BondsName_Enum.虎卫御侮, BondsName_Enum.夺射锦袍]