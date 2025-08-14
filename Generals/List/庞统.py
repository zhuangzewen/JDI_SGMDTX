from hero_imports import *

class 庞统_info(HeroInfo):
    def __init__(self):
        super().__init__()
        self.武将名称 = Generals_Name_Enum.庞统
        self.阵营 = 阵营.蜀
        self.兵种 = 兵种.弓
        self.性别 = 性别.男
        
        # 初始属性
        self.初始武力 = 54
        self.初始智力 = 116
        self.初始统帅 = 83
        self.初始先攻 = 51
        
        # 成长属性
        self.成长武力 = 0.55
        self.成长智力 = 2.65
        self.成长统帅 = 1.75
        self.成长先攻 = 1.65
        
        # 自带战法
        self.自带战法 = Fitting_List_Enum.连环计
        
        # 缘分列表
        self.缘分列表 = [BondsName_Enum.西蜀之智]