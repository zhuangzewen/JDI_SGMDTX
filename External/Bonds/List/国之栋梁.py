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
from BattleField.Team.JDI_Team import Team
from Calcu.JDI_Calculate import 获取武将所在的队伍

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
                 initiaTeam: Team = None, 
                 skill: Skill = None, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None):
        super().__init__(target, initiator, initiaTeam=initiaTeam, skill=skill, effect_type=effect_type, effect_value=effect_value, source_soul=source_soul)
        self.attack_damage = 0

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero = None, sourceSoul=None):

        # 队伍中的缘分武将 各持有一个独立的 国之栋梁_谋略伤害soul
        # 当 attack_damage 总和等于 3 时 全部 restore_initial
        if status == SoulResponseTime.造成伤害时 and hero == self.target:
            
            damage:Damage = sourceSoul.damage
            if damage.type == SoulDamageType.谋略:
                self.source_soul.commond_attack_damage += 1

            from Calcu.JDI_Calculate import 获取武将所在的队伍
            if self.source_soul.commond_attack_damage >= 3:
                
                所在队伍 = 获取武将所在的队伍(self.target, battleField)
                for 队伍Hero in [所在队伍.firstHero, 所在队伍.secondHero, 所在队伍.thirdHero]:
                    soulList = 队伍Hero.get_响应Soul列表()
                    for soulDetail in soulList:
                        if soulDetail.source_soul == self.source_soul:
                            Log().battle_L1('[{}]的[国之栋梁]效果已消失'.format(self.target.get_武将名称().value))
                            soulDetail.restore_initial()
                            队伍Hero.get_响应Soul列表().remove(soulDetail)

class 国之栋梁_soul(Soul):

    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill=skill)
        self.commond_attack_damage = 0

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