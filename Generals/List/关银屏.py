from hero_imports import *

class 关银屏_info(HeroInfo):
    def __init__(self):
        super().__init__()
        self.武将名称 = Generals_Name_Enum.关银屏
        self.阵营 = 阵营.蜀
        self.兵种 = 兵种.骑
        self.性别 = 性别.女
        
        # 初始属性
        self.初始武力 = 108
        self.初始智力 = 60
        self.初始统帅 = 89
        self.初始先攻 = 86
        
        # 成长属性
        self.成长武力 = 2.55
        self.成长智力 = 0.99
        self.成长统帅 = 1.78
        self.成长先攻 = 2.36
        
        # 自带战法
        self.自带战法 = Fitting_List_Enum.虎啸生威
        
        # 缘分列表
        self.缘分列表 = [BondsName_Enum.义薄云天]
        
        # 武将分类
        self.武将分类 = [武将分类.兵刃, 武将分类.后排]