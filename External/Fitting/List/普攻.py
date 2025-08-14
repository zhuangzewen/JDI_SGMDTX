# 战法名称: 普攻
# 战法类型: 普通
# 战法特性: 攻击
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 普攻:
# 对敌军单体造成100%兵刃伤害

from Soul.JDI_Soul import (
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
        from External.JDI_Skill import SkillInfo
        SkillInfo.__init__(self, Fitting_List_Enum.普攻)
        self.战法名称 = Fitting_List_Enum.普攻
        self.战法类型 = SkillType.普攻
        self.战法特性 = SkillFeature.普攻
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 普攻_soul(BaseSkillSoul):
    def __init__(self, 
                target, 
                initiator=None, 
                initiaTeam = None,
                sourceType=SoulSourceType.不溯源, 
                sourceDetail=[],
                skill=None, 
                response_time=SoulResponseTime.无响应阶段, 
                duration=-1,
                effect_type=SoulEffectType.无影响, 
                effect_value=0, 
                source_soul=None, 
                battleField=None):
        super().__init__(target, initiator, initiaTeam, sourceType, sourceDetail, skill, response_time, 
                    duration, effect_type, effect_value, source_soul, battleField)
        # 每回合 连击上线次数 1
        # 每回合 反击上线次数 5
        self.连击次数 = 0
        self.反击次数 = 0

        

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        def 对某单位普攻一次(目标单位: Hero = None, 可连击: bool = False, 可追击: bool = False, 可反击: bool = False, battleField=None):
            attacked: Hero = 目标单位
            if attacked == None:
                Log().battle_L1('[{}]没有可攻击对象'.format(self.target.get_武将名称().value))
                return
            from Calcu.JDI_Calculate import 计算伤害
            damage_class: Damage = 计算伤害(battleField, 
                                            self.target, 
                                            attacked, 
                                            SoulDamageType.兵刃, 
                                            SkillType.普攻, 
                                            伤害值= 1)
            damage_detail = []
            if 可反击:
                damage_detail.append(SoulSourceDetail.可反击)
            damage_soul = Soul(target=attacked,
                                initiator=self.target,
                                sourceType=SoulSourceType.武将战法,
                                sourceDetail=damage_detail,
                                skill=self.skill,
                                effect_type=SoulEffectType.损失兵力,
                                effect_value=damage_class.damage_value,
                                source_soul=self,
                                battleField=battleField,
                                damage=damage_class)
            damage_soul.deploy_initial()

            if 可追击:
                from BattleField.JDI_BattleField import BattleField
                battleField: BattleField
                battleField.respond(status=SoulResponseTime.追击行动时, 时机响应武将=self.target, 溯源SOUL=damage_soul)

            from Calcu.JDI_RanVal import 触发连击
            if self.连击次数 < 1 and 可连击 and 触发连击(self.target):
                self.连击次数 += 1
                Log().battle_L1('[{}]进行连击'.format(self.target.get_武将名称().value))
                battleField.respond(status=SoulResponseTime.连击行动时, 时机响应武将=self.target)

        if status == SoulResponseTime.回合重置阶段:
            self.连击次数 = 0
            self.反击次数 = 0

        if (status == SoulResponseTime.普攻行动时 or status == SoulResponseTime.连击行动时) and hero == self.target:

            from Calcu.JDI_Calculate import 对敌方所有目标生效, 从队列确定受击单位
            attacked_heroes = 对敌方所有目标生效(self.target, battleField)
            attacked: Hero = 从队列确定受击单位(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            可连击 = True if status == SoulResponseTime.普攻行动时 else False
            可追击 = True
            可反击 = True
            attacked_name = attacked.get_武将名称().value
            Log().battle_L1('[{}]对[{}]发动普通攻击'.format(self.target.get_武将名称().value, attacked_name))
            对某单位普攻一次(attacked, 可连击, 可追击, 可反击, battleField)

        elif status == SoulResponseTime.受到伤害后 and hero == self.target:
            if SoulSourceDetail.可反击 not in sourceSoul.sourceDetail:
                return
            from Calcu.JDI_Calculate import msg_普攻发起判断
            if not msg_普攻发起判断(self.target):
                Log().battle_L1('[{}]无法普攻(反击)'.format(self.target.get_武将名称().value))
                return
            
            from Calcu.JDI_RanVal import 触发反击
            if  self.反击次数 < 5 and 触发反击(self.target):
                self.反击次数 += 1
                attacked: Hero = sourceSoul.initiator
                可连击 = False
                可追击 = False
                可反击 = True
                Log().battle_L1('[{}]进行反击'.format(self.target.get_武将名称().value))
                对某单位普攻一次(attacked, 可连击, 可追击, 可反击, battleField)

class 普攻_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        普攻soul = 普攻_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self)
        持有者and响应者: Hero = self.get_持有者()
        持有者and响应者.get_持有Soul列表().append(普攻soul)
        持有者and响应者.get_响应Soul列表().append(普攻soul)

    def 普攻_伤害系数(self):
        """
        普攻的伤害系数为 1.0
        """
        return 1.0

        
