
# 战法名称: 星罗棋布
# 战法类型: 指挥
# 战法特性: 辅助
# 适应兵种: 盾,弓,枪,骑
# 发动率: 1

# 星罗棋布:
# 我军全体受到谋略伤害降低10%(受智力影响,对自身的效果提升30%),
# 战斗开始前施加星罗棋布,使阵型加成提升70%(受智力影响),并根据阵型类型获得棋局增益

# 满阶星罗棋布:
# 我军全体受到谋略伤害降低11.5%(受智力影响,对自身的效果提升30%),
# 战斗开始前施加星罗棋布,使阵型加成提升80.5%(受智力影响),并根据阵型类型获得棋局增益

# 棋局增益:
# 不同类型获得的棋局增益:
# 单前排阵型: 我军前排受到伤害降低12%(受智力影响),受击率固定为85%
# 双前排阵型: 我军统帅最低单体对前排造成伤害提升20%,每回合行动时对敌军随机1-2人造成160%伤害(伤害类型由武力或智力高的一项决定)
# 三前排阵型: 每个回合结束后我军智力最高单体对敌军全体造成60%谋略伤害(额外受全队累积治疗量影响)

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

class 星罗棋布_info(SkillInfo):
    def __init__(self):
        self.战法名称 = Fitting_List_Enum.星罗棋布
        self.战法类型 = SkillType.指挥
        self.战法特性 = SkillFeature.辅助
        self.适应兵种 = [WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑]
        self.发动率 = 1

class 星罗棋布_阵型强化_soul(Soul):
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
            if soul.target == hero:
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

        if self.soul持有列表.__len__() > 0:
            Log().show_battle_info('        [{}]的[星罗棋布-阵型]效果已消失'.format(self.target.get_武将名称().value))

        soul_to_remove = []
        for soul in self.soul持有列表:
            soul: Soul
            if soul.initiator == hero:
                soul.restore_initial()
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField, hero, sourceSoul)
            return

        if status != SoulResponseTime.阵型强化结束时:
            return

        for 己方阵型强化soul in 对己方阵型强化SOUL生效(self.target, battleField):
            己方阵型强化soul: Soul
            targetHero = 己方阵型强化soul.target
            存在未强化的阵型SOUL = True
            for exist_soul in self.soul持有列表:
                if exist_soul.sourceType == SoulSourceType.星罗棋布_阵型强化 and exist_soul.target == targetHero and exist_soul.effect_type == 己方阵型强化soul.effect_type and exist_soul.skill == self.skill:
                    存在未强化的阵型SOUL = False
                    break
            if 存在未强化的阵型SOUL:
                Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
                break
        
        for 己方阵型强化soul in 对己方阵型强化SOUL生效(self.target, battleField):
            己方阵型强化soul: Soul
            targetHero = 己方阵型强化soul.target
            target_name = targetHero.get_武将名称().value

            # 判断已经存在 星罗棋布_阵型强化效果的soul continue
            存在未强化的阵型SOUL = False
            for exist_soul in self.soul持有列表:
                if exist_soul.sourceType == SoulSourceType.星罗棋布_阵型强化 and exist_soul.target == targetHero and exist_soul.effect_type == 己方阵型强化soul.effect_type and exist_soul.skill == self.skill:
                    存在未强化的阵型SOUL = True
                    break
            if 存在未强化的阵型SOUL:
                continue

            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-阵型]效果'.format(target_name, self.skill.get_战法名称().value))
            strengRatio = self.skill.星罗棋布_阵型强化系数() * 己方阵型强化soul.effect_value
            阵型强化soul = Soul(target=己方阵型强化soul.target, 
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.星罗棋布_阵型强化, 
                            skill=self.skill, 
                            effect_type=己方阵型强化soul.effect_type, 
                            effect_value=strengRatio)
            阵型强化soul.deploy_initial()
            self.soul持有列表.append(阵型强化soul)

        存在未强化的阵型SOUL = False

