from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log

def deploy_固定受击率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    value = soul.effect_value
    setattr(hero, HeroInfoKey.固定受击率.value, True)
    Log().battle_L2(f'[{heroName}]的【固定受击率】提升为{value * 100:.2f}%')
    return True

def restore_固定受击率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    value = 0
    setattr(hero, HeroInfoKey.固定受击率.value, False)
    Log().battle_L2(f'[{heroName}]的【固定受击率】降低为{value * 100:.2f}%')
    return True

def deploy_受治疗效果_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    value = soul.effect_value
    cur_value = getattr(hero, HeroInfoKey.受治疗效果.value)
    cur_value += value
    setattr(hero, HeroInfoKey.受治疗效果.value, cur_value)
    show_upEffect_name = '提升' if value > 0 else '降低'
    Log().battle_L2('[{}]的【受治疗效果】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(value) * 100, cur_value * 100))
    return True

def restore_受治疗效果_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    value = soul.effect_value
    cur_value = getattr(hero, HeroInfoKey.受治疗效果.value)
    cur_value -= value
    setattr(hero, HeroInfoKey.受治疗效果.value, cur_value)
    show_upEffect_name = '降低' if value > 0 else '提升'
    Log().battle_L2('[{}]的【受治疗效果】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(value) * 100, cur_value * 100))
    return True
