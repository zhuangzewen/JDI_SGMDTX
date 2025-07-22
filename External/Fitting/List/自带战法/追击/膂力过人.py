
# 战法名称: 膂力过人
# 战法类型: 追击
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 膂力过人:
# 普通攻击后,对当前攻击目标造成150%兵刃伤害,若目标武力低于自身额外造成70%兵刃伤害

# 满阶膂力过人:
# 普通攻击后,对当前攻击目标造成172.5%兵刃伤害,若目标武力低于自身额外造成90.5%兵刃伤害

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
from Log.JDI_Log import Log
from Calcu.JDI_Calculate import *

class 膂力过人_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.膂力过人
        self.战法类型 = SkillType.追击
        self.战法特性 = SkillFeature.兵刃
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 膂力过人_soul(Soul):
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
        self.soul持有列表 = []

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        
        if hero != self.initiator:
            return
        
        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.target == self.target:
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

        if self.soul持有列表.__len__() <= 0:
            return

        soul_to_remove = []
        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                soul.restore_initial()
                soul_to_remove.append(soul)

        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)
                if soul in self.soul持有列表:
                    self.soul持有列表.remove(soul)

        msg_移除响应(self)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return
        
        if status == SoulResponseTime.追击行动时 and self.target == hero:
            Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
            attacked_hero = sourceSoul.target
            damage_class: Damage = 计算伤害(battleField, 
                                        self.target, 
                                        attacked_hero, 
                                        SoulDamageType.兵刃, 
                                        SkillType.追击, 
                                        self.skill.膂力过人_伤害系数())
            damage_soul = Soul(target=attacked_hero,
                                initiator=self.target,
                                sourceType=SoulSourceType.武将战法,
                                skill=self.skill,
                                effect_type=SoulEffectType.损失兵力,
                                effect_value=damage_class.damage_value,
                                source_soul=self,
                                battleField=battleField,
                                damage=damage_class)
            damage_soul.deploy_initial()

            if attacked_hero.get_武力() < self.target.get_武力():

                extra_damage_class: Damage = 计算伤害(battleField,
                                                self.target,
                                                attacked_hero,
                                                SoulDamageType.兵刃,
                                                SkillType.追击,
                                                self.skill.膂力过人_额外伤害系数())
                extra_damage_class.skillEffectName = "膂力过人"
                Log().show_battle_info('    [{}]执行来自【{}】的[{}]效果'.format(attacked_hero.get_武将名称().value, self.skill.get_战法名称().value, extra_damage_class.skillEffectName))

                extra_damage_soul = Soul(target=attacked_hero,
                                        initiator=self.target,
                                        sourceType=SoulSourceType.武将战法,
                                        skill=self.skill,
                                        effect_type=SoulEffectType.损失兵力,
                                        effect_value=extra_damage_class.damage_value,
                                        source_soul=self,
                                        battleField=battleField,
                                        damage=extra_damage_class)
                extra_damage_soul.deploy_initial()

class 膂力过人_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者:Hero = self.get_持有者()
        膂力过人soul = 膂力过人_soul(target=持有者and响应者, 
                             initiator=持有者and响应者, 
                             sourceType=SoulSourceType.武将战法, 
                             skill=self, 
                             response_time=SoulResponseTime.内置待响应, 
                             effect_type=SoulEffectType.无影响)
        持有者and响应者.get_持有Soul列表().append(膂力过人soul)
        持有者and响应者.get_响应Soul列表().append(膂力过人soul)

    def 膂力过人_伤害系数(self):
        rankUp = self.get_战法升阶()
        value = 1.5 + rankUp * 0.045
        return value
    
    def 膂力过人_额外伤害系数(self):
        rankUp = self.get_战法升阶()
        value = 0.7 + rankUp * 0.021
        return value