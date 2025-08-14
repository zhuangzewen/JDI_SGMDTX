from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 黄月英_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.黄月英
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.弓
        self.武将性别 = 0
        
        # 初始属性
        self.初始武力 = 31
        self.初始智力 = 109
        self.初始统率 = 93
        self.初始先攻 = 36
        
        # 成长属性
        self.武力成长 = 0.33
        self.智力成长 = 2.28
        self.统率成长 = 1.62
        self.先攻成长 = 2
        
        # 战法
        self.自带战法 = Fitting_List_Enum.木牛流马
        
        # 缘分
        self.缘分列表 = [BondsName_Enum.才堪相配]