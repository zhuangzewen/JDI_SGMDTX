from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 蔡文姬_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.蔡文姬
        self.武将阵营 = Faction.群  # 假设群阵营对应的值为"群"
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0  # 0表示女性
        self.初始武力 = 18
        self.武力成长 = 0.24
        self.初始智力 = 107
        self.智力成长 = 2.29
        self.初始统率 = 94
        self.统率成长 = 1.59
        self.初始先攻 = 87
        self.先攻成长 = 1.92
        self.自带战法 = Fitting_List_Enum.悲愤诗
        self.缘分列表 = [BondsName_Enum.乱世红颜]