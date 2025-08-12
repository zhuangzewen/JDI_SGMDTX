from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
from Control.Log.JDI_Log import Log
from Soul.Enum.SoulSourceType_Enum import SoulSourceDetail
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime

def get_造成伤害(hero: Hero):
    造成伤害提升 = getattr(hero, HeroInfoKey.造成伤害提升.value)
    造成伤害降低 = getattr(hero, HeroInfoKey.造成伤害降低.value)
    return (造成伤害提升 + 造成伤害降低 - 1)

def deploy_造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成伤害提升.value, cur_value)
    show_upEffect_name = '【造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成伤害提升.value, cur_value)
    show_upEffect_name = '【造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_造成伤害降低_initial(soul: Any):
    print('[DEBUG] deploy_造成伤害降低_initial 被调用')
    hero = soul.target                                                                                  
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成伤害降低.value, cur_value)
    show_upEffect_name = '【造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成伤害降低.value, cur_value)
    show_upEffect_name = '【造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_对前排造成伤害(hero: Hero):
    对前排造成伤害提升 = getattr(hero, HeroInfoKey.对前排造成伤害提升.value)
    对前排造成伤害降低 = getattr(hero, HeroInfoKey.对前排造成伤害降低.value)
    return (对前排造成伤害提升 + 对前排造成伤害降低 - 1)

def deploy_对前排造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.对前排造成伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.对前排造成伤害提升.value, cur_value)
    show_upEffect_name = '【对前排造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_对前排造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_对前排造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.对前排造成伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.对前排造成伤害提升.value, cur_value)
    show_upEffect_name = '【对前排造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_对前排造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_对前排造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.对前排造成伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.对前排造成伤害降低.value, cur_value)
    show_upEffect_name = '【对前排造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_对前排造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_对前排造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.对前排造成伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.对前排造成伤害降低.value, cur_value)
    show_upEffect_name = '【对前排造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_对前排造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_造成谋略伤害(hero: Hero):
    造成谋略伤害提升 = getattr(hero, HeroInfoKey.造成谋略伤害提升.value)
    造成谋略伤害降低 = getattr(hero, HeroInfoKey.造成谋略伤害降低.value)
    return (造成谋略伤害提升 + 造成谋略伤害降低 - 1)

def deploy_造成谋略伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成谋略伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成谋略伤害提升.value, cur_value)
    show_upEffect_name = '【造成谋略伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成谋略伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成谋略伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成谋略伤害提升.value, cur_value)
    show_upEffect_name = '【造成谋略伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_造成谋略伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成谋略伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成谋略伤害降低.value, cur_value)
    show_upEffect_name = '【造成谋略伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成谋略伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成谋略伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成谋略伤害降低.value, cur_value)
    show_upEffect_name = '【造成谋略伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成谋略伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_造成兵刃伤害(hero: Hero):
    造成兵刃伤害提升 = getattr(hero, HeroInfoKey.造成兵刃伤害提升.value)
    造成兵刃伤害降低 = getattr(hero, HeroInfoKey.造成兵刃伤害降低.value)
    return (造成兵刃伤害提升 + 造成兵刃伤害降低 - 1)

def deploy_造成兵刃伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成兵刃伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成兵刃伤害提升.value, cur_value)
    show_upEffect_name = '【造成兵刃伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成兵刃伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成兵刃伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成兵刃伤害提升.value, cur_value)
    show_upEffect_name = '【造成兵刃伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_造成兵刃伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成兵刃伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.造成兵刃伤害降低.value, cur_value)
    show_upEffect_name = '【造成兵刃伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_造成兵刃伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.造成兵刃伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.造成兵刃伤害降低.value, cur_value)
    show_upEffect_name = '【造成兵刃伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_造成兵刃伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_普通攻击造成伤害(hero: Hero):
    普通攻击造成伤害提升 = getattr(hero, HeroInfoKey.普通攻击造成伤害提升.value)
    普通攻击造成伤害降低 = getattr(hero, HeroInfoKey.普通攻击造成伤害降低.value)
    return (普通攻击造成伤害提升 + 普通攻击造成伤害降低 - 1)

