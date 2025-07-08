# 战法名称: 普攻
# 战法类型: 普通
# 战法特性: 攻击
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 普攻:
# 对敌军单体造成100%伤害(受武力或智力影响，取较高的一项)

from External.Fitting.JDI_Skill import SkillInfo, Skill
from JDI_Enum import SkillName, SkillType, SkillFeature, WeaponType
from Soul.JDI_Soul import Soul
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Generals.JDI_Hero import Hero

class 普攻_info(SkillInfo):
    def __init__(self):
        self.战法名称 = SkillName.普攻
        self.战法类型 = SkillType.普攻
        self.战法特性 = SkillFeature.普攻
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1
        self.战法响应时机列表 = [SoulResponseTime.普攻行动时]

class 普攻_soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None):
        print(f"响应普攻: ")


class 普攻_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self, battleField=None):
        普攻soul = 普攻_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.不溯源,
            skill=self,
            response_time=SoulResponseTime.普攻行动时,
            duration=-1,
            effect_type=SoulEffectType.普攻,
            effect_value=0,
            source_soul=None,
            battleField=battleField
        )
        持有者and响应者: Hero = self.get_持有者()
        持有者and响应者.get_持有Soul列表().append(普攻soul)
        持有者and响应者.get_响应Soul列表().append(普攻soul)

    def 普攻_伤害系数(self):
        """
        普攻的伤害系数为 1.0
        """
        return 1.0

        
