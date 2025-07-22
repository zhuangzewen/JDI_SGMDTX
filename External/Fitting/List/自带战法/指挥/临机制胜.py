# 战法名称: 临机制胜 (使用模板系统重构版本)
# 战法类型: 指挥
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 临机制胜:
# 战斗中,敌我全体被施加异常状态时,有70%概率触发制胜:立刻对敌军随机两人造成60%谋略伤害。
# 每回合制胜最多触发4次。累积触发4次制胜后,恢复我军全体兵力(治疗率40%,受智力影响)

# 满阶临机制胜:
# 战斗中,敌我全体被施加异常状态时,有70%概率触发制胜:立刻对敌军随机两人造成69%谋略伤害。
# 每回合制胜最多触发4次。累积触发4次制胜后,恢复我军全体兵力(治疗率46%,受智力影响)

from External.Fitting.List.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template
)
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from External.Fitting.Enum.FittingType_Enum import SkillType
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
import random

class 临机制胜_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板
        template = get_skill_template('指挥_谋略', Fitting_List_Enum.临机制胜)
        super().__init__(template)

class 临机制胜_soul(BaseSkillSoul):
    def __init__(self, target, initiator=None, sourceType=SoulSourceType.不溯源, 
                 skill=None, response_time=SoulResponseTime.无响应阶段, duration=-1,
                 effect_type=SoulEffectType.无影响, effect_value=0, source_soul=None, battleField=None):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, 
                        effect_type, effect_value, source_soul, battleField)
        self.临机制胜发动次数 = 0
        self.临机制胜发动总次数 = 0

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.战法布阵开始时:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(
                self.target.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))

        elif status == SoulResponseTime.回合重置阶段:
            self.临机制胜发动次数 = 0

        elif status in [SoulResponseTime.被施加异常时, SoulResponseTime.被施加控制时]:
            if self.临机制胜发动次数 < 4:
                if random.random() > 0.7:
                    Log().show_debug_info('        [{}]发动来自【{}】的[临机制胜-制胜]效果, 但因几率未触发'.format(
                        hero.get_武将名称().value, self.skill.get_战法名称().value))
                    return
                
                self._execute_制胜效果(battleField, hero)

        elif status == SoulResponseTime.被施加异常时 and self.临机制胜发动总次数 >= 4:
            self._execute_治疗效果(battleField)

    def _execute_制胜效果(self, battleField, hero):
        """执行制胜效果的便捷方法"""
        Log().show_battle_info('        [{}]执行来自【{}】的[临机制胜-制胜]效果'.format(
            hero.get_武将名称().value, self.skill.get_战法名称().value))

        self.临机制胜发动次数 += 1
        self.临机制胜发动总次数 += 1

        # 对敌军随机两人造成伤害
        attacked_times = msg_对敌方所有目标生效_number(self.target, battleField, 2)
        attacked_heroes = 对敌方所有目标生效(self.target, battleField)
        
        for _ in range(attacked_times):
            if len(attacked_heroes) == 0:
                break

            attacked = 从队列确定受击武将(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            damage_soul = self.skill.create_damage_soul(
                battleField, self.target, attacked,
                SoulDamageType.谋略, SkillType.指挥,
                self.skill.临机制胜_伤害系数(), self
            )
            damage_soul.deploy_initial()

    def _execute_治疗效果(self, battleField):
        """执行治疗效果的便捷方法"""
        Log().show_battle_info('        [{}]执行来自【{}】的[临机制胜-治疗]效果'.format(
            self.target.get_武将名称().value, self.skill.get_战法名称().value))

        treatment_times = msg_对己方所有目标生效_number(self.target, battleField)
        treatment_heroes = 对己方所有目标生效(self.target, battleField)
        
        for _ in range(treatment_times):
            if len(treatment_heroes) == 0:
                break

            treatment = 从队列确定受击武将(treatment_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            treatmentValue = 治疗计算(battleField, self.target, treatment, self.skill.临机制胜_治疗系数())

            treatment_soul = self.skill.create_soul(
                treatment, SoulEffectType.恢复兵力, treatmentValue
            )
            treatment_soul.source_soul = self
            treatment_soul.battleField = battleField
            treatment_soul.deploy_initial()

class 临机制胜_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        # 使用基类的便捷方法创建Soul
        soul = 临机制胜_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            sourceType=SoulSourceType.武将战法, 
            skill=self, 
            response_time=SoulResponseTime.内置待响应, 
            effect_type=SoulEffectType.无影响
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    # 使用基类的便捷方法简化数值计算
    def 临机制胜_伤害系数(self):
        return self.get_rank_bonus(0.6, 0.014)
    
    def 临机制胜_治疗系数(self):
        return self.get_rank_bonus(0.4, 0.012)
