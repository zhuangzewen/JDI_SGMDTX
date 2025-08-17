
# 战法名称: 七进七出
# 战法类型: 被动
# 战法特性: 兵刃
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 七进七出:
# 提升自身35%规避率，成功规避后触发龙胆
# 龙胆:立刻对敌军随机两人造成90%兵刃伤害,当前回合下一次龙胆的伤害系数降低10%。龙胆每个回合可触发7次

from Soul.JDI_Soul import (BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template, SoulResponseTime, SoulSourceType, SoulEffectType, SoulDamageType, SkillType, Fitting_List_Enum, Log, random, Hero, Soul, Skill)
from Calcu.JDI_Calculate import *

class 七进七出_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('被动_兵刃', Fitting_List_Enum.七进七出)
        super().__init__(template)

class 七进七出_soul(BaseSkillSoul):
    def __init__(self, target: Hero, initiator: Hero, skill: Skill):
        super().__init__(target, initiator, skill=skill)
        self.龙胆触发次数 = 0
        self.当前伤害系数 = 0.9

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.战法布阵开始时:
            self._部署规避效果()
        elif status == SoulResponseTime.回合重置阶段:
            self.龙胆触发次数 = 0
            self.当前伤害系数 = 0
        elif status == SoulResponseTime.规避伤害时:
            if hero != self.target or self.龙胆触发次数 >=7:
                return
            self._触发龙胆效果(battleField)

    def _部署规避效果(self):
        Log().battle_L1('[{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
        规避soul: Soul = Soul(
            target=self.target,
            initiator=self.target,
            sourceType=SoulSourceType.武将战法,
            skill=self.skill,
            effect_type=SoulEffectType.规避,
            effect_value=self.skill.七进七出_规避率提升系数()
        )
        规避soul.deploy_initial()

    def _触发龙胆效果(self, battleField):
        Log().battle_L2('[{}]执行来自【{}】的[七进七出-龙胆]效果'.format(
            self.target.get_武将名称().value, self.skill.get_战法名称().value))

        self.当前伤害系数 = self.skill.七进七出_龙胆伤害系数() - self.龙胆触发次数 * self.skill.七进七出_龙胆伤害降低系数()
        self.龙胆触发次数 += 1       

        attacked_heroes = 对敌方所有目标生效(self.target, battleField)
        attacked_times = min(len(attacked_heroes), 2)
        for i in range(attacked_times):
            attacked = 从队列确定受击单位(attacked_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            damage_soul = self.skill.create_damage_soul(
                battleField = battleField,
                target = attacked,
                initiator = self.target,
                damage_type = SoulDamageType.兵刃,
                skill_type = SkillType.被动,
                damage_multiplier = self.当前伤害系数,
                source_soul = self,
                effect_name="七进七出-龙胆",
                isShowLog=False
            )
            damage_soul.deploy_initial()

class 七进七出_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者 = self.get_持有者()
        soul = 七进七出_soul(target=持有者, initiator=持有者, skill=self)
        持有者.get_持有Soul列表().append(soul)
        持有者.get_响应Soul列表().append(soul)

    def 七进七出_规避率提升系数(self):
        return self.get_rank_bonus(0.35, 0.0105)

    def 七进七出_龙胆伤害系数(self):
        return self.get_rank_bonus(0.9, 0.027)

    def 七进七出_龙胆伤害降低系数(self):
        return self.get_rank_bonus(0.1, 0.003)