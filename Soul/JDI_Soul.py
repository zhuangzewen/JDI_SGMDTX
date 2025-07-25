
from Control.Log.JDI_Log import Log
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulSourceType_Enum import SoulSourceType
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from External.JDI_Skill import Skill
from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
from Generals.JDI_Hero import Hero
from Soul.Class.Damage_Class import Damage
from Calcu.JDI_Calculate import msg_移除响应

class Soul():
    # 目标 发起者 来源类型 技能 响应时机 持续回合 效果类型 效果值
    # 声明传入的类型 而不是any
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
                 battleField = None,
                 damage: Damage = None):
        self.target = target                # 目标
        self.initiator = initiator          # 发起者
        self.sourceType = sourceType        # 来源类型
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

        if self.effect_value > 0:
            show_upEffect_name = '提升'
        else:
            show_upEffect_name = '降低'

        from Soul.Enum.SoulEffectType_Enum import SoulEffectType
        if self.effect_type == SoulEffectType.造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.造成伤害提升.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.造成伤害提升.value, cur_value)
            Log().battle_L2('[{}]的【造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.对前排造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.对前排造成伤害提升.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.对前排造成伤害提升.value, cur_value)
            Log().battle_L2('[{}]的【对前排造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.受到伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到伤害降低.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.受到伤害降低.value, cur_value)
            Log().battle_L2('[{}]的【受到伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))
            if self.effect_value > 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.受到谋略伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到谋略伤害降低.value)
            real_value = (1 + cur_value) * self.effect_value
            cur_value += real_value
            setattr(self.target, HeroInfoKey.受到谋略伤害降低.value, cur_value)
            Log().battle_L2('[{}]的【受到谋略伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100,  cur_value * 100))

        elif self.effect_type == SoulEffectType.武力:
            cur_value = getattr(self.target, HeroInfoKey.武力.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.初始武力.value, cur_value)
            Log().battle_L2('[{}]的【武力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.智力:
            cur_value = getattr(self.target, HeroInfoKey.智力.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.智力.value, cur_value)
            Log().battle_L2('[{}]的【智力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.统帅:
            cur_value = getattr(self.target, HeroInfoKey.统帅.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.统帅.value, cur_value)
            Log().battle_L2('[{}]的【统帅】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.先攻:
            cur_value = getattr(self.target, HeroInfoKey.先攻.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.先攻.value, cur_value)
            Log().battle_L2('[{}]的【先攻】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:    
                self.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=self.initiator, 溯源SOUL=self)
                self.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=self.target, 溯源SOUL=self)

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

        elif self.effect_type == SoulEffectType.闪避几率:
            cur_value = getattr(self.target, HeroInfoKey.闪避几率.value)
            real_value = (1 - cur_value) * self.effect_value
            cur_value += real_value
            setattr(self.target, HeroInfoKey.闪避几率.value, cur_value)
            Log().battle_L2('[{}]的【闪避几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100, cur_value * 100))

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
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
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
            if self.effect_value < 0 and self.sourceType != SoulSourceType.异常状态效果_额外效果:
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

        elif self.effect_type == SoulEffectType.震慑:
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
                统帅soul = Soul(target=self.target, 
                                        sourceType=SoulSourceType.异常状态效果_额外效果, 
                                        skill=self.skill,
                                        effect_type=SoulEffectType.统帅, 
                                        effect_value=-20,
                                        source_soul=self)
                统帅soul.deploy_initial()
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
                                        sourceType=SoulSourceType.异常状态效果_额外效果, 
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
                                        sourceType=SoulSourceType.异常状态效果_额外效果, 
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
                                        sourceType=SoulSourceType.异常状态效果_额外效果, 
                                        skill=self.skill,
                                        effect_type=SoulEffectType.受到伤害, 
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
                            sourceType=SoulSourceType.异常状态效果_额外效果, 
                            skill=self.skill,
                            effect_type=SoulEffectType.会心伤害, 
                            effect_value=-0.15,
                            source_soul=self)
                会心伤害soul.deploy_initial()
                奇谋伤害soul = Soul(target=self.target, 
                            sourceType=SoulSourceType.异常状态效果_额外效果, 
                            skill=self.skill,
                            effect_type=SoulEffectType.奇谋伤害,
                            effect_value=-0.15,
                            source_soul=self)
                奇谋伤害soul.deploy_initial()
                Log().battle_L2('[{}]的[妖术]效果已施加'.format(heroName))
            self.battleField.respond(status=SoulResponseTime.施加异常时, 时机响应武将=self.initiator, 溯源SOUL=self)
            self.battleField.respond(status=SoulResponseTime.被施加异常时, 时机响应武将=self.target, 溯源SOUL=self)

        elif self.effect_type == SoulEffectType.损失兵力:

            伤害来源武将: Hero = self.initiator
            伤害来源武将名称 = 伤害来源武将.get_武将名称().value if 伤害来源武将 else '未知来源'
            伤害来源技能名称 = self.skill.get_战法名称().value if self.skill else '未知技能'
            伤害来源Soul效果 = self.damage.skillEffectName if self.damage else '未知效果来源'
            伤害数值 = int(self.effect_value)

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

        if self.effect_type == SoulEffectType.造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.造成伤害提升.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.造成伤害提升.value, cur_value)
            Log().battle_L2('[{}]的【造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.对前排造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.对前排造成伤害提升.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.对前排造成伤害提升.value, cur_value)
            Log().battle_L2('[{}]的【对前排造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.受到伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到伤害降低.value)
            ori_value = (cur_value - self.effect_value) / (self.effect_value + 1)
            real_value = cur_value - ori_value
            setattr(self.target, HeroInfoKey.受到伤害降低.value, ori_value)
            Log().battle_L2('[{}]的【受到伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100,  ori_value * 100))

        elif self.effect_type == SoulEffectType.受到谋略伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到谋略伤害降低.value)
            ori_value = (cur_value - self.effect_value) / (self.effect_value + 1)
            real_value = cur_value - ori_value
            setattr(self.target, HeroInfoKey.受到谋略伤害降低.value, ori_value)
            Log().battle_L2('[{}]的【受到谋略伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100,  ori_value * 100))

        elif self.effect_type == SoulEffectType.武力:
            cur_value = getattr(self.target, HeroInfoKey.武力.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.武力.value, cur_value)
            Log().battle_L2('[{}]的【武力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.智力:
            cur_value = getattr(self.target, HeroInfoKey.智力.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.智力.value, cur_value)
            Log().battle_L2('[{}]的【智力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.统帅:
            cur_value = getattr(self.target, HeroInfoKey.统帅.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.统帅.value, cur_value)
            Log().battle_L2('[{}]的【统帅】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.先攻:
            cur_value = getattr(self.target, HeroInfoKey.先攻.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.先攻.value, cur_value)
            Log().battle_L2('[{}]的【先攻】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.攻心:
            cur_value = getattr(self.target, HeroInfoKey.攻心.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.攻心.value, cur_value)
            Log().battle_L2('[{}]的【攻心】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.连击几率:
            cur_value = getattr(self.target, HeroInfoKey.连击几率.value)
            cur_value -= self.effect_value
            setattr(self.target, HeroInfoKey.连击几率.value, cur_value)
            Log().battle_L2('[{}]的【连击几率】{}{:.2f}%({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.闪避几率:
            cur_value = getattr(self.target, HeroInfoKey.闪避几率.value)
            ori_value = (cur_value - self.effect_value) / (1 - self.effect_value)
            real_value = cur_value - ori_value
            setattr(self.target, HeroInfoKey.闪避几率.value, ori_value)
            Log().battle_L2('[{}]的【闪避几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100, ori_value * 100))

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
            统帅soul = Soul(target=self.target, 
                                    sourceType=SoulSourceType.异常状态效果_额外效果, 
                                    skill=self.skill,
                                    effect_type=SoulEffectType.统帅, 
                                    effect_value=20,
                                    source_soul=self)
            统帅soul.deploy_initial()

        elif self.effect_type == SoulEffectType.火攻:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[火攻]效果已消失'.format(heroName))

            智力soul = Soul(target=self.target, 
                                    sourceType=SoulSourceType.异常状态效果_额外效果, 
                                    skill=self.skill,
                                    effect_type=SoulEffectType.智力, 
                                    effect_value=15,
                                    source_soul=self)
            智力soul.deploy_initial()

        elif self.effect_type == SoulEffectType.风暴:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[风暴]效果已消失'.format(heroName))

            先攻soul = Soul(target=self.target, 
                                    sourceType=SoulSourceType.异常状态效果_额外效果, 
                                    skill=self.skill,
                                    effect_type=SoulEffectType.先攻, 
                                    effect_value=30,
                                    source_soul=self)
            先攻soul.deploy_initial()

        elif self.effect_type == SoulEffectType.畏惧:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[畏惧]效果已消失'.format(heroName))

            受到伤害soul = Soul(target=self.target, 
                                    sourceType=SoulSourceType.异常状态效果_额外效果, 
                                    skill=self.skill,
                                    effect_type=SoulEffectType.受到伤害, 
                                    effect_value=-0.1,
                                    source_soul=self)
            受到伤害soul.deploy_initial()

        elif self.effect_type == SoulEffectType.妖术:
            msg_移除响应(self)
            Log().battle_L2('[{}]的[妖术]效果已消失'.format(heroName))

            会心伤害soul = Soul(target=self.target,
                        sourceType=SoulSourceType.异常状态效果_额外效果,
                        skill=self.skill,
                        effect_type=SoulEffectType.会心伤害, 
                        effect_value=0.15,
                        source_soul=self)
            会心伤害soul.deploy_initial()
            奇谋伤害soul = Soul(target=self.target, 
                        sourceType=SoulSourceType.异常状态效果_额外效果, 
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
