
from Generals.JDI_Hero import HeroInfo
from Control.Imports.hero_imports import Generals_Name_Enum, Faction, WeaponType, Fitting_List_Enum, BondsName_Enum

class 刘备_info(HeroInfo):
    def __init__(self):
        self.武将名称 = Generals_Name_Enum.刘备
        self.武将阵营 = Faction.蜀
        self.武将兵种 = WeaponType.盾
        self.武将性别 = 1
        self.初始武力 = 80
        self.武力成长 = 1.43
        self.初始智力 = 94
        self.智力成长 = 2.31
        self.初始统率 = 109
        self.统率成长 = 2.12
        self.初始先攻 = 53
        self.先攻成长 = 1.72
        self.自带战法 = Fitting_List_Enum.携民渡江
        self.缘分列表 = [BondsName_Enum.缘系皇思, BondsName_Enum.三分天下, BondsName_Enum.珠联璧合, BondsName_Enum.桃园结义, BondsName_Enum.仁义昭烈]