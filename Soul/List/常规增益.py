from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log

def deploy_会心几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.会心几率.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.会心几率.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【会心几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_会心几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.会心几率.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.会心几率.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【会心几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_会心伤害_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.会心伤害.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.会心伤害.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【会心伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_会心伤害_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.会心伤害.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.会心伤害.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【会心伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_奇谋几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.奇谋几率.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.奇谋几率.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【奇谋几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_奇谋几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.奇谋几率.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.奇谋几率.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【奇谋几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_奇谋伤害_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.奇谋伤害.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.奇谋伤害.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【奇谋伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_奇谋伤害_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.奇谋伤害.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.奇谋伤害.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【奇谋伤害】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_破甲_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.破甲.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.破甲.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【破甲】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_破甲_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.破甲.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.破甲.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【破甲】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_看破_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.看破.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.看破.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【看破】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_看破_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.看破.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.看破.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【看破】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_倒戈_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.倒戈.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.倒戈.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【倒戈】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_倒戈_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.倒戈.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.倒戈.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【倒戈】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_攻心_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.攻心.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.攻心.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【攻心】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_攻心_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.攻心.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.攻心.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【攻心】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_连击几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.连击几率.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.连击几率.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【连击几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_连击几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.连击几率.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.连击几率.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【连击几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_反击几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.反击几率.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.反击几率.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【反击几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_反击几率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.反击几率.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.反击几率.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【反击几率】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def deploy_规避_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.规避.value)
    effectValue = soul.effectValue * (1 - cur_value)
    soul.effectValue = effectValue
    cur_value += effectValue
    setattr(hero, HeroInfoKey.规避.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【规避】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True

def restore_规避_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.规避.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.规避.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【规避】{}{:.2f}%({:.2f}%)'.format(heroName, show_upEffect_name, abs(soul.effectValue) * 100, cur_value * 100))
    return True
