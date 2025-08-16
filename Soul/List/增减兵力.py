from typing import Any
from Generals.JDI_Hero import Hero
from Generals.Enum.Generals_Enum import HeroInfoKey
from Control.Log.JDI_Log import Log
from Soul.Enum.SoulResponseTime_Enum import SoulResponseTime
from Soul.Enum.SoulEffectType_Enum import SoulEffectType
import random

def deploy_损失兵力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value

    伤害来源武将: Hero = soul.initiator
    伤害来源武将名称 = 伤害来源武将.get_武将名称().value if 伤害来源武将 else '未知来源'
    伤害来源技能名称 = soul.skill.get_战法名称().value if soul.skill else '未知技能'
    伤害来源Soul效果 = soul.damage.skillEffectName if soul.damage else '未知效果来源'
    伤害数值 = int(soul.effect_value)

    # battlefield 响应
    if hasattr(soul, 'battleField') and soul.battleField:
        soul.battleField.respond(status=SoulResponseTime.受到伤害前, 时机响应武将=hero, 溯源SOUL=soul)
    # 闪避判断
    if hasattr(soul, 'initiator') and soul.initiator and hero.get_规避() > 0:
        if random.random() < hero.get_规避():
            Log().battle_L2(f'[{heroName}]成功规避[{soul.initiator.get_武将名称().value}]的伤害')
            if hasattr(soul, 'battleField') and soul.battleField:
                soul.battleField.respond(status=SoulResponseTime.规避伤害时, 时机响应武将=hero, 溯源SOUL=soul)
            return True
    # 抵御判定
    剩余抵御次数 = hero.get_抵御()
    if 剩余抵御次数 > 0:
        抵御减伤 = random.randint(70, 90) / 100
        Log().battle_L2('[{}]消耗一次抵御机会,此次伤害减少{:.2f}%'.format(heroName, 抵御减伤 * 100))
        Log().battle_L2('[{}]的【抵御次数】降低1({})'.format(heroName, 剩余抵御次数 - 1))
        setattr(hero, HeroInfoKey.抵御.value, 剩余抵御次数 - 1)
        伤害数值 = int(伤害数值 * (1 - 抵御减伤))
    # 兵力减少逻辑
    cur兵力 = hero.get_兵力()
    损失兵力 = abs(伤害数值)
    if cur兵力 < 损失兵力:
        损失兵力 = cur兵力
    剩余兵力 = cur兵力 - 损失兵力
    # 伤兵与亖兵
    伤兵数值 = int(损失兵力 * 0.8)
    亖兵数值 = int(损失兵力 - 伤兵数值)
    setattr(hero, HeroInfoKey.伤兵.value, hero.get_伤兵() + 伤兵数值)
    setattr(hero, HeroInfoKey.亖兵.value, hero.get_亖兵() + 亖兵数值)
    setattr(hero, HeroInfoKey.兵力.value, 剩余兵力)

    from External.Fitting.Enum.FittingList_Enum import Fitting_List_Enum
    if (soul.skill and soul.skill.get_战法名称() == Fitting_List_Enum.普攻):
        Log().battle_L2('[{}]损失了兵力{}({})'.format(heroName, abs(伤害数值), 剩余兵力))
    else:
        if 伤害来源Soul效果 == '':
            Log().battle_L2(f'[{heroName}]由于[{伤害来源武将名称}]的【{伤害来源技能名称}】的伤害,损失了兵力{abs(伤害数值)}({剩余兵力})')
        else :
            Log().battle_L2(f'[{heroName}]由于[{伤害来源武将名称}]【{伤害来源技能名称}】的[{伤害来源Soul效果}]效果,损失了兵力{abs(伤害数值)}({剩余兵力})')

    # 兵力为0响应
    if 剩余兵力 <= 0 and hasattr(soul, 'battleField') and soul.battleField:
        Log().battle_L2('[{}]兵力为0 无法再战'.format(heroName))
        soul.battleField.respond(status=SoulResponseTime.武将溃败, 时机响应武将=hero)
    # 造成/受到伤害响应
    if hasattr(soul, 'battleField') and soul.battleField and hasattr(soul, 'initiator'):
        soul.battleField.respond(status=SoulResponseTime.造成伤害时, 时机响应武将=soul.initiator, 溯源SOUL=soul)
        soul.battleField.respond(status=SoulResponseTime.受到伤害时, 时机响应武将=hero, 溯源SOUL=soul)
    return True

def restore_损失兵力_initial(soul: Any):
    return True

def deploy_恢复兵力_initial(soul: Any):
    hero = soul.target
    heroName = hero.get_武将名称().value
    value = int(soul.effect_value)
    # battlefield 响应
    if hasattr(soul, 'battleField') and soul.battleField:
        soul.battleField.respond(status=SoulResponseTime.受到伤害前, 时机响应武将=hero, 溯源SOUL=soul)
    # 断粮判定
    恢复兵力 = value
    if hasattr(hero, 'get_响应Soul列表'):
        for s in hero.get_响应Soul列表():
            from Soul.Enum.SoulEffectType_Enum import SoulEffectType
            if hasattr(s, 'effect_type') and s.effect_type == SoulEffectType.断粮:
                Log().battle_L2('[{}]由于[{}]【{}】的[断粮]效果治疗效率降为30%'.format(heroName, s.initiator.get_武将名称().value, s.skill.get_战法名称().value))
                恢复兵力 = int(恢复兵力 * 0.3)
                break
    当前兵力 = hero.get_兵力()
    当前伤兵 = hero.get_伤兵()
    if 恢复兵力 <= 当前伤兵:
        剩余伤兵 = 当前伤兵 - 恢复兵力
        实际兵力 = 当前兵力 + 恢复兵力
        setattr(hero, HeroInfoKey.伤兵.value, 剩余伤兵)
        setattr(hero, HeroInfoKey.兵力.value, 实际兵力)
    else:
        恢复兵力 = 当前伤兵
        剩余伤兵 = 0
        实际兵力 = 当前兵力 + 恢复兵力
        setattr(hero, HeroInfoKey.伤兵.value, 剩余伤兵)
        setattr(hero, HeroInfoKey.兵力.value, 实际兵力)
    Log().battle_L2('[{}]恢复了兵力{}({})'.format(heroName, 恢复兵力, hero.get_兵力()))
    return True

def restore_恢复兵力_initial(soul: Any):
    return True