def deploy_普通攻击造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.普通攻击造成伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.普通攻击造成伤害提升.value, cur_value)
    show_upEffect_name = '【普通攻击造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_普通攻击造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_普通攻击造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.普通攻击造成伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.普通攻击造成伤害提升.value, cur_value)
    show_upEffect_name = '【普通攻击造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_普通攻击造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_普通攻击造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.普通攻击造成伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.普通攻击造成伤害降低.value, cur_value)
    show_upEffect_name = '【普通攻击造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_普通攻击造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_普通攻击造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.普通攻击造成伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.普通攻击造成伤害降低.value, cur_value)
    show_upEffect_name = '【普通攻击造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_普通攻击造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_主动战法造成伤害(hero: Hero):
    主动战法造成伤害提升 = getattr(hero, HeroInfoKey.主动战法造成伤害提升.value)
    主动战法造成伤害降低 = getattr(hero, HeroInfoKey.主动战法造成伤害降低.value)
    return 主动战法造成伤害提升 + 主动战法造成伤害降低 - 1

def deploy_主动战法造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.主动战法造成伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.主动战法造成伤害提升.value, cur_value)
    show_upEffect_name = '【主动战法造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_主动战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_主动战法造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.主动战法造成伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.主动战法造成伤害提升.value, cur_value)
    show_upEffect_name = '【主动战法造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_主动战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_主动战法造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.主动战法造成伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.主动战法造成伤害降低.value, cur_value)
    show_upEffect_name = '【主动战法造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_主动战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_主动战法造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.主动战法造成伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.主动战法造成伤害降低.value, cur_value)
    show_upEffect_name = '【主动战法造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_主动战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def get_追击战法造成伤害(hero: Hero):
    追击战法造成伤害提升 = getattr(hero, HeroInfoKey.追击战法造成伤害提升.value)
    追击战法造成伤害降低 = getattr(hero, HeroInfoKey.追击战法造成伤害降低.value)
    return (追击战法造成伤害提升 + 追击战法造成伤害降低 - 1)

def deploy_追击战法造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.追击战法造成伤害提升.value)
    effect_value = soul.effect_value
    if cur_value + effect_value > 2:
        effect_value = 2 - cur_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.追击战法造成伤害提升.value, cur_value)
    show_upEffect_name = '【追击战法造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_追击战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_追击战法造成伤害提升_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.追击战法造成伤害提升.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.追击战法造成伤害提升.value, cur_value)
    show_upEffect_name = '【追击战法造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_追击战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True

def deploy_追击战法造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.追击战法造成伤害降低.value)
    effect_value = soul.effect_value
    cur_value += effect_value
    setattr(hero, HeroInfoKey.追击战法造成伤害降低.value, cur_value)
    show_upEffect_name = '【追击战法造成伤害】降低'
    show_effectValue_name = '{:.2f}%'.format(abs(effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_追击战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    if SoulSourceDetail.负面状态效果 in soul.sourceDetail:
        soul.battleField.respond(status=SoulResponseTime.施加负面时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.被施加负面时, 时机响应武将=soul.target, 溯源SOUL=soul)
    return True
def restore_追击战法造成伤害降低_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    cur_value = getattr(hero, HeroInfoKey.追击战法造成伤害降低.value)
    cur_value -= soul.effect_value
    setattr(hero, HeroInfoKey.追击战法造成伤害降低.value, cur_value)
    show_upEffect_name = '【追击战法造成伤害】提升'
    show_effectValue_name = '{:.2f}%'.format(abs(soul.effect_value) * 100)
    show_curEffect_name = '{:.2f}%'.format(get_追击战法造成伤害(hero) * 100)
    Log().battle_L2('[{}]的{}{}({})'.format(heroName, show_upEffect_name, show_effectValue_name, show_curEffect_name))
    return True
