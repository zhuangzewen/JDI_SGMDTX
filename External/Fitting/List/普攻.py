# 战法名称: 普攻
# 战法类型: 普通
# 战法特性: 攻击
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 普攻:
# 对敌军单体造成100%伤害(受武力或智力影响，取较高的一项)

from External.Fitting.JDI_Skill import SkillInfo, Skill
from JDI_Enum import SkillName, SkillType, SkillFeature, WeaponType
from JDI_Enum import ResponseStatus
from JDI_Enum import SkillInfoKey

class 普攻_info(SkillInfo):
    def __init__(self):
        self.战法名称 = SkillName.普攻
        self.战法类型 = SkillType.普攻
        self.战法特性 = SkillFeature.普攻
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1
        self.战法响应时机列表 = [ResponseStatus.普攻行动时]

class 普攻_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def 普攻_伤害系数(self):
        """
        普攻的伤害系数为 1.0
        """
        return 1.0
