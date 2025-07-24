# 战法名称: 战法名称
# 战法类型: 战法类型(指挥/主动/被动/追击)
# 战法特性: 战法特性(谋略/物理/治疗/辅助等)
# 适应兵种: 适应的兵种(盾,弓,枪,骑等)
# 发动率: 发动概率(0-1之间的小数)

# 基础效果描述

# 十级效果描述

# 满阶效果描述（不填写，后续实现时补充）

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType,
    Fitting_List_Enum, Log, random, Hero, Soul, Skill
)
from Calcu.JDI_Calculate import *

class 战法名称_info(BaseSkillInfo):
    def __init__(self):
        # 使用工厂方法获取模板，参数1为战法类型_特性，参数2为战法枚举，参数3位发动率
        template = get_skill_template('战法类型_特性', Fitting_List_Enum.战法枚举名称, 1)
        super().__init__(template)

class 战法名称_soul(BaseSkillSoul):
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero,
                 skill: Skill):
        super().__init__(target, initiator, skill=skill)
        self.soul持有列表 = []

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        # 根据不同的响应阶段执行不同的效果
        # if status == SoulResponseTime.战法布阵开始时:
        #     self._deploy_initial_effect()
        #
        # elif status == SoulResponseTime.回合重置阶段:
        #     self._reset_count()
        #
        # elif status == SoulResponseTime.造成伤害时:
        #     self._on_damage_dealt(battleField)
        #
        # elif status == SoulResponseTime.受到伤害时:
        #     self._on_damage_taken(battleField)
        #
        # elif status == SoulResponseTime.回合结束时:
        #     self._on_turn_end(battleField)

    # 示例：部署初始效果
    def _deploy_initial_effect(self):
        """部署初始效果的便捷方法"""
        Log().battle_L1('[{}]发动战法【{}】'.format(
            self.target.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))
        
        # 创建并部署效果
        # effect_soul = self.skill.create_soul(
        #     self.target, SoulEffectType.效果类型, self.skill.效果系数()
        # )
        # effect_soul.deploy_initial()
        # self.soul持有列表.append(effect_soul)

    # 示例：尝试触发效果
    def _try_trigger_effect(self, battleField):
        """尝试触发效果的便捷方法"""
        # 检查触发条件
        # if random.random() > 触发概率:
        #     Log().debug_L2(f'[{self.target.get_武将名称().value}]发动来自【{self.skill.get_战法名称().value}】的效果, 但因几率未触发')
        #     return
        
        # Log().battle_L2('[{}]执行来自【{}】的效果'.format(
        #     self.target.get_武将名称().value, self.skill.get_战法名称().value))

        # 执行效果逻辑
        # 例如：造成伤害、治疗、施加状态等

class 战法名称_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()
        
        # 使用基类的便捷方法创建Soul
        soul = 战法名称_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )
        
        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)

    # 示例：获取战法系数（随阶数变化）
    def 效果系数(self):
        # 参数1：基础系数，参数2：每阶成长
        return self.get_rank_bonus(基础系数, 每阶成长)