class 星罗棋布_谋略减伤_soul(Soul):
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

        souls_to_remove = []
        for soul in self.soul持有列表:
            if soul.target == hero:
                souls_to_remove.append(soul)
        for soul in souls_to_remove:
            self.soul持有列表.remove(soul)

        if self.soul持有列表.__len__() <= 0:
            return
        
        souls_to_remove = []
        for soul in self.soul持有列表:
            if soul.initiator == self.target:
                Log().show_battle_info(f'        [{soul.target.get_武将名称().value}]的[星罗棋布-谋略减伤]效果已消失')
                soul.restore_initial()
                souls_to_remove.append(soul)

        for soul in souls_to_remove:
            self.soul持有列表.remove(soul)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField, hero, sourceSoul)
            return

        if status != SoulResponseTime.战法布阵开始时:
            return
        
        Log().show_battle_info('    [{}]发动战法【{}】'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
        valueList = 对己方所有目标生效(self.target, battleField)
        for 目标武将 in valueList:
            reduce_value = self.skill.星罗棋布_受到谋略伤害降低系数()
            if 目标武将 == self.skill.get_持有者():
                reduce_value = reduce_value * 1.3
            谋略减伤soul = Soul(target=目标武将, 
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.受到谋略伤害, 
                            effect_value= - reduce_value)
            谋略减伤soul.deploy_initial()
            self.soul持有列表.append(谋略减伤soul)

class 星罗棋布_额外效果_soul(Soul):
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
        self.soul持有列表_单前排 = []
        self.soul持有列表_双前排 = []

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if hero != self.initiator:
            return
        
        soul_to_remove = []
        for soul in self.soul持有列表_单前排 + self.soul持有列表_双前排:
            if soul.target == self.target:
                soul_to_remove.append(soul)
        for soul in soul_to_remove:
            self.soul持有列表_单前排.remove(soul) if soul in self.soul持有列表_单前排 else None
            self.soul持有列表_双前排.remove(soul) if soul in self.soul持有列表_双前排 else None

        if self.soul持有列表_单前排.__len__() <= 0 and self.soul持有列表_双前排.__len__() <= 0:
            return

        soul_to_remove = []
        for soul in self.soul持有列表_单前排:
            if soul.initiator == self.target:
                Log().show_battle_info('        [{}]的[星罗棋布-单前排阵型]效果已消失'.format(soul.target.get_武将名称().value))
                soul.restore_initial()
                soul_to_remove.append(soul)

        for soul in self.soul持有列表_双前排:
            if soul.initiator == self.target:
                Log().show_battle_info('        [{}]的[星罗棋布-双前排阵型]效果已消失'.format(soul.target.get_武将名称().value))
                soul.restore_initial()
                soul_to_remove.append(soul)

        for soul in self.soul持有列表_单前排 + self.soul持有列表_双前排:
            if soul.initiator == self.target:
                if soul in self.soul持有列表_单前排:
                    self.soul持有列表_单前排.remove(soul)
                if soul in self.soul持有列表_双前排:
                    self.soul持有列表_双前排.remove(soul)

    def response(self, status = SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField, hero, sourceSoul)
            return

        if status != SoulResponseTime.战法布阵开始时:
            return
        
        Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-额外效果]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
        
        if msg_判断己方前排武将数量(self.target, battleField) == 1:
            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-单前排阵型]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
            frontLineHero = msg_对我方的单前排生效(self.target, battleField)

            固定受击率soul = Soul(target=frontLineHero,
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.固定受击率, 
                            effect_value=0.85)
            固定受击率soul.deploy_initial()
            self.soul持有列表_单前排.append(固定受击率soul)

            单前排减伤soul = Soul(target=frontLineHero, 
                        initiator=self.skill.get_持有者(), 
                        sourceType=SoulSourceType.武将战法, 
                        skill=self.skill, 
                        effect_type=SoulEffectType.受到伤害, 
                        effect_value= - self.skill.星罗棋布_单前排_受到伤害降低系数())
            单前排减伤soul.deploy_initial()
            self.soul持有列表_单前排.append(单前排减伤soul)
            Log().show_battle_info('        [{}]的[星罗棋布-单前排阵型]效果已施加'.format(frontLineHero.get_武将名称().value))

        elif msg_判断己方前排武将数量(self.target, battleField) == 2:
            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-双前排阵型]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))
            lowest_ts_hero = msg_对我方统帅最低的武将(self.target, battleField)

            对前排增伤soul = Soul(target=lowest_ts_hero, 
                            initiator=self.skill.get_持有者(), 
                            sourceType=SoulSourceType.武将战法, 
                            skill=self.skill, 
                            effect_type=SoulEffectType.对前排造成伤害, 
                            effect_value= self.skill.星罗棋布_双前排_对前排造成伤害提升系数())
            对前排增伤soul.deploy_initial()
            self.soul持有列表_双前排.append(对前排增伤soul)

            星罗棋布双前排额外效果soul = 星罗棋布_额外效果_双前排阵型(target=lowest_ts_hero,
                                              initiator=self.skill.get_持有者(),
                                              sourceType=SoulSourceType.武将战法,
                                              skill=self.skill,
                                              response_time=SoulResponseTime.内置待响应,
                                              duration=-1,
                                              effect_type=SoulEffectType.待响应,
                                              effect_value=0,
                                              source_soul=None,
                                              battleField=battleField)
            双前排持有者: Hero = self.skill.get_持有者()
            双前排响应者: Hero = lowest_ts_hero
            双前排持有者.get_持有Soul列表().append(星罗棋布双前排额外效果soul)
            双前排响应者.get_响应Soul列表().append(星罗棋布双前排额外效果soul)
            Log().show_battle_info('        [{}]的[星罗棋布-双前排阵型]效果已施加'.format(lowest_ts_hero.get_武将名称().value))

        elif msg_判断己方前排武将数量(self.target, battleField) == 3:
            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-三前排阵型]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

            星罗棋布三前排额外效果soul = 星罗棋布_额外效果_三前排阵型(target=self.target,
                                              initiator=self.skill.get_持有者(),
                                              sourceType=SoulSourceType.武将战法,
                                              skill=self.skill,
                                              response_time=SoulResponseTime.内置待响应,
                                              duration=-1,
                                              effect_type=SoulEffectType.待响应,
                                              effect_value=0,
                                              source_soul=None,
                                              battleField=battleField)
            self.target.get_持有Soul列表().append(星罗棋布三前排额外效果soul)
            self.target.get_响应Soul列表().append(星罗棋布三前排额外效果soul)
            Log().show_battle_info('        [{}]的[星罗棋布-三前排阵型]效果已施加'.format(self.target.get_武将名称().value))

class 星罗棋布_额外效果_双前排阵型(Soul):
    def __init__(self, target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if hero != self.initiator:
            return
        
        if self.target == hero:
            return
        
        Log().show_battle_info('        [{}]的[星罗棋布-双前排阵型]效果已消失'.format(self.target.get_武将名称().value))

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField, hero, sourceSoul)
            return

        if status != SoulResponseTime.回合行动时 or hero != self.target:
            return

        Log().show_battle_info('    [{}]执行来自【{}】的[星罗棋布-双前排阵型]效果'.format(self.target.get_武将名称().value, self.skill.get_战法名称().value))

        # 发起攻击的武将
        atta_hero = self.target
        attaHero_name = atta_hero.get_武将名称()
        attacked_heroes = 对敌方所有目标生效(atta_hero, battleField)

        # 发起攻击次数
        attack_times = int_随机一到两个敌方()
        for _ in range(attack_times):

            if len(attacked_heroes) == 0:
                Log().show_battle_info('    [{}]没有可攻击的敌方武将'.format(attaHero_name.value))
                break

            attacked: Hero = 从队列确定受击武将(attacked_heroes)
            attacked_heroes.remove(attacked)
            damageModel = 计算伤害(battleField, atta_hero, attacked, SoulDamageType.择优, SkillType.指挥, 伤害值= 1.6)
            damageModel.skillEffectName = "星罗棋布-双前排阵型"

            # 创建一个伤害 SOUL
            damage_soul = Soul(target=attacked,
                                initiator=atta_hero,
                                sourceType=SoulSourceType.武将战法,
                                skill= self.skill,
                                effect_type=SoulEffectType.损失兵力,
                                effect_value= damageModel.damage_value,
                                source_soul=self,
                                battleField= battleField,
                                damage=damageModel)
            damage_soul.deploy_initial()

class 星罗棋布_额外效果_三前排阵型(Soul):
    def __init__(self, target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField):
        super().__init__(target, initiator, sourceType, skill, response_time, duration, effect_type, effect_value, source_soul, battleField)

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        if hero != self.initiator:
            return

    def response(self, status=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul: Soul = None):

        if status == SoulResponseTime.武将溃败:
            self.handle_defeat(battleField, hero, sourceSoul)
            return

        if status != SoulResponseTime.回合结束时:
            return

        # 发起攻击的武将
        atta_hero = msg_对我方智力最高的武将(self.target, battleField)
        attaHero_name = atta_hero.get_武将名称()
        attacked_heroes = 对敌方所有目标生效(atta_hero, battleField)

        Log().show_battle_info('    [{}]执行来自【{}】的[星罗棋布-三前排阵型]效果'.format(attaHero_name.value, self.skill.get_战法名称().value))

        # 发起攻击次数
        attack_times = len(attacked_heroes)
        for i in range(attack_times):

            if len(attacked_heroes) == 0:
                Log().show_battle_info('    [{}]没有可攻击的敌方武将'.format(attaHero_name.value))
                break

            attacked: Hero = 从队列确定受击武将(attacked_heroes)
            attacked_heroes.remove(attacked)

            ourTeam = 获取武将所在的队伍(atta_hero, battleField)
            ourTeam_治疗总量 = ourTeam.全队累计治疗量

            受治疗影响伤害系数 = self.skill.星罗棋布_三前排_治疗量造成的伤害提升系数(ourTeam_治疗总量)
            damageModel = 计算伤害(battleField, atta_hero, attacked, SoulDamageType.谋略, SkillType.指挥, 伤害值= 受治疗影响伤害系数)
            damageModel.skillEffectName = "星罗棋布-三前排阵型"

            # 创建一个伤害 SOUL
            damage_soul = Soul(target=attacked,
                                initiator=atta_hero,
                                sourceType=SoulSourceType.武将战法,
                                skill= self.skill,
                                effect_type=SoulEffectType.损失兵力,
                                effect_value=damageModel.damage_value,
                                source_soul=self,
                                battleField=battleField,
                                damage=damageModel)
            damage_soul.deploy_initial()

class 星罗棋布_skill(Skill):
    def __init__(self, hero, skillName):
        super().__init__(hero, skillName)

    def fill_init_soul(self):
        持有者and响应者: Hero = self.get_持有者()

        星罗棋布阵型强化soul = 星罗棋布_阵型强化_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=SoulResponseTime.内置待响应,
            duration=-1,
            effect_type=SoulEffectType.待响应,
            effect_value=0,
            source_soul=None,
            battleField=None)
        持有者and响应者.get_持有Soul列表().append(星罗棋布阵型强化soul)
        持有者and响应者.get_响应Soul列表().append(星罗棋布阵型强化soul)

        星罗棋布谋略减伤soul = 星罗棋布_谋略减伤_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=SoulResponseTime.内置待响应,
            duration=-1,
            effect_type=SoulEffectType.待响应,
            effect_value=0,
            source_soul=None,
            battleField=None)
        持有者and响应者.get_持有Soul列表().append(星罗棋布谋略减伤soul)
        持有者and响应者.get_响应Soul列表().append(星罗棋布谋略减伤soul)

        星罗棋布额外效果soul = 星罗棋布_额外效果_soul(
            target=self.get_持有者(),
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=SoulResponseTime.内置待响应,
            duration=-1,
            effect_type=SoulEffectType.待响应,
            effect_value=0,
            source_soul=None,
            battleField=None)
        持有者and响应者.get_持有Soul列表().append(星罗棋布额外效果soul)
        持有者and响应者.get_响应Soul列表().append(星罗棋布额外效果soul)

    def 星罗棋布_阵型强化系数(self):
        def 拟合过程数据统计():
            # 初始值为 70%
            # 每一级升阶提升基础初始值为 2.1%

            # 智力 260
            # [吕布] 的【奇谋几率】提升 8.39%(16.39%)
            # 提升值为 8.39 / (16.39 - 8.39) - 0.7 = 0.3485

            # 智力 270
            # [吕布]的【奇谋几率】提升8.54%(16.54%)
            # 提升值为 8.54 / (16.54 - 8.54) - 0.7 = 0.3675

            # 智力 280
            # [姜维] 的【奇谋几率】提升 8.70%(16.70%)
            # 提升值为 8.70 / (16.70 - 8.70) - 0.7 = 0.3875

            # 智力 290
            # [吕布]的【奇谋几率】提升8.85%(16.85%)
            # 提升值为 8.85 / (16.85 - 8.85) - 0.7 = 0.40625

            # 智力 300
            # [吕布] 的【奇谋几率】提升 9.00%(17.00%)
            # 提升值为 9.00 / (17.00 - 9.00) - 0.7 = 0.425

            # 智力 310
            # [吕布] 的【奇谋几率】提升 9.15%(17.15%)
            # 提升值为 9.15 / (17.15 - 9.15) - 0.7 = 0.44375

            # x 为智力, y 为提升值 
            # y = 0.001875x - 0.14875

            pass

        rankUp = self.get_战法升阶()
        from Generals.JDI_Hero import Hero
        original_value = 0.7 + rankUp * 0.021
        owner: Hero = self.get_持有者()
        x = owner.get_智力()
        y = 0.001875 * x - 0.14875 + original_value
        return y
    
    def 星罗棋布_受到谋略伤害降低系数(self):
        def 拟合过程数据统计():
            # 初始值为 10%
            # 每一级升阶提升基础初始值为 0.3%

            # 智力 297.68
            # [吕布] 的【受到谋略伤害】降低 14.21%(-14.21%)
            # 提升值为 14.21 - 11.5 = 2.71%
            # 转为小数 0.0271

            # 智力 308.99
            # [吕布]的【受到谋略伤害]降低14.42%(-14.42%)
            # 提升值为 14.42 - 11.5 = 2.9%
            # 转为小数 0.029

            # 智力 320.12
            # [吕布] 的【受到谋略伤害] 降低 14.62%(14.62%)
            # 提升值为 14.62 - 11.5 = 3.12%
            # 转为小数 0.0312

            # 智力 331.25
            # [吕布] 的【受到谋略伤害] 降低 14.83%(-14.83%)
            # 提升值为 14.83 - 11.5 = 3.33%
            # 转为小数 0.033

            # 智力 342.38
            # [吕布] 的【受到谋略伤害] 降低 15.03%(-15.03%)
            # 提升值为 15.03 - 11.5 = 3.53%
            # 转为小数 0.0353

            # 智力 353.51
            # [吕布] 的【受到谋略伤害] 降低 15.23%(-15.23%)
            # 提升值为 15.23 - 11.5 = 3.73%
            # 转为小数 0.0373

            # x 为智力, y 为提升值 
            # y = 0.000189x - 0.03815

            pass

        rankUp = self.get_战法升阶()
        from Generals.JDI_Hero import Hero
        original_value = 0.1 + rankUp * 0.003
        owner: Hero = self.get_持有者()
        x = owner.get_智力()
        y = 0.000189 * x - 0.03815 + original_value
        return y
    
    def 星罗棋布_单前排_受到伤害降低系数(self):
        def 拟合过程数据统计():
            # 初始值为 12%
            # 棋局布阵效果初始值 不受升阶影响

            # 智力 297.68
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮] 的【受到伤害】降低 19.42%(-19.92%)
            # 实际值为 (0.1942 − 0.005) / 0.95 = 0.1992
            # 提升值为 0.1992 - 0.12 = 0.0792

            # 智力 308.99
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮]的【受到伤害】降低19.66%(-20.16%)
            # 提升值为 (0.1966 − 0.005) / 0.95 = 0.2017

            # 智力 320.12
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮] 的【受到伤害】降低 19.90%(-20.40%)
            # 提升值为 (0.1990 − 0.005) / 0.95 = 0.2042

            # 智力 331.25
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮] 的【受到伤害】降低 20.14%(-20.64%)
            # 提升值为 (0.2014 − 0.005) / 0.95 = 0.2067

            # 智力 342.38
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮] 的【受到伤害】降低 20.38%(-20.88%)
            # 提升值为 (0.2038 − 0.005) / 0.95 = 0.2093

            # 智力 353.51
            # [诸葛亮] 的【受到伤害】降低 0.50%(-0.50%)
            # [诸葛亮] 的【受到伤害】降低 20.62%(-21.12%)
            # 提升值为 (0.2062 − 0.005) / 0.95 = 0.2118

            # x 为智力, y 为提升值 
            # y = 0.000226x + 0.139

            pass

        from Generals.JDI_Hero import Hero
        original_value = 0.12
        owner: Hero = self.get_持有者()
        x = owner.get_智力()
        y = 0.000226 * x + 0.139 + original_value
        return y
    
    def 星罗棋布_双前排_对前排造成伤害提升系数(self):
        # 初始值为 20%
        # 棋局布阵效果初始值 不受升阶影响

        return 0.2
    
    def 星罗棋布_三前排_治疗量造成的伤害提升系数(self, 治疗总量):
        def 拟合过程数据统计():
            # 初始值为 60%
            # 棋局布阵效果初始值 不受升阶影响

            # 累计 981
            # 伤害 487

            # 累计 3829
            # 伤害 680

            # 累计 5915
            # 伤害 741
            
            # 累计 10571
            # 伤害 857

            # 累计 13006
            # 伤害 893

            # 累计 14813
            # 伤害 931

            # 累计 15996
            # 伤害 926

            # 累计 17770
            # 伤害 952

            # 第八回合个兵力依然有 9660 ，默认不受兵力影响
            # y = -1.12e-7 * x**2 + 0.061 * x + 412.5

            # 增长谋略系数为 
            # y = -1.614e-10 * x**2 + 8.87e-5 * x
            pass

        original_value = 0.6
        x = 治疗总量
        y = -1.614e-10 * x**2 + 8.87e-5 * x + original_value
        return y

