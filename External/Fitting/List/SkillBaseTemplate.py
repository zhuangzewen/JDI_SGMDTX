# External 战法基础模板系统
# 提供快捷的战法创建和继承方法

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import WeaponType
from External.Fitting.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Soul.JDI_Soul import Soul
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *

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
    """基础战法Soul类，提供通用功能"""
    
    def __init__(self, target: Hero, initiator: Hero = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None):
        super().__init__(target, initiator, sourceType, skill, response_time, 
                        duration, effect_type, effect_value, source_soul, battleField)
        self.soul持有列表 = []

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        """通用的失败处理逻辑"""
        if hero != self.initiator:
            return
        
        self._remove_souls_for_target(self.target)
        
        if len(self.soul持有列表) <= 0:
            return
            
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
            # 移除所有匹配的soul（防止重复）
            while soul in self.soul持有列表:
                self.soul持有列表.remove(soul)

class BaseSkill(Skill):
    """基础战法技能类，提供通用功能"""
    
    def __init__(self, hero: Hero, skillName: Fitting_List_Enum):
        super().__init__(hero, skillName)

    def create_soul(self, target: Hero, effect_type: SoulEffectType, 
                   effect_value: float, response_time: SoulResponseTime = SoulResponseTime.内置待响应) -> Soul:
        """创建标准Soul的便捷方法"""
        return Soul(
            target=target,
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=response_time,
            effect_type=effect_type,
            effect_value=effect_value
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
            Log().show_battle_info('    [{}]执行来自【{}】的[{}]效果'.format(
                target.get_武将名称().value, 
                self.get_战法名称().value, 
                effect_name
            ))
        
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

# 预定义的常用战法模板
def get_skill_template(template_type: str, skill_name: Fitting_List_Enum):
    """获取战法模板的工厂方法"""
    templates = {
        '被动_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.被动,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=1.0
        ),
        '主动_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.主动,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=0.4
        ),
        '指挥_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=1.0
        ),
        '追击_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.追击,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=0.5
        )
    }
    return templates.get(template_type)
