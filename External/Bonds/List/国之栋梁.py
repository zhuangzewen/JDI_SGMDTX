# 战法名称: 国之栋梁
# 战法类型: 缘分

# 国之栋梁:
# 司马懿、诸葛亮、SP诸葛亮、周瑜
# 缘分关系3人在同一队伍时激活效果
# 战斗中造成的前3次谋略伤害提升50%

from External.Bonds.BondUtils import (
    BondUtils, Hero, SkillInfo, Skill, SkillType,
    SoulResponseTime, SoulSourceType, SoulEffectType, Soul, Generals_Name_Enum, BondsName_Enum, Log
)
from Soul.Class.Damage_Class import Damage
from Soul.Enum.SoulDamageType_Enum import SoulDamageType

class 国之栋梁_info(SkillInfo):
    def __init__(self):
        self.战法名称 = BondsName_Enum.国之栋梁
        self.战法类型 = SkillType.缘分
        self.缘分武将 = [
            Generals_Name_Enum.司马懿,
            Generals_Name_Enum.诸葛亮,
            Generals_Name_Enum.诸葛亮SP,
            Generals_Name_Enum.周瑜
        ]
        self.缘分武将生效数量 = 3
        
class 国之栋梁_谋略伤害soul(Soul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 skill: Skill = None, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None):
        super().__init__(target, initiator, skill=skill, effect_type=effect_type, effect_value=effect_value, source_soul=source_soul)
        self.attack_damage = 0

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        if status == SoulResponseTime.造成伤害时:
            damage:Damage = sourceSoul.damage
            if damage.type == SoulDamageType.谋略:
                self.attack_damage += 1
                if self.attack_damage >= 3:
                    self.attack_damage = 0
                    self.restore_initial()

    def _restore_and_remove_initiator_souls(self):
        """恢复并移除发起者的souls"""
        souls_to_process = [soul for soul in self.soul持有列表 if soul.initiator == self.target]
        
        for soul in souls_to_process:
            soul.restore_initial()
            # 移除所有匹配的soul（防止重复）
            while soul in self.soul持有列表:
                self.soul持有列表.remove(soul)



class 国之栋梁_soul(Soul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill=skill)


    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):
        def 国之栋梁_effect(team, effect_hero_list):
            for effect_hero in effect_hero_list:
                谋略伤害soul = 国之栋梁_谋略伤害soul(
                    target=effect_hero,
                    initiator=self.target,
                    skill=self.skill,
                    effect_type=SoulEffectType.造成谋略伤害提升,
                    effect_value=0.5,
                    source_soul=self,
                )
                谋略伤害soul.deploy_initial()
                effect_hero.get_响应Soul列表().append(谋略伤害soul)

            pass
                    
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battleField,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="国之栋梁",
            effect_callback=国之栋梁_effect
        )

class 国之栋梁_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者:Hero = self.get_持有者()
        国之栋梁soul = 国之栋梁_soul(
                            target=持有者, 
                            initiator=持有者, 
                            skill=self)
        return 国之栋梁soul