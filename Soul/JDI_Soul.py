from Control.Log.JDI_Log import Log
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulSourceType_Enum import SoulSourceType, SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from External.JDI_Skill import Skill
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Generals.JDI_Hero import Hero
from Soul.Class.Damage_Class import Damage
from Calcu.JDI_Calculate import msg_移除响应
from BattleField.Team.JDI_Team import Team
import random

class Soul():
    # 目标 发起者 来源类型 技能 响应时机 持续回合 效果类型 效果值
    # 声明传入的类型 而不是any
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 initiaTeam: Team = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 sourceDetail: [SoulSourceDetail] = [], # pyright: ignore[reportInvalidTypeForm]
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None,
                 damage: Damage = None):
        self.target = target                # 目标
        self.initiator = initiator          # 发起者
        self.initiaTeam = initiaTeam        # 发起队伍
        self.sourceType = sourceType        # 来源类型
        self.sourceDetail = sourceDetail    # 来源详情
        self.skill = skill                  # 技能
        self.response_time = response_time  # 响应时机
        self.duration = duration            # 持续回合
        self.effect_type = effect_type      # 效果类型
        self.effect_value = effect_value    # 效果值
        self.source_soul = source_soul      # 来源魂灵
        self.damage = damage                # 伤害类

        if battleField is not None:
            from BattleField.JDI_BattleField import BattleField
            self.battleField = battleField

    def response(self, status: SoulResponseTime=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul = None):
        pass

    def deploy_initial(self):

        self.target: Hero
        # 溃败状态不响应
        if self.initiator is not None and self.initiator.get_被击溃状态():
            return
        if self.target is not None and self.target.get_被击溃状态():
            return
        # 自动分发到分文件方法
        method_name = f"deploy_{self.effect_type.name}_initial"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            if method(self) != False:
                # 状态响应分发
                if SoulSourceDetail.控制状态效果 in self.sourceDetail:
                    self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
                    self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)
                if SoulSourceDetail.异常状态效果 in self.sourceDetail:
                    self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
                    self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)
                if SoulSourceDetail.负面状态效果 in self.sourceDetail:
                    self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                    self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)
                return
        else:
            Log().show_debug_info(f'[DEBUG] {method_name} not found in Soul')

    def restore_initial(self):

        self.target: Hero
        # 溃败状态不响应
        if self.initiator is not None and self.initiator.get_被击溃状态():
            return
        if self.target is not None and self.target.get_被击溃状态():
            return
        # 自动分发到分文件方法
        method_name = f"restore_{self.effect_type.name}_initial"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            if method(self) != False:
                return
        else:
            Log().show_debug_info(f'[DEBUG] {method_name} not found in Soul')


# 战法基础模板系统合并
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import WeaponType
from External.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType, SoulSourceDetail
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
from BattleField.Team.JDI_Team import Team
import random

__all__ = [
    'BaseSkillInfo', 'BaseSkillSoul', 'BaseSkill', 'get_skill_template',
    'SoulResponseTime', 'SoulSourceType', 'SoulSourceDetail', 'SoulEffectType', 'SoulDamageType',
    'SkillType', 'Fitting_List_Enum', 'Log', 'random'
]

class SkillTemplate:
    """战法配置模板类，用于快速创建战法配置"""
    def __init__(self, skill_name: Fitting_List_Enum, skill_type: SkillType, 
                 skill_feature: SkillFeature, weapon_types: List[WeaponType], 
                 trigger_rate: float):
        self.skill_name = skill_name
        self.skill_type = skill_type
        self.skill_feature = skill_feature
        self.weapon_types = weapon_types
        self.trigger_rate = trigger_rate

class BaseSkillInfo(SkillInfo):
    """基础战法信息类，简化继承"""
    def __init__(self, template: SkillTemplate):
        super().__init__(template.skill_name)
        self.战法名称 = template.skill_name
        self.战法类型 = template.skill_type
        self.战法特性 = template.skill_feature
        self.适应兵种 = template.weapon_types
        self.发动率 = template.trigger_rate

