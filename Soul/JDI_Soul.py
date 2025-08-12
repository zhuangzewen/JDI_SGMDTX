from Control.Log.JDI_Log import Log
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulSourceType_Enum import SoulSourceType, SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from External.JDI_Skill import Skill
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Generals.JDI_Hero import Hero
from Soul.Class.Damage_Class import Damage
from Calcu.JDI_Calculate import msg_移除响应
from BattleField.Team.JDI_Team import Team
import random

class Soul():
    # 目标 发起者 来源类型 技能 响应时机 持续回合 效果类型 效果值
    # 声明传入的类型 而不是any
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 initiaTeam: Team = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 sourceDetail: [SoulSourceDetail] = [], # pyright: ignore[reportInvalidTypeForm]
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None,
                 damage: Damage = None):
        self.target = target                # 目标
        self.initiator = initiator          # 发起者
        self.initiaTeam = initiaTeam        # 发起队伍
        self.sourceType = sourceType        # 来源类型
        self.sourceDetail = sourceDetail    # 来源详情
        self.skill = skill                  # 技能
        self.response_time = response_time  # 响应时机
        self.duration = duration            # 持续回合
        self.effect_type = effect_type      # 效果类型
        self.effect_value = effect_value    # 效果值
        self.source_soul = source_soul      # 来源魂灵
        self.damage = damage                # 伤害类

        if battleField is not None:
            from BattleField.JDI_BattleField import BattleField
            self.battleField = battleField

    def response(self, status: SoulResponseTime=SoulResponseTime.无响应阶段, battleField=None, hero: Hero = None, sourceSoul = None):
        pass

    def deploy_initial(self):

        self.target: Hero
        heroName = self.target.get_武将名称().value

        # 补充判断 当发起者或目标为 溃败状态时 不响应
        if self.initiator is not None and self.initiator.get_被击溃状态():
            return
        if self.target is not None and self.target.get_被击溃状态():
            return

        # 将 self.effect_type 转化为 方法名
        method_name = f"deploy_{self.effect_type.name}_initial"
        # 若是存在 则引用
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            if method(self) != False:

                if SoulSourceDetail.负面状态效果 in self.sourceDetail:
                    self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                    self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

                return
        else:
            Log().show_debug_info(f'[DEBUG] {method_name} not found in Soul')

        # if (self.deploy_增减伤系数_initial() != False):
        #     return

        if (self.deploy_异常状态_initial() != False):
            return

        if self.effect_value > 0:
            show_upEffect_name = '提升'
        else:
            show_upEffect_name = '降低'

        from Soul.Enum.SoulEffectType_Enum import SoulEffectType


        if self.effect_type == SoulEffectType.看破:
            cur_value = getattr(self.target, HeroInfoKey.看破.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.看破.value, cur_value)
            Log().battle_L2('[{}]的【看破】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.破甲:
            cur_value = getattr(self.target, HeroInfoKey.破甲.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.破甲.value, cur_value)
            Log().battle_L2('[{}]的【破甲】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.抵御:
            cur_value = getattr(self.target, HeroInfoKey.抵御.value)
            if cur_value == 2:
                Log().battle_L2('[{}]的「抵御」效果已刷新'.format(heroName))
                return
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.抵御.value, cur_value)
            Log().battle_L2('[{}]的【抵御次数】{}{}({})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))
            Log().battle_L2('[{}]的「抵御」效果已施加'.format(heroName))

        elif self.effect_type == SoulEffectType.攻心:
            cur_value = getattr(self.target, HeroInfoKey.攻心.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.攻心.value, cur_value)
            Log().battle_L2('[{}]的【攻心】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.连击几率:
            cur_value = getattr(self.target, HeroInfoKey.连击几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.连击几率.value, cur_value)
            Log().battle_L2('[{}]的【连击几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.规避:
            cur_value = getattr(self.target, HeroInfoKey.规避.value)
            self.effect_value *= (1 - cur_value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.规避.value, cur_value)
            Log().battle_L2('[{}]的【规避】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.会心几率:
            cur_value = getattr(self.target, HeroInfoKey.会心几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.会心几率.value, cur_value)
            Log().battle_L2('[{}]的【会心几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.会心伤害:
            cur_value = getattr(self.target, HeroInfoKey.会心伤害.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.会心伤害.value, cur_value)
            Log().battle_L2('[{}]的【会心伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))
            if self.effect_value < 0 and SoulSourceDetail.异常状态效果_额外效果 not in self.sourceDetail:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.奇谋几率:
            cur_value = getattr(self.target, HeroInfoKey.奇谋几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.奇谋几率.value, cur_value)
            Log().battle_L2('[{}]的【奇谋几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.奇谋伤害:
            cur_value = getattr(self.target, HeroInfoKey.奇谋伤害.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.奇谋伤害.value, cur_value)
            Log().battle_L2('[{}]的【奇谋伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))
            if self.effect_value < 0 and SoulSourceDetail.异常状态效果_额外效果 not in self.sourceDetail:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.固定受击率:
            setattr(self.target, HeroInfoKey.固定受击率.value, True)
            Log().battle_L2(f'[{heroName}]的【固定受击率】提升为{self.effect_value * 100:.2f}%')

        elif self.effect_type == SoulEffectType.清醒:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.清醒 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[清醒]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[清醒]效果已施加'.format(heroName))

        elif self.effect_type == SoulEffectType.受治疗效果:
            cur_value = getattr(self.target, HeroInfoKey.受治疗效果.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.受治疗效果.value, cur_value)
            Log().battle_L2('[{}]的【受治疗效果】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.损失兵力:

            self.battleField.respond(status=SoulResponseTime.受到伤害前, 时机响应武将=self.target, 溯源SOUL=self)
            # 进一个 闪避的 判断

            if self.target.get_规避() > 0:
                if random.random() < self.target.get_规避():
                    # [赵云]成功规避[姜维]的伤害
                    Log().battle_L2(f'[{heroName}]成功规避[{self.initiator.get_武将名称().value}]的伤害')
                    self.battleField.respond(status=SoulResponseTime.规避伤害时, 时机响应武将=self.target, 溯源SOUL=self)
                    return

            伤害来源武将: Hero = self.initiator
            伤害来源武将名称 = 伤害来源武将.get_武将名称().value if 伤害来源武将 else '未知来源'
            伤害来源技能名称 = self.skill.get_战法名称().value if self.skill else '未知技能'
            伤害来源Soul效果 = self.damage.skillEffectName if self.damage else '未知效果来源'
            伤害数值 = int(self.effect_value)

            剩余抵御次数 = self.target.get_抵御()
            if 剩余抵御次数 > 0:
                # 0.7 - 0.9 两位数
                抵御减伤 = random.randint(70, 90) / 100
                Log().battle_L2('[{}]消耗一次抵御机会,此次伤害减少{:.2f}%'.format(heroName, 抵御减伤 * 100))
                Log().battle_L2('[{}]的【抵御次数】降低1({})'.format(heroName, 剩余抵御次数 - 1))
                setattr(self.target, HeroInfoKey.抵御.value, 剩余抵御次数 - 1)
                伤害数值 = int(伤害数值 * (1 - 抵御减伤))

            if (self.target.get_兵力() < 伤害数值):
                伤害数值 = int(self.target.get_兵力())
            剩余兵力 = int(self.target.get_兵力() - 伤害数值)

            伤兵数值 = int(伤害数值 * 0.8)
            亖兵数值 = int(伤害数值 - 伤兵数值)

            setattr(self.target, HeroInfoKey.伤兵.value, self.target.get_伤兵() + 伤兵数值)
            setattr(self.target, HeroInfoKey.亖兵.value, self.target.get_亖兵() + 亖兵数值)
            setattr(self.target, HeroInfoKey.兵力.value, 剩余兵力)
            if (self.skill and self.skill.get_战法名称() == Fitting_List_Enum.普攻):
                Log().battle_L2('[{}]损失了兵力{}({})'.format(heroName, abs(伤害数值), 剩余兵力))
            else:
                if 伤害来源Soul效果 == '':
                    Log().battle_L2(f'[{heroName}]由于[{伤害来源武将名称}]的【{伤害来源技能名称}】的伤害,损失了兵力{abs(伤害数值)}({剩余兵力})')
                else :
                    Log().battle_L2(f'[{heroName}]由于[{伤害来源武将名称}]【{伤害来源技能名称}】的[{伤害来源Soul效果}]效果,损失了兵力{abs(伤害数值)}({剩余兵力})')

            if 剩余兵力 <= 0:
                Log().battle_L2('[{}]兵力为0 无法再战'.format(heroName))
                self.battleField.respond(status=SoulResponseTime.武将溃败, 时机响应武将=self.target)

            from BattleField.JDI_BattleField import BattleField
            self.battleField : BattleField
            self.battleField.respond(status=SoulResponseTime.造成伤害时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.受到伤害时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.恢复兵力:

            恢复兵力 = int(self.effect_value)
            
            for soul in self.target.get_响应Soul列表():
                from Soul.Enum.SoulEffectType_Enum import SoulEffectType
                if soul.effect_type == SoulEffectType.断粮:
                    Log().battle_L2('[{}]由于[{}]【{}】的[断粮]效果治疗效率降为30%'.format(self.target.get_武将名称().value, soul.initiator.get_武将名称().value, soul.skill.get_战法名称().value))
                    恢复兵力 = int(恢复兵力 * 0.7)
                    break

            当前兵力 = self.target.get_兵力()
            当前伤兵 = self.target.get_伤兵()

            if 恢复兵力 <= 当前伤兵:
                剩余伤兵 = 当前伤兵 - 恢复兵力
                实际兵力 = 当前兵力 + 恢复兵力
                setattr(self.target, HeroInfoKey.伤兵.value, 剩余伤兵)
                setattr(self.target, HeroInfoKey.兵力.value, 实际兵力)
            else:
                恢复兵力 = 当前伤兵
                剩余伤兵 = 0
                实际兵力 = 当前兵力 + 恢复兵力
                setattr(self.target, HeroInfoKey.伤兵.value, 剩余伤兵)
                setattr(self.target, HeroInfoKey.兵力.value, 实际兵力)

            Log().battle_L2('[{}]恢复了兵力{}({})'.format(self.target.get_武将名称().value, 恢复兵力, self.target.get_兵力()))

    def deploy_异常状态_initial(self):

        self.target: Hero
        heroName = self.target.get_武将名称().value

        from Soul.Enum.SoulEffectType_Enum import SoulEffectType
        if self.effect_type == SoulEffectType.震慑:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.震慑 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[震慑]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[震慑]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.缴械:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.缴械 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[缴械]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[缴械]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.技穷:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.技穷 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[技穷]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[技穷]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.混乱:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.混乱 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)
            
            if is存在同类状态:
                Log().battle_L2('[{}]的[混乱]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[混乱]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.嘲讽:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.嘲讽 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)
            
            if is存在同类状态:
                Log().battle_L2('[{}]的[嘲讽]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[嘲讽]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.虚弱:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.虚弱 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)
            
            if is存在同类状态:
                Log().battle_L2('[{}]的[虚弱]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[虚弱]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.断粮:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.断粮 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[断粮]效果已刷新'.format(heroName))
            else:
                Log().battle_L2('[{}]的[断粮]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加控制时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加控制时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.洪水:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.洪水 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[洪水]效果已刷新'.format(heroName))
            else:
                统率soul = Soul(target=self.target, 
                                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                        skill=self.skill,
                                        effect_type=SoulEffectType.统率, 
                                        effect_value=-20,
                                        source_soul=self)
                统率soul.deploy_initial()
                Log().battle_L2('[{}]的[洪水]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.火攻:
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.火攻 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[火攻]效果已刷新'.format(heroName))
            else:
                智力soul = Soul(target=self.target, 
                                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                        skill=self.skill,
                                        effect_type=SoulEffectType.智力, 
                                        effect_value=-15,
                                        source_soul=self)
                智力soul.deploy_initial()
                Log().battle_L2('[{}]的[火攻]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.风暴:

            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.风暴 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[风暴]效果已刷新'.format(heroName))
            else:
                先攻soul = Soul(target=self.target, 
                                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                        skill=self.skill,
                                        effect_type=SoulEffectType.先攻, 
                                        effect_value=-30,
                                        source_soul=self)
                先攻soul.deploy_initial()
                Log().battle_L2('[{}]的[风暴]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.畏惧:

            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.畏惧 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)
            
            if is存在同类状态:
                Log().battle_L2('[{}]的[畏惧]效果已刷新'.format(heroName))
            else:
                受到伤害soul = Soul(target=self.target, 
                                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                        skill=self.skill,
                                        effect_type=SoulEffectType.受到伤害提升固定值, 
                                        effect_value=0.1,
                                        source_soul=self)
                受到伤害soul.deploy_initial()
                Log().battle_L2('[{}]的[畏惧]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.妖术:
    
            is存在同类状态 = False
            if len(self.target.get_响应Soul列表()) > 0:
                for soul in self.target.get_响应Soul列表():
                    if soul.effect_type == SoulEffectType.妖术 and soul != self:
                        is存在同类状态 = True
                        msg_移除响应(soul)

            if is存在同类状态:
                Log().battle_L2('[{}]的[妖术]效果已刷新'.format(heroName))
            else:
                会心伤害soul = Soul(target=self.target, 
                            sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],  
                            skill=self.skill,
                            effect_type=SoulEffectType.会心伤害, 
                            effect_value=-0.15,
                            source_soul=self)
                会心伤害soul.deploy_initial()
                奇谋伤害soul = Soul(target=self.target, 
                            sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                            skill=self.skill,
                            effect_type=SoulEffectType.奇谋伤害,
                            effect_value=-0.15,
                            source_soul=self)
                奇谋伤害soul.deploy_initial()
                Log().battle_L2('[{}]的[妖术]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        else:
            return False

    def restore_initial(self):

        self.target: Hero
        if self.target.get_被击溃状态():
            return

        heroInfo = getattr(self.target, HeroInfoKey.武将信息.value)
        heroName = getattr(heroInfo, HeroInfoKey.武将名称.value).value
        
        if self.effect_value > 0:
            show_upEffect_name = '降低'
        else:
            show_upEffect_name = '提升'

        if self.damage and self.damage.skillEffectName:
            Log().battle_L2('[{}]的[{}]效果已消失'.format(heroName, self.damage.skillEffectName))

        if self.effect_type == SoulEffectType.破甲:
            cur_value = getattr(self.target, HeroInfoKey.破甲.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.破甲.value, cur_value)
            Log().battle_L2('[{}]的【破甲】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.看破:
            cur_value = getattr(self.target, HeroInfoKey.看破.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.看破.value, cur_value)
            Log().battle_L2('[{}]的【看破】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.攻心:
            cur_value = getattr(self.target, HeroInfoKey.攻心.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.攻心.value, cur_value)
            Log().battle_L2('[{}]的【攻心】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.规避:
            cur_value = getattr(self.target, HeroInfoKey.规避.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.规避.value, cur_value)
            Log().battle_L2('[{}]的【规避】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.连击几率:
            cur_value = getattr(self.target, HeroInfoKey.连击几率.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.连击几率.value, cur_value)
            Log().battle_L2('[{}]的【连击几率】{}{:.2f}%({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.会心几率:
            cur_value = getattr(self.target, HeroInfoKey.会心几率.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.会心几率.value, cur_value)
            Log().battle_L2('[{}]的【会心几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.奇谋几率:
            cur_value = getattr(self.target, HeroInfoKey.奇谋几率.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.奇谋几率.value, cur_value)
            Log().battle_L2('[{}]的【奇谋几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.固定受击率:
            setattr(self.target, HeroInfoKey.固定受击率.value, True)
            Log().battle_L2(f'[{heroName}]的【固定受击率】降低为{self.effect_value * 100:.2f}%')

        elif self.effect_type == SoulEffectType.清醒:
            msg_移除响应(self)
            Log().battle_L2('[{}]的【清醒】效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.受治疗效果:
            cur_value = getattr(self.target, HeroInfoKey.受治疗效果.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.受治疗效果.value, cur_value)
            Log().battle_L2('[{}]的【受治疗效果】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.震慑:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[震慑]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.缴械:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[缴械]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.技穷:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[技穷]效果已消失'.format(heroName))

       

        elif self.effect_type == SoulEffectType.混乱:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[混乱]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.嘲讽:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[嘲讽]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.虚弱:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[虚弱]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.断粮:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[断粮]效果已消失'.format(heroName))

        elif self.effect_type == SoulEffectType.洪水:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[洪水]效果已消失'.format(heroName))
            统率soul = Soul(target=self.target, 
                                    sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                    skill=self.skill,
                                    effect_type=SoulEffectType.统率, 
                                    effect_value=20,
                                    source_soul=self)
            统率soul.deploy_initial()

        elif self.effect_type == SoulEffectType.火攻:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[火攻]效果已消失'.format(heroName))

            智力soul = Soul(target=self.target, 
                                    sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                    skill=self.skill,
                                    effect_type=SoulEffectType.智力, 
                                    effect_value=15,
                                    source_soul=self)
            智力soul.deploy_initial()

        elif self.effect_type == SoulEffectType.风暴:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[风暴]效果已消失'.format(heroName))

            先攻soul = Soul(target=self.target, 
                                    sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                    skill=self.skill,
                                    effect_type=SoulEffectType.先攻, 
                                    effect_value=30,
                                    source_soul=self)
            先攻soul.deploy_initial()

        elif self.effect_type == SoulEffectType.畏惧:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[畏惧]效果已消失'.format(heroName))

            受到伤害soul = Soul(target=self.target, 
                                    sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                                    skill=self.skill,
                                    effect_type=SoulEffectType.受到伤害降低固定值, 
                                    effect_value=-0.1,
                                    source_soul=self)
            受到伤害soul.deploy_initial()

        elif self.effect_type == SoulEffectType.妖术:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[妖术]效果已消失'.format(heroName))

            会心伤害soul = Soul(target=self.target,
                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                        skill=self.skill,
                        effect_type=SoulEffectType.会心伤害, 
                        effect_value=0.15,
                        source_soul=self)
            会心伤害soul.deploy_initial()
            奇谋伤害soul = Soul(target=self.target, 
                        sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                        skill=self.skill,
                        effect_type=SoulEffectType.奇谋伤害,
                        effect_value=0.15,
                        source_soul=self)
            奇谋伤害soul.deploy_initial()

        elif self.effect_type == SoulEffectType.损失兵力:
            # 兵噶不恢复
            pass

        elif self.effect_type == SoulEffectType.恢复兵力:
            # 兵力不恢复
            pass

# 战法基础模板系统合并
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import WeaponType
from External.JDI_Skill import SkillInfo, Skill
from External.Fitting.Enum.FittingFeature_Enum import SkillFeature
from External.Fitting.Enum.FittingType_Enum import SkillType
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulSourceType_Enum import SoulSourceType, SoulSourceDetail
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Soul.Enum.SoulDamageType_Enum import SoulDamageType
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import *
from BattleField.Team.JDI_Team import Team
import random

__all__ = [
    'BaseSkillInfo', 'BaseSkillSoul', 'BaseSkill', 'get_skill_template',
    'SoulResponseTime', 'SoulSourceType', 'SoulSourceDetail', 'SoulEffectType', 'SoulDamageType',
    'SkillType', 'Fitting_List_Enum', 'Log', 'random'
]

class SkillTemplate:
    """战法配置模板类，用于快速创建战法配置"""
    def __init__(self, skill_name: Fitting_List_Enum, skill_type: SkillType, 
                 skill_feature: SkillFeature, weapon_types: List[WeaponType], 
                 trigger_rate: float):
        self.skill_name = skill_name
        self.skill_type = skill_type
        self.skill_feature = skill_feature
        self.weapon_types = weapon_types
        self.trigger_rate = trigger_rate

class BaseSkillInfo(SkillInfo):
    """基础战法信息类，简化继承"""
    def __init__(self, template: SkillTemplate):
        super().__init__(template.skill_name)
        self.战法名称 = template.skill_name
        self.战法类型 = template.skill_type
        self.战法特性 = template.skill_feature
        self.适应兵种 = template.weapon_types
        self.发动率 = template.trigger_rate

class BaseSkillSoul(Soul):
    """基础战法Soul类,提供通用功能"""
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 initiaTeam: Team = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 sourceDetail: List[SoulSourceDetail] = [],
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.无响应阶段, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0,
                 source_soul = None,
                 battleField = None,
                 damage: 'Damage' = None):
        super().__init__(target, initiator, initiaTeam, sourceType, sourceDetail, skill, response_time, 
                        duration, effect_type, effect_value, source_soul, battleField, damage)
        self.soul持有列表 = []

    def handle_defeat(self, battleField=None, hero: Hero = None, sourceSoul: Soul = None):
        """通用的失败处理逻辑"""
        if hero != self.initiator:
            return
        self._remove_souls_for_target(hero)
        if self.damage and self.damage.skillEffectName:
            skillEffectName = self.damage.skillEffectName
            Log().battle_L2('[{}]的[{}]效果已消失'.format(self.target.get_武将名称().value, skillEffectName))
        self._restore_and_remove_initiator_souls()
        msg_移除响应(self)

    def _remove_souls_for_target(self, target: Hero):
        """移除目标英雄的souls"""
        soul_to_remove = [soul for soul in self.soul持有列表 if soul.target == target]
        for soul in soul_to_remove:
            self.soul持有列表.remove(soul)

    def _restore_and_remove_initiator_souls(self):
        """恢复并移除发起者的souls"""
        souls_to_process = [soul for soul in self.soul持有列表 if soul.initiator == self.target]
        for soul in souls_to_process:
            soul.restore_initial()
            while soul in self.soul持有列表:
                self.soul持有列表.remove(soul)

class BaseSkill(Skill):
    """基础战法技能类，提供通用功能"""
    def __init__(self, hero: Hero, skillName: Fitting_List_Enum):
        super().__init__(hero, skillName)

    def create_soul(self, 
                    target: Hero, 
                    effect_type: SoulEffectType, 
                    effect_value: float, 
                    response_time: SoulResponseTime = SoulResponseTime.内置待响应,
                    duration: int = -1,
                    source_soul = None,
                    damage: 'Damage' = None) -> Soul:
        """创建标准Soul的便捷方法"""
        return Soul(
            target=target,
            initiator=self.get_持有者(),
            sourceType=SoulSourceType.武将战法,
            skill=self,
            response_time=response_time,
            duration=duration,
            effect_type=effect_type,
            effect_value=effect_value,
            source_soul=source_soul,
            damage=damage
        )

    def deploy_soul(self, soul: Soul, add_to_list: bool = True):
        """部署Soul的便捷方法"""
        soul.deploy_initial()
        if add_to_list and hasattr(self, 'soul持有列表'):
            self.soul持有列表.append(soul)

    def get_rank_bonus(self, base_value: float, rank_multiplier: float) -> float:
        """根据战法升阶计算加成的便捷方法"""
        rank = self.get_战法升阶()
        return base_value + rank * rank_multiplier

    def create_damage_soul(self, battleField, initiator: Hero, target: Hero, 
                          damage_type: SoulDamageType, skill_type: SkillType, 
                          damage_multiplier: float, source_soul: Soul = None,
                          effect_name: str = None) -> Soul:
        """创建伤害Soul的便捷方法"""
        damage_model = 计算伤害(battleField, initiator, target, damage_type, skill_type, damage_multiplier)
        if effect_name:
            damage_model.skillEffectName = effect_name
        damage_soul = Soul(
            target=target,
            initiator=initiator,
            sourceType=SoulSourceType.武将战法,
            skill=self,
            effect_type=SoulEffectType.损失兵力,
            effect_value=damage_model.damage_value,
            source_soul=source_soul,
            battleField=battleField,
            damage=damage_model
        )
        return damage_soul

def get_skill_template(template_type: str, skill_name: Fitting_List_Enum, trigger_rate: float = None):
    """获取战法模板的工厂方法"""
    default_rates = {
        '被动_兵刃': 1.0,
        '主动_谋略': 1.0,
        '主动_治疗': 1.0,
        '指挥_治疗': 1.0,
        '指挥_谋略': 1.0,
        '指挥_文武': 1.0,
        '指挥_辅助': 1.0,
        '追击_兵刃': 1.0
    }
    final_trigger_rate = trigger_rate if trigger_rate is not None else default_rates.get(template_type, 1.0)
    templates = {
        '被动_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.被动,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '主动_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.主动,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '主动_治疗': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.主动,
            skill_feature=SkillFeature.治疗,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_谋略': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.谋略,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_文武': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.文武,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_辅助': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.辅助,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '追击_兵刃': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.追击,
            skill_feature=SkillFeature.兵刃,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
        '指挥_治疗': SkillTemplate(
            skill_name=skill_name,
            skill_type=SkillType.指挥,
            skill_feature=SkillFeature.治疗,
            weapon_types=[WeaponType.盾, WeaponType.弓, WeaponType.枪, WeaponType.骑],
            trigger_rate=final_trigger_rate
        ),
    }
    if template_type not in templates:
        raise ValueError(f"Unknown template type: {template_type}")
    return templates.get(template_type)


# 文件末尾自动注册所有 deploy_*_initial && restore_*_initial 方法到 Soul 类
import types
from Soul.List.受到伤害 import *
from Soul.List.造成伤害 import *
from Soul.List.基础属性 import *
for name, obj in list(globals().items()):
    if name.startswith('deploy_') and name.endswith('_initial') and isinstance(obj, types.FunctionType):
        setattr(Soul, name, staticmethod(obj))
    if name.startswith('restore_') and name.endswith('_initial') and isinstance(obj, types.FunctionType):
        setattr(Soul, name, staticmethod(obj))