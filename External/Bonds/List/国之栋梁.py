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
        
class 国之栋梁_soul(Soul):
    def __init__(self, target, initiator, skill):
        super().__init__(target, initiator, skill)
        # 初始化伤害计数器
        self.damage_count = {}
        for general in self.skill.get_战法信息().缘分武将:
            self.damage_count[general] = 0

    def response(self, status = SoulResponseTime.无响应阶段, battlefield=None, hero = None, sourceSoul=None):
        def 国之栋梁_effect(team, effect_hero_list):
            # 初始化缘分武将的伤害计数器
            for effect_hero in effect_hero_list:
                general_name = effect_hero.get_武将名称()
                if general_name in self.skill.get_战法信息().缘分武将:
                    self.damage_count[general_name] = 0
                    
        # 使用统一的缘分响应处理
        BondUtils.standard_bond_response(
            soul=self,
            status=status,
            battlefield=battlefield,
            hero=hero,
            sourceSoul=sourceSoul,
            bond_name="国之栋梁",
            effect_callback=国之栋梁_effect
        )

    def on_damage_dealt(self, damage_model, battlefield=None):
        # 当造成伤害时触发
        attacker = damage_model.attacker
        damage_type = damage_model.damage_type
        general_name = attacker.get_武将名称()

        # 检查是否是缘分武将且造成的是谋略伤害
        if general_name in self.skill.get_战法信息().缘分武将 and damage_type == SoulDamageType.谋略 and self.damage_count[general_name] < 3:
            # 增加伤害计数
            self.damage_count[general_name] += 1
            
            # 为缘分武将添加谋略伤害提升效果
            谋略伤害提升soul = Soul(
                target=attacker,
                initiator=self.target,
                skill=self.skill,
                effect_type=SoulEffectType.造成谋略伤害提升,
                effect_value= 0.5,  # 提升50%
                source_soul=self,
                battlefield=battlefield,
                duration=1  # 持续1次行动
            )
            谋略伤害提升soul.deploy_initial()
            
            # 记录已触发次数
            if self.damage_count[general_name] == 3:
                # 达到最大触发次数后，输出日志
                Log().battle_L1('[{}]已达到【国之栋梁】最大触发次数'.format(general_name.value))


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