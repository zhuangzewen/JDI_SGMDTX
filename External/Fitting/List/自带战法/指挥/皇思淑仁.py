# 战法名称: 皇思淑仁
# 战法类型: 指挥
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 皇思淑仁:
# 每个回合开始有60%概率(受智力影响)提升我军随机2-3人18%规避率(受智力影响),持续2回合。
# 每个回合结束时恢复我军随机两人兵力(治疗率120%)

# 满阶皇思淑仁:
# 每个回合开始有60%概率(受智力影响)提升我军随机2-3人18%规避率(受智力影响),持续2回合。
# 每个回合结束时恢复我军随机两人兵力(治疗率120%)

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

class 皇思淑仁_soul(BaseSkillSoul):

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero=None, sourceSoul=None):
        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField=battleField, hero=hero, sourceSoul=sourceSoul)
            return

        if status == SoulResponseTime.回合开始:
            self._deploy_规避率效果(battleField)

        elif status == SoulResponseTime.回合结束:
            self._deploy_治疗效果(battleField)
            pass

    def _deploy_规避率效果(self, battleField):
        initiator = self.initiator
        基础概率 = 0.3
        智力影响 = initiator.get_智力() * 0.001
        最终概率 = min(基础概率 + 智力影响, 0.6)

        if random.random() <= 最终概率:
            Log().battle_L1('[{}]发动战法【{}】'.format(
                initiator.get_武将名称().value, 
                self.skill.get_战法名称().value
            ))

            team = battleField.get_team_by_hero(initiator)
            alive_heroes = team.get_alive_heroes()
            if len(alive_heroes) >= 2:
                效果人数 = random.randint(2, 3)
                效果目标 = random.sample(alive_heroes, min(效果人数, len(alive_heroes)))

                for target_hero in 效果目标:
                    规避率提升值 = self.skill.皇思淑仁_规避率提升系数()
                    规避率soul = self.skill.create_soul(
                        target=target_hero,
                        effect_type=SoulEffectType.规避率提升,
                        effect_value=规避率提升值,
                        duration=2
                    )
                    规避率soul.deploy_initial()
                    Log().battle_L1(f'[{initiator.get_武将名称()}]发动【皇思淑仁】，提升[{target_hero.get_武将名称()}]规避率{规避率提升值*100:.1f}%，持续2回合')

    def _deploy_治疗效果(self, battleField):
        initiator = self.initiator

        Log().battle_L1('[{}]发动战法【{}】'.format(
            initiator.get_武将名称().value, 
            self.skill.get_战法名称().value
        ))

        team = battleField.get_team_by_hero(initiator)
        alive_heroes = team.get_alive_heroes()
        if len(alive_heroes) >= 2:
            治疗目标 = random.sample(alive_heroes, min(2, len(alive_heroes)))

            for target_hero in 治疗目标:
                治疗率 = self.skill.皇思淑仁_治疗率计算()
                治疗量 = 治疗计算(battleField, 施救者=initiator, 受助者=target_hero, 治疗率=治疗率)
                治疗soul = self.skill.create_soul(
                    target=target_hero,
                    effect_type=SoulEffectType.恢复兵力,
                    effect_value=治疗量
                )
                治疗soul.deploy_initial()
                Log().battle_L1(f'[{initiator.get_武将名称()}]发动【皇思淑仁】，为[{target_hero.get_武将名称()}]恢复{治疗量:.0f}兵力')

class 皇思淑仁_skill(BaseSkill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

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

    def 皇思淑仁_规避率提升系数(self):
        基础提升 = 0.09
        owner = self.get_持有者()
        x = owner.get_智力()
        智力加成 = x * 0.0003
        最终提升 = min(基础提升 + 智力加成, 0.18)
        return 最终提升

    def 皇思淑仁_治疗率计算(self):
        基础治疗率 = 0.6
        owner = self.get_持有者()
        x = owner.get_智力()
        智力加成 = x * 0.002
        最终治疗率 = min(基础治疗率 + 智力加成, 1.2)
        return 最终治疗率