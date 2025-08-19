from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log

def deploy_武力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.武力.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.武力.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【武力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def restore_武力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.武力.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.武力.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【武力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def deploy_智力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.智力.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.智力.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【智力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def restore_智力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.智力.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.智力.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【智力】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def deploy_统率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.统率.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.统率.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【统率】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def restore_统率_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.统率.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.统率.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【统率】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def deploy_先攻_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.先攻.value)
    cur_value += soul.effectValue
    setattr(hero, HeroInfoKey.先攻.value, cur_value)
    show_upEffect_name = '提升' if soul.effectValue > 0 else '降低'
    Log().battle_L2('[{}]的【先攻】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True

def restore_先攻_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.先攻.value)
    cur_value -= soul.effectValue
    setattr(hero, HeroInfoKey.先攻.value, cur_value)
    show_upEffect_name = '降低' if soul.effectValue > 0 else '提升'
    Log().battle_L2('[{}]的【先攻】{}{:.2f}({:.2f})'.format(heroName, show_upEffect_name, abs(soul.effectValue), cur_value))
    return True
