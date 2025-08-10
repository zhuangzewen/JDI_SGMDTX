from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Control.Log.JDI_Log import Log
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime


def deploy_受到伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害提升.value, cur_value)
    show_upEffect_name = '【受到伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(cur_value * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True

def deploy_受到伤害降低_initial(soul: Any):
    print('[DEBUG] deploy_受到伤害降低_initial 被调用')
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害降低.value, cur_value)
    show_upEffect_name = '【受到伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(cur_value * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True