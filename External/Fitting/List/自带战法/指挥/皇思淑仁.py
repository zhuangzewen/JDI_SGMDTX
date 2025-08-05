# 战法名称: 皇思淑仁
# 战法类型: 指挥
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 皇思淑仁:
# 每个回合开始有60%概率(受智力影响)提升我军随机2-3人18%规避率(受智力影响),持续2回合。
# 每个回合结束时恢复我军随机两人兵力(治疗率120%)

# 满阶皇思淑仁:
# 每个回合开始有69%概率(受智力影响)提升我军随机2-3人20.6%规避率(受智力影响),持续2回合。
# 每个回合结束时恢复我军随机两人兵力(治疗率138%)

from External.SkillBaseTemplate import (
    BaseSkillInfo, BaseSkillSoul, BaseSkill, get_skill_template,
    SoulResponseTime, SoulEffectType,
    Fitting_List_Enum, Log, random, Hero, Soul
)
from Calcu.JDI_Calculate import *

class 皇思淑仁_info(BaseSkillInfo):
    def __init__(self):
        template = get_skill_template('指挥_辅助', Fitting_List_Enum.皇思淑仁, 1.0)
        super().__init__(template)

class 皇思淑仁_规避soul(Soul):
    def __init__(self, 
                 target, 
                 initiator=None, 
                 sourceType=None, 
                 sourceDetail=[],
                 skill=None, 
                 response_time=None, 
                 duration=2, 
                 effect_type=SoulEffectType.规避, 
                 effect_value=0,
                 source_soul=None,
                 battleField=None,
                 damage=Damage(skillEffectName="皇思淑仁")):
         super().__init__(target, initiator, sourceType, sourceDetail, skill, response_time, duration, effect_type, effect_value, source_soul, battleField, damage)

    def response(self, status=None, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将回合重置阶段 and hero == self.target:
            hero: Hero = self.target
            self.duration -= 1
            if self.duration < 0:
                self.restore_initial()
                return

class 皇思淑仁_soul(BaseSkillSoul):

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.回合开始时:
            self._deploy_规避率效果(battleField)

        elif status == SoulResponseTime.武将回合重置阶段:
            
            pass

        elif status == SoulResponseTime.回合结束时:
            self._deploy_治疗效果(battleField)
            pass

    def _deploy_规避率效果(self, battleField):

        if random.random() > self.skill.皇思淑仁_发动率():
            Log().debug_L2(f'[{self.target.get_武将名称().value}]发动来自【{self.skill.get_战法名称().value}】的[皇思淑仁]效果, 但因几率未触发')
            return

        Log().battle_L1('[{}]执行来自【{}】的[皇思淑仁]效果'.format(
            self.initiator.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)
        value_times = min(random.randint(2, 3), len(value_heroes))
        
        for _ in range(value_times):
            if len(value_heroes) == 0:
                break

            目标武将: Hero = 从队列确定受击单位(value_heroes, skill=self.skill, hero=self.target, battleField=battleField)

            for 已存在soul in 目标武将.get_响应Soul列表():
                已存在soul: Soul
                if 已存在soul.source_soul == self:
                    已存在soul.duration = 2
                    Log().battle_L2('[{}]的[皇思淑仁]效果已刷新'.format(目标武将.get_武将名称().value))
                    break
            else:
                规避soul = 皇思淑仁_规避soul(
                    target=目标武将,
                    initiator=self.initiator,
                    sourceType=SoulSourceType.武将战法,
                    skill=self.skill,
                    effect_value=self.skill.皇思淑仁_规避率提升系数(),
                    duration=2,
                    source_soul=self,
                    battleField=battleField
                )
                规避soul.deploy_initial()
                self.soul持有列表.append(规避soul)
                目标武将.get_响应Soul列表().append(规避soul)

    def _deploy_治疗效果(self, battleField):
        initiator = self.initiator

        Log().battle_L1('[{}]执行来自【{}】的[皇思淑仁]效果'.format(
            initiator.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        value_heroes = 对己方所有目标生效(self.target, battleField)
        value_times = min(2, len(value_heroes))
        
        for _ in range(value_times):
            if len(value_heroes) == 0:
                break

            目标武将 = 从队列确定受击单位(value_heroes, skill=self.skill, hero=self.target, battleField=battleField)
            治疗soul = self.skill.create_soul(
                target=目标武将,
                effect_type=SoulEffectType.恢复兵力,
                effect_value=治疗计算(battleField, 施救者=self.target, 受助者=目标武将, 治疗率 = self.skill.皇思淑仁_治疗率计算())
            )
            治疗soul.deploy_initial()   

class 皇思淑仁_skill(BaseSkill):

    def fill_init_soul(self):
        持有者and响应者 = self.get_持有者()

        # 使用基类的便捷方法创建Soul
        soul = 皇思淑仁_soul(
            target=持有者and响应者, 
            initiator=持有者and响应者, 
            skill=self
        )

        持有者and响应者.get_持有Soul列表().append(soul)
        持有者and响应者.get_响应Soul列表().append(soul)
        return soul

    def 皇思淑仁_发动率(self):
        # 直接套用韬光的发动率 
        # y = 0.0001972619047618951*x+0.005635839285716829
        基础提升 = self.get_rank_bonus(0.6, 0.018)
        owner = self.get_持有者()
        x = owner.get_智力()
        最终提升 = 0.0001972619047618951*x+0.005635839285716829 + 基础提升
        return 最终提升

    def 皇思淑仁_规避率提升系数(self):
        def 拟合过程数据统计():
            # 初始值为 18%

            # 智力 196.85
            # 规避 24.14%
            # 提升 24.14% - 18% = 0.0614

            # 智力 206.85
            # 规避 24.44%
            # 提升 24.44% - 18% = 0.0644

            # 智力 216.85
            # 规避 24.74%
            # 提升 24.74% - 18% = 0.0674

            # 智力 226.85
            # 规避 25.04%
            # 提升 25.04% - 18% = 0.0704

            # y = 0.00030000000000001136*x+0.002344999999997599
            pass

        基础提升 = self.get_rank_bonus(0.18, 0.0052)
        owner = self.get_持有者()
        x = owner.get_智力()
        最终提升 = 0.0003*x+0.002344999999997599 + 基础提升
        return 最终提升

    def 皇思淑仁_治疗率计算(self):
        original_value = self.get_rank_bonus(1.2, 0.036)
        return original_value
