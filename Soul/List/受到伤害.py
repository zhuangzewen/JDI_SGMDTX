from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime

def get_受到伤害(hero: Hero):
    受到伤害提升 = getattr(hero, HeroInfoKey.受到伤害提升.value)
    受到伤害降低 = getattr(hero, HeroInfoKey.受到伤害降低.value)
    return (受到伤害提升 + 受到伤害降低 - 1)

def deploy_受到伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害提升.value, cur_value)
    show_upEffect_name = '【受到伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True
def restore_受到伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到伤害提升.value, cur_value)
    show_upEffect_name = '【受到伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到伤害降低_initial(soul: Any):
    print('[DEBUG] deploy_受到伤害降低_initial 被调用')
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害降低.value, cur_value)
    show_upEffect_name = '【受到伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True
def restore_受到伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到伤害降低.value, cur_value)
    show_upEffect_name = '【受到伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到伤害提升固定值_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害提升.value)
    effect_value = soul.effect_value  # 固定值直接加
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害提升.value, cur_value)
    show_upEffect_name = '【受到伤害】提升(固定值)'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到伤害提升固定值_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到伤害提升.value, cur_value)
    show_upEffect_name = '【受到伤害】降低(固定值)'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到伤害降低固定值_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害降低.value)
    effect_value = soul.effect_value  # 固定值直接加
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到伤害降低.value, cur_value)
    show_upEffect_name = '【受到伤害】降低(固定值)'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到伤害降低固定值_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到伤害降低.value, cur_value)
    show_upEffect_name = '【受到伤害】提升(固定值)'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到异性伤害(hero: Hero):
    受到异性伤害提升 = getattr(hero, HeroInfoKey.受到异性伤害提升.value)
    受到异性伤害降低 = getattr(hero, HeroInfoKey.受到异性伤害降低.value)
    return (受到异性伤害提升 + 受到异性伤害降低 - 1)

def deploy_受到异性伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到异性伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到异性伤害提升.value, cur_value)
    show_upEffect_name = '【受到异性伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到异性伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到异性伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到异性伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到异性伤害提升.value, cur_value)
    show_upEffect_name = '【受到异性伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到异性伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到异性伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到异性伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到异性伤害降低.value, cur_value)
    show_upEffect_name = '【受到异性伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到异性伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到异性伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到异性伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到异性伤害降低.value, cur_value)
    show_upEffect_name = '【受到异性伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到异性伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到谋略伤害(hero: Hero):
    受到谋略伤害提升 = getattr(hero, HeroInfoKey.受到谋略伤害提升.value)
    受到谋略伤害降低 = getattr(hero, HeroInfoKey.受到谋略伤害降低.value)
    return (受到谋略伤害提升 + 受到谋略伤害降低 - 1)

def deploy_受到谋略伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到谋略伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到谋略伤害提升.value, cur_value)
    show_upEffect_name = '【受到谋略伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到谋略伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到谋略伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到谋略伤害提升.value, cur_value)
    show_upEffect_name = '【受到谋略伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到谋略伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到谋略伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到谋略伤害降低.value, cur_value)
    show_upEffect_name = '【受到谋略伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到谋略伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到谋略伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到谋略伤害降低.value, cur_value)
    show_upEffect_name = '【受到谋略伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到兵刃伤害(hero: Hero):
    受到兵刃伤害提升 = getattr(hero, HeroInfoKey.受到兵刃伤害提升.value)
    受到兵刃伤害降低 = getattr(hero, HeroInfoKey.受到兵刃伤害降低.value)
    return (受到兵刃伤害提升 + 受到兵刃伤害降低 - 1)

def deploy_受到兵刃伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到兵刃伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到兵刃伤害提升.value, cur_value)
    show_upEffect_name = '【受到兵刃伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True


def restore_受到兵刃伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到兵刃伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到兵刃伤害提升.value, cur_value)
    show_upEffect_name = '【受到兵刃伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到兵刃伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到兵刃伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到兵刃伤害降低.value, cur_value)
    show_upEffect_name = '【受到兵刃伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到兵刃伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到兵刃伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到兵刃伤害降低.value, cur_value)
    show_upEffect_name = '【受到兵刃伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到普通攻击伤害(hero: Hero):
    受到普通攻击伤害提升 = getattr(hero, HeroInfoKey.受到普通攻击伤害提升.value)
    受到普通攻击伤害降低 = getattr(hero, HeroInfoKey.受到普通攻击伤害降低.value)
    return (受到普通攻击伤害提升 + 受到普通攻击伤害降低 - 1)

def deploy_受到普通攻击伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到普通攻击伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到普通攻击伤害提升.value, cur_value)
    show_upEffect_name = '【受到普通攻击伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到普通攻击伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到普通攻击伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到普通攻击伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到普通攻击伤害提升.value, cur_value)
    show_upEffect_name = '【受到普通攻击伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到普通攻击伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到普通攻击伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到普通攻击伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到普通攻击伤害降低.value, cur_value)
    show_upEffect_name = '【受到普通攻击伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到普通攻击伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到普通攻击伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到普通攻击伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到普通攻击伤害降低.value, cur_value)
    show_upEffect_name = '【受到普通攻击伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到普通攻击伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到主动战法伤害(hero: Hero):
    受到主动战法伤害提升 = getattr(hero, HeroInfoKey.受到主动战法伤害提升.value)
    受到主动战法伤害降低 = getattr(hero, HeroInfoKey.受到主动战法伤害降低.value)
    return (受到主动战法伤害提升 + 受到主动战法伤害降低 - 1)

def deploy_受到主动战法伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到主动战法伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到主动战法伤害提升.value, cur_value)
    show_upEffect_name = '【受到主动战法伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到主动战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到主动战法伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到主动战法伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到主动战法伤害提升.value, cur_value)
    show_upEffect_name = '【受到主动战法伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到主动战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到主动战法伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到主动战法伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到主动战法伤害降低.value, cur_value)
    show_upEffect_name = '【受到主动战法伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到主动战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到主动战法伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到主动战法伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到主动战法伤害降低.value, cur_value)
    show_upEffect_name = '【受到主动战法伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到主动战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_受到追击战法伤害(hero: Hero):
    受到追击战法伤害提升 = getattr(hero, HeroInfoKey.受到追击战法伤害提升.value)
    受到追击战法伤害降低 = getattr(hero, HeroInfoKey.受到追击战法伤害降低.value)
    return (受到追击战法伤害提升 + 受到追击战法伤害降低 - 1)

def deploy_受到追击战法伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到追击战法伤害提升.value)
    effect_value = soul.effect_value * (2 - cur_value)
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到追击战法伤害提升.value, cur_value)
    show_upEffect_name = '【受到追击战法伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到追击战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到追击战法伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到追击战法伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到追击战法伤害提升.value, cur_value)
    show_upEffect_name = '【受到追击战法伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到追击战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_受到追击战法伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到追击战法伤害降低.value)
    effect_value = (1 + cur_value) * soul.effect_value
    soul.effect_value = effect_value  # Store the calculated effect value for later use
    cur_value += effect_value
    setattr(hero, HeroInfoKey.受到追击战法伤害降低.value, cur_value)
    show_upEffect_name = '【受到追击战法伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到追击战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    # respond逻辑已移除，主流程统一控制
    return True
def restore_受到追击战法伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.受到追击战法伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.受到追击战法伤害降低.value, cur_value)
    show_upEffect_name = '【受到追击战法伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_受到追击战法伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True