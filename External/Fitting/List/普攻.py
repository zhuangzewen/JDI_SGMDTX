# 战法名称: 普攻
# 战法类型: 普通
# 战法特性: 攻击
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 普攻:
# 对敌军单体造成100%兵刃伤害

from External.Fitting.List.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, WeaponType, SkillFeature, Hero, Soul
)
from Soul.Class.Damage_Class import Damage
from Calcu.JDI_Calculate import *

class 普攻_info(BaseSkillInfo):
    def __init__(self):
        # 普攻不使用模板，需要特殊处理
        # 先调用SkillInfo的构造函数
        from External.Fitting.JDI_Skill import SkillInfo
        SkillInfo.__init__(self, Fitting_List_Enum.普攻)
        self.战法名称 = Fitting_List_Enum.普攻
        self.战法类型 = SkillType.普攻
        self.战法特性 = SkillFeature.普攻
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 普攻_soul(BaseSkillSoul):
    def __init__(self, target, initiator=None, sourceType=SoulSourceType.不溯源, 
                 skill=None, response_time=SoulResponseTime.无响应阶段, duration=-1,
                 effect_type=SoulEffectType.无影响, effect_value=0, source_soul=None, battleField=None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, 
                        effect_type, effect_value, source_soul, battleField)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if (status == SoulResponseTime.普攻行动时 or status == SoulResponseTime.连击行动时) and hero == self.target:

            from Calcu.JDI_Calculate import msg_普攻发起判断
            if not msg_普攻发起判断(self.target):
                Log().show_battle_info('    [{}]无法普攻'.format(self.target.get_武将名称().value))
                return
        
            from Calcu.JDI_Calculate import 对敌方所有目标生效, 从队列确定受击武将, 计算伤害
            attacked_heroes = 对敌方所有目标生效(self.target, battleField)
            attacked: Hero = 从队列确定受击武将(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            if attacked == None:
                Log().show_battle_info('    [{}]没有可攻击对象'.format(self.target.get_武将名称().value))
                return
            
            attacked_name = attacked.get_武将名称().value
            Log().show_battle_info('    [{}]对[{}]发动普通攻击'.format(self.target.get_武将名称().value, attacked_name))
            damage_class: Damage = 计算伤害(battleField, self.target, attacked, SoulDamageType.兵刃, SkillType.普攻, 伤害值= 1)
            damage_soul = Soul(target=attacked,
                                initiator=self.target,
                                sourceType=SoulSourceType.武将战法,
                                skill=self.skill,
                                effect_type=SoulEffectType.损失兵力,
                                effect_value=damage_class.damage_value,
                                source_soul=self,
                                battleField=battleField,
                                damage=damage_class)
            damage_soul.deploy_initial()

            from BattleField.JDI_BattleField import BattleField
            battleField: BattleField
            battleField.respond(status=SoulResponseTime.追击行动时, 时机响应武将=self.target, 溯源SOUL=damage_soul)

            from Calcu.JDI_RanVal import 触发连击
            if status == SoulResponseTime.普攻行动时 and 触发连击(self.target):
                Log().show_battle_info('    [{}]进行连击'.format(self.target.get_武将名称().value))
                battleField.respond(status=SoulResponseTime.连击行动时, 时机响应武将=self.target)

class 普攻_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        普攻soul = 普攻_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=SoulResponseTime.内置待响应,
            duration=-1,
            effect_type=SoulEffectType.待响应,
            effect_value=0,
            source_soul=None,
            battleField=None)
        持有者and响应者: Hero = self.get_持有者()
        持有者and响应者.get_持有Soul列表().append(普攻soul)
        持有者and响应者.get_响应Soul列表().append(普攻soul)

    def 普攻_伤害系数(self):
        """
        普攻的伤害系数为 1.0
        """
        return 1.0

        
