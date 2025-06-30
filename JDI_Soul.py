
from JDI_Log import Log
from JDI_Enum import HeroInfoKey, SoulSourceType, SoulResponseTime, SoulEffectType
from JDI_Skill import Skill
from JDI_Hero import Hero


class Soul():
    # 目标 发起者 来源类型 技能 响应时机 持续回合 效果类型 效果值
    # 声明传入的类型 而不是any
    def __init__(self, 
                 target: Hero, 
                 initiator: Hero = None, 
                 sourceType: SoulSourceType = SoulSourceType.不溯源, 
                 skill: Skill = None, 
                 response_time: SoulResponseTime = SoulResponseTime.None_Response, 
                 duration: int = -1, 
                 effect_type: SoulEffectType = SoulEffectType.无影响, 
                 effect_value: float = 0):
        self.target = target                # 目标
        self.initiator = initiator          # 发起者
        self.sourceType = sourceType        # 来源类型
        self.skill = skill                  # 技能
        self.response_time = response_time  # 响应时机
        self.duration = duration            # 持续回合
        self.effect_type = effect_type      # 效果类型
        self.effect_value = effect_value    # 效果值

    def deploy_initial(self):

        heroInfo = getattr(self.target, HeroInfoKey.武将信息.value)
        heroName = getattr(heroInfo, HeroInfoKey.武将名称.value).value
        
        if self.effect_value > 0:
            show_upEffect_name = '提升'
        else:
            show_upEffect_name = '降低'

        if self.effect_type == SoulEffectType.造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.造成伤害提升.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.造成伤害提升.value, cur_value)
            Log().show_battle_info('        [{}]的【造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.对前排造成伤害:
            cur_value = getattr(self.target, HeroInfoKey.对前排造成伤害提升.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.对前排造成伤害提升.value, cur_value)
            Log().show_battle_info('        [{}]的【对前排造成伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.受到伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到伤害降低.value)
            real_value = (1 + cur_value) * self.effect_value
            cur_value += real_value
            setattr(self.target, HeroInfoKey.受到伤害降低.value, cur_value)
            Log().show_battle_info('        [{}]的【受到伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100,  cur_value * 100))

        elif self.effect_type == SoulEffectType.受到谋略伤害:
            cur_value = getattr(self.target, HeroInfoKey.受到谋略伤害降低.value)
            real_value = (1 + cur_value) * self.effect_value
            cur_value += real_value
            setattr(self.target, HeroInfoKey.受到谋略伤害降低.value, cur_value)
            Log().show_battle_info('        [{}]的【受到谋略伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100,  cur_value * 100))

        elif self.effect_type == SoulEffectType.武力:
            cur_value = getattr(self.target, HeroInfoKey.武力.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.初始武力.value, cur_value)
            Log().show_battle_info('        [{}]的【武力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.智力:
            cur_value = getattr(self.target, HeroInfoKey.智力.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.智力.value, cur_value)
            Log().show_battle_info('        [{}]的【智力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.统帅:
            cur_value = getattr(self.target, HeroInfoKey.统帅.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.统帅.value, cur_value)
            Log().show_battle_info('        [{}]的【统帅】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.先攻:
            cur_value = getattr(self.target, HeroInfoKey.先攻.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.先攻.value, cur_value)
            Log().show_battle_info('        [{}]的【先攻】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value), cur_value))

        elif self.effect_type == SoulEffectType.连击:
            cur_value = getattr(self.target, HeroInfoKey.连击几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.连击几率.value, cur_value)
            Log().show_battle_info('        [{}]的【连击几率】{}{:.2f}%({:.2f})'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.闪避:
            cur_value = getattr(self.target, HeroInfoKey.闪避几率.value)
            real_value = (1 - cur_value) + self.effect_value
            cur_value += real_value
            setattr(self.target, HeroInfoKey.闪避几率.value, cur_value)
            Log().show_battle_info('        [{}]的【闪避几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(real_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.会心:
            cur_value = getattr(self.target, HeroInfoKey.会心几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.会心几率.value, cur_value)
            Log().show_battle_info('        [{}]的【会心几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.奇谋:
            cur_value = getattr(self.target, HeroInfoKey.奇谋几率.value)
            cur_value += self.effect_value
            setattr(self.target, HeroInfoKey.奇谋几率.value, cur_value)
            Log().show_battle_info('        [{}]的【奇谋几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(self.effect_value) * 100, cur_value * 100))

        elif self.effect_type == SoulEffectType.固定受击率:
            setattr(self.target, HeroInfoKey.固定受击率.value, True)
            Log().show_battle_info('        [{}]的【固定受击率】提升为{:.2f}%'.format(heroName, self.effect_value * 100))

        elif self.effect_type == SoulEffectType.借刀_星罗棋布_双前排阵型:
            Log().show_battle_info('        [{}]的【星罗棋布-双前排阵型】效果已施加'.format(heroName))

        elif self.effect_type == SoulEffectType.借刀_星罗棋布_三前排阵型:
            Log().show_battle_info('        [{}]的【星罗棋布-三前排阵型】效果已施加'.format(heroName))
