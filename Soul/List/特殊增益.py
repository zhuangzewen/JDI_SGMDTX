from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log

def deploy_清醒_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.清醒.value, True)
    Log().battle_L2('[{}]的【清醒】效果已施加'.format(heroName))
    return True

def restore_清醒_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.清醒.value, False)
    Log().battle_L2('[{}]的【清醒】效果已消失'.format(heroName))
    return True

def deploy_抵御_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.抵御.value)
    if cur_value == 2:
        Log().battle_L2('[{}]的「抵御」效果已刷新'.format(heroName))
        return
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.抵御.value, cur_value)
    Log().battle_L2('[{}]的【抵御次数】{}{}({})'.format(heroName, '提升' if soul.effectValue > 0 else '降低', abs(soul.effectValue), cur_value))
    Log().battle_L2('[{}]的「抵御」效果已施加'.format(heroName))
    return True

def restore_抵御_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.抵御.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.抵御.value, cur_value)
    Log().battle_L2('[{}]的【抵御次数】{}{}({})'.format(heroName, '降低' if soul.effectValue > 0 else '提升', abs(soul.effectValue), cur_value))
    Log().battle_L2('[{}]的「抵御」效果已消失'.format(heroName))
    return True

def deploy_必中_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.必中.value, True)
    Log().battle_L2('[{}]的【必中】效果已施加'.format(heroName))
    return True

def restore_必中_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.必中.value, False)
    Log().battle_L2('[{}]的【必中】效果已消失'.format(heroName))
    return True

def deploy_破御_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.破御.value, True)
    Log().battle_L2('[{}]的【破御】效果已施加'.format(heroName))
    return True

def restore_破御_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    setattr(hero, HeroInfoKey.破御.value, False)
    Log().battle_L2('[{}]的【破御】效果已消失'.format(heroName))
    return True
