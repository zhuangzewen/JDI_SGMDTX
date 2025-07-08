# 战法名称: 普攻
# 战法类型: 普通
# 战法特性: 攻击
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 普攻:
# 对敌军单体造成100%伤害(受武力或智力影响，取较高的一项)

from JDI_Enum import SkillName, SkillType, SkillFeature, WeaponType
from External.Fitting.JDI_Skill import SkillInfo, Skill
from Generals.JDI_Hero import Hero
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Soul.JDI_Soul import Soul
from Log.JDI_Log import Log



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

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None):
        if status != SoulResponseTime.普攻行动时 or hero != self.target:
            return
        
        from Calcu.JDI_Calculate import 对敌方所有目标生效, 从队列确定受击武将, 计算伤害
        attacked_heroes = 对敌方所有目标生效(self.target, battleField)
        attacked: Hero = 从队列确定受击武将(attacked_heroes)
        attacked_name = attacked.get_武将名称().value
        Log().show_battle_info('  [{}]对[{}]发动普通攻击'.format(self.target.get_武将名称().value, attacked_name))
        value = 计算伤害(battleField, self.target, attacked, SoulDamageType.兵刃, SkillType.普攻, 伤害值= 1)
        damage_soul = Soul(target=attacked,
                            initiator=self.target,
                            sourceType=SoulSourceType.武将战法,
                            skill=self.skill,
                            effect_type=SoulEffectType.损失兵力,
                            effect_value=value,
                            battleField=battleField)
        damage_soul.deploy_initial()

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

        