class BaseSkillSoul(Soul):
    """基础战法Soul类,提供通用功能"""
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 initiaTeam: Team = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 sourceDetail: List[SoulSourceDetail] = [],
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None,
                 damage: 'Damage' = None):
        super().__init__(target, initiator, initiaTeam, sourceType, sourceDetail, skill, response_time, 
                        duration, effect_type, effect_value, source_soul, battleField, damage)
        self.soul持有列表 = []

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        """通用的失败处理逻辑"""
        if hero != self.initiator:
            return
        self._remove_souls_for_target(hero)
        if self.damage and self.damage.skillEffectName:
            skillEffectName = self.damage.skillEffectName
            Log().battle_L2('[{}]的[{}]效果已消失'.format(self.target.get_武将名称().value, skillEffectName))
        self._restore_and_remove_initiator_souls()
        msg_移除响应(self)

    def _remove_souls_for_target(self, target: Hero):
        """移除目标英雄的souls"""
        soul_to_remove = [soul for soul in self.soul持有列表 if soul.target == target]
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

    def _restore_and_remove_initiator_souls(self):
        """恢复并移除发起者的souls"""
        souls_to_process = [soul for soul in self.soul持有列表 if soul.initiator == self.target]
        for soul in souls_to_process:
            soul.restore_initial()
            while soul in self.soul持有列表:
                self.soul持有列表.remove(soul)

class BaseSkill(Skill):
    """基础战法技能类，提供通用功能"""
    def __init__(self, hero: Hero, skillName: Fitting_List_Enum):
        super().__init__(hero, skillName)

    def create_soul(self, 
                    target: Hero, 
                    effect_type: SoulEffectType, 
                    effect_value: float, 
                    response_time: SoulResponseTime = SoulResponseTime.内置待响应,
                    duration: int = -1,
                    source_soul = None,
                    damage: 'Damage' = None) -> Soul:
        """创建标准Soul的便捷方法"""
        return Soul(
            target=target,
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=response_time,
            duration=duration,
            effect_type=effect_type,
            effect_value=effect_value,
            source_soul=source_soul,
            damage=damage
        )

    def deploy_soul(self, soul: Soul, add_to_list: bool = True):
        """部署Soul的便捷方法"""
        soul.deploy_initial()
        if add_to_list and hasattr(self, 'soul持有列表'):
            self.soul持有列表.append(soul)

    def get_rank_bonus(self, base_value: float, rank_multiplier: float) -> float:
        """根据战法升阶计算加成的便捷方法"""
        rank = self.get_战法升阶()
        return base_value + rank * rank_multiplier

    def create_damage_soul(self, battleField, initiator: Hero, target: Hero, 
                          damage_type: SoulDamageType, skill_type: SkillType, 
                          damage_multiplier: float, source_soul: Soul = None,
                          effect_name: str = None) -> Soul:
        """创建伤害Soul的便捷方法"""
        damage_model = 计算伤害(battleField, initiator, target, damage_type, skill_type, damage_multiplier)
        if effect_name:
            damage_model.skillEffectName = effect_name
        damage_soul = Soul(
            target=target,
            initiator=initiator,
            sourceType=SoulSourceType.武将战法,
            skill=self,
            effect_type=SoulEffectType.损失兵力,
            effect_value=damage_model.damage_value,
            source_soul=source_soul,
            battleField=battleField,
            damage=damage_model
        )
        return damage_soul

def get_skill_template(template_type: str, skill_name: Fitting_List_Enum, trigger_rate: float = None):
    """获取战法模板的工厂方法"""
    default_rates = {
        '被动_兵刃': 1.0,
        '主动_谋略': 1.0,
        '主动_治疗': 1.0,
        '指挥_治疗': 1.0,
        '指挥_谋略': 1.0,
        '指挥_文武': 1.0,
        '指挥_辅助': 1.0,
        '追击_兵刃': 1.0
    }
    final_trigger_rate = trigger_rate if trigger_rate is not None else default_rates.get(template_type, 1.0)
    templates = {
        '被动_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.被动,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '主动_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.主动,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '主动_治疗': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.主动,
            skill_feature=SkillFeature.治疗,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_文武': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.文武,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_辅助': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.辅助,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '追击_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.追击,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_治疗': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.治疗,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
    }
    if template_type not in templates:
        raise ValueError(f"Unknown template type: {template_type}")
    return templates.get(template_type)


# 文件末尾自动注册所有 deploy_*_initial && restore_*_initial 方法到 Soul 类
import types
# 引入 Soul.List 下的所有文件 的所有方法

from Soul.List.造成伤害 import *
from Soul.List.受到伤害 import *
from Soul.List.基础属性 import *
from Soul.List.常规增益 import *
from Soul.List.特殊增益 import *
from Soul.List.特殊负面 import *
from Soul.List.附加属性 import *
from Soul.List.增减兵力 import *

for name, obj in list(globals().items()):
    if name.startswith('deploy_') and name.endswith('_initial') and isinstance(obj, types.FunctionType):
        setattr(Soul, name, staticmethod(obj))
    if name.startswith('restore_') and name.endswith('_initial') and isinstance(obj, types.FunctionType):
        setattr(Soul, name, staticmethod(obj))