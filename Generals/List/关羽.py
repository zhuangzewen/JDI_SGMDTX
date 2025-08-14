from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 关羽_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.关羽
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.骑
        self.武将性别 = 1
        
        # 初始属性
        self.初始武力 = 120
        self.初始智力 = 86
        self.初始统率 = 104
        self.初始先攻 = 79
        
        # 成长属性
        self.武力成长 = 2.75
        self.智力成长 = 1.35
        self.统率成长 = 2.13
        self.先攻成长 = 2.43
        
        # 战法
        self.自带战法 = Fitting_List_Enum.威震华夏
        
        # 缘分
        self.缘分列表 = [BondsName_Enum.义薄云天, BondsName_Enum.桃园结义, BondsName_Enum.五虎上将]