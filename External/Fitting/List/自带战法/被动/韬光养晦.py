# 战法名称: 韬光养晦
# 战法类型: 被动
# 战法特性: 谋略
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 韬光养晦:
# 自带主动战法发动率提升3%→6%(受智力影响),每个回合开始时使自身造成谋略伤害提升4%→8%,可叠加,持续到战斗结束

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType,
    Fitting_List_Enum, Log, Hero
)
from Calcu.JDI_Calculate import *

class 韬光养晦_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('被动_谋略', Fitting_List_Enum.韬光养晦, 1.0)
        super().__init__(template)
        self.战法描述 = "自带主动战法发动率提升3%→6%(受智力影响),每个回合开始时使自身造成谋略伤害提升4%→8%,可叠加,持续到战斗结束"
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 韬光养晦_soul(BaseSkillSoul):
    def __init__(self, target: Hero, initiator: Hero, skill):
        super().__init__(target, initiator, skill=skill)
        self.response_time = SoulResponseTime.回合开始
        self.damage_boost_stacks = 0

    def response(self, status=SoulResponseTime.回合开始, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.战斗开始:
            self.战斗开始效果(battleField)
        elif status == SoulResponseTime.回合开始:
            self.回合开始效果(battleField)

    def 战斗开始效果(self, battleField):
        # 提升自带主动战法发动率
        发动率提升值 = self.skill.韬光养晦_发动率提升系数()
        发动率soul = self.skill.create_soul(
            target=self.target,
            effect_type=SoulEffectType.主动战法发动率提升,
            effect_value=发动率提升值,
            duration=-1  # 永久效果
        )
        发动率soul.deploy_initial()
        Log().battle_L1(f'[{self.initiator.get_武将名称()}]获得【韬光养晦】效果，主动战法发动率提升{发动率提升值*100:.1f}%')

    def 回合开始效果(self, battleField):
        # 叠加谋略伤害提升
        self.damage_boost_stacks += 1
        伤害提升值 = self.skill.韬光养晦_伤害提升系数()
        叠加伤害提升 = 伤害提升值 * self.damage_boost_stacks

        # 更新或创建伤害提升soul
        existing_soul = next((s for s in self.target.get_响应Soul列表() if s.effect_type == SoulEffectType.谋略伤害提升 and s.skill == self.skill), None)
        if existing_soul:
            existing_soul.effect_value = 叠加伤害提升
        else:
            伤害提升soul = self.skill.create_soul(
                target=self.target,
                effect_type=SoulEffectType.谋略伤害提升,
                effect_value=叠加伤害提升,
                duration=-1  # 永久效果
            )
            伤害提升soul.deploy_initial()
            self.target.get_响应Soul列表().append(伤害提升soul)

        Log().battle_L1(f'[{self.initiator.get_武将名称()}]【韬光养晦】效果叠加{self.damage_boost_stacks}层，谋略伤害提升{叠加伤害提升*100:.1f}%')

class 韬光养晦_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者 = self.get_持有者()
        soul = 韬光养晦_soul(
            target=持有者,
            initiator=持有者,
            skill=self
        )
        持有者.get_持有Soul列表().append(soul)
        持有者.get_响应Soul列表().append(soul)
        return soul

    def 韬光养晦_发动率提升系数(self):
        def 拟合过程数据统计():
            # 初始值为 6.3%

            # 智力 227.35
            # 11.34 %
            # 11.34 % - 6.3% = 0.0504

            # 智力 237.35
            # 11.54 %
            # 11.54 % - 6.3% = 0.0524

            # 智力 247.35
            # 11.75 %
            # 11.75 % - 6.3% = 0.0545

            # 智力 257.35
            # 11.95 %
            # 11.95 % - 6.3% = 0.0565

            # 智力 267.35
            # 12.14 %
            # 12.14 % - 6.3% = 0.0584

            # 智力 277.35
            # 12.34 %
            # 12.34 % - 6.3% = 0.0604

            # 智力 287.35
            # 12.53 %
            # 12.53 % - 6.3% = 0.0623

            # 智力 297.35
            # 12.72 %
            # 12.72 % - 6.3% = 0.0642

            # x = 智力
            # y = 0.0001972619047618951*x+0.005635839285716829

            pass
            


        # 基础3%，受智力影响最高提升至6%
        基础提升 = 0.03
        owner = self.get_持有者()
        智力加成 = owner.get_智力() * 0.0001
        最终提升 = min(基础提升 + 智力加成, 0.06)
        return 最终提升

    def 韬光养晦_伤害提升系数(self):
        # 基础4%，受智力影响最高提升至8%
        基础提升 = 0.04
        owner = self.get_持有者()
        智力加成 = owner.get_智力() * 0.000133
        最终提升 = min(基础提升 + 智力加成, 0.08)
        return 最终提升