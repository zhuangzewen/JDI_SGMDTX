
from JDI_Log import Log
from JDI_RanVal import *
import math
from JDI_Enum import DamageType, SkillType, WeaponType

def msg_过滤掉被击溃的武将(heroes):
    from JDI_Hero import Hero
    from JDI_Enum import HeroInfoKey

    heroes: list[Hero]

    result = []
    for hero in heroes:
        if getattr(hero, HeroInfoKey.被击溃状态.value) == False:
            result.append(hero)
    return result

def msg_判断己方前排武将数量(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()
    owner = skill.get_持有者()

    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        heroes = [team1.firstHero, team1.secondHero, team1.thirdHero]
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        heroes = [team2.firstHero, team2.secondHero, team2.thirdHero]

    length = 0
    for hero in heroes:
        if not hero.get_被击溃状态() and hero.get_前排状态():
            length += 1
    return length

def msg_对我方的单前排生效(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()
    owner = skill.get_持有者()

    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        heroes = [team1.firstHero, team1.secondHero, team1.thirdHero]
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        heroes = [team2.firstHero, team2.secondHero, team2.thirdHero]

    for hero in heroes:
        if not hero.get_被击溃状态() and hero.get_前排状态():
            return hero

    return None

def msg_对我方统帅最低的武将(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()
    owner = skill.get_持有者()

    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        heroes = [team1.firstHero, team1.secondHero, team1.thirdHero]
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        heroes = [team2.firstHero, team2.secondHero, team2.thirdHero]

    lowest_ts_hero = None
    for hero in heroes:
        if not hero.get_被击溃状态() and lowest_ts_hero == None:
            lowest_ts_hero = hero

        elif not hero.get_被击溃状态() and hero.get_统帅() < lowest_ts_hero.get_统帅():
            lowest_ts_hero = hero

    return lowest_ts_hero

def msg_对我方智力最高的武将(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()
    owner = skill.get_持有者()

    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        heroes = [team1.firstHero, team1.secondHero, team1.thirdHero]
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        heroes = [team2.firstHero, team2.secondHero, team2.thirdHero]

    highest_zl_hero = None
    for hero in heroes:
        if not hero.get_被击溃状态() and highest_zl_hero == None:
            highest_zl_hero = hero

        elif not hero.get_被击溃状态() and hero.get_智力() > highest_zl_hero.get_智力():
            highest_zl_hero = hero

    return highest_zl_hero

def 对己方所有目标生效(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField

    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()

    owner = skill.get_持有者()
    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        return msg_过滤掉被击溃的武将([team1.firstHero, team1.secondHero, team1.thirdHero])
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        return msg_过滤掉被击溃的武将([team2.firstHero, team2.secondHero, team2.thirdHero])

def 对己方阵型强化SOUL生效(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team
    from JDI_Soul import Soul, SoulSourceType

    skill: Skill
    battleField: BattleField
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()
    owner = skill.get_持有者()

    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        heroes = [team1.firstHero, team1.secondHero, team1.thirdHero]
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        heroes = [team2.firstHero, team2.secondHero, team2.thirdHero]

    # 返回新数组
    check_list = []
    for soul in battleField.getSoulList():
        soul: Soul
        if soul.sourceType == SoulSourceType.阵型加成 and soul.target in heroes and soul.target.get_被击溃状态() == False:
            check_list.append(soul)
    return check_list

def 实际受击率(hero):

    # 兵力影响受击率 
    from JDI_Hero import Hero
    hero: Hero
    
    # 先判断固定受击率
    if hero.get_固定受击率() != 0:
        return hero.get_固定受击率()
    
    # 获取受击率 是否为 0.6
    if hero.get_受击率() != 0.6:
        return hero.get_受击率()
    
    # 受击率 = -7.5e-9 * 兵力^2 + 0.0001625 * 兵力 - 0.275
    if hero.get_受击率() == 0.6:
        return -7.5e-9 * hero.get_兵力() ** 2 + 0.0001625 * hero.get_兵力() - 0.275
    
    return 0

def 从队列确定受击武将(heroList):
    from JDI_Hero import Hero
    heroList: list[Hero]

    # 创建受击率数组
    hit_rate_list = []
    for hero in heroList:
        hero: Hero
        hit_rate = 实际受击率(hero)
        hit_rate_list.append(hit_rate)

    randomInt = 根据受击率列表随机一个敌方(hit_rate_list)
    return heroList[randomInt]

def 对敌方所有目标生效(skill, battleField):
    from JDI_Skill import Skill
    from JDI_BattleField import BattleField
    from JDI_Team import Team

    skill: Skill
    battleField: BattleField

    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()

    owner = skill.get_持有者()
    if owner in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        return msg_过滤掉被击溃的武将([team2.firstHero, team2.secondHero, team2.thirdHero])
    elif owner in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        return msg_过滤掉被击溃的武将([team1.firstHero, team1.secondHero, team1.thirdHero])

def 武将行动队列(battleField):
    from JDI_BattleField import BattleField
    from JDI_Team import Team
    from JDI_Hero import Hero
    from JDI_Enum import HeroInfoKey

    battleField: BattleField
    
    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()

    def msg_获取队伍中先攻最高的武将(team: Team):
        fastest_hero = None
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if getattr(hero, HeroInfoKey.被击溃状态.value) == True or getattr(hero, HeroInfoKey.已行动状态.value) == True:
                continue
            if fastest_hero == None:
                fastest_hero = hero
            elif getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.先攻.value) > getattr(fastest_hero, HeroInfoKey.先攻.value):
                fastest_hero = hero
        return fastest_hero

    def msg_检索未行动武将():
        for hero in team1.firstHero, team1.secondHero, team1.thirdHero, team2.firstHero, team2.secondHero, team2.thirdHero :
            if getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.已行动状态.value) == False:
                return True
        return False

    def msg_两队先攻对比(hero1, hero2):

        from JDI_RanVal import 获取对比行动优先级

        hero1_xg = getattr(hero1, HeroInfoKey.先攻.value)
        hero2_xg = getattr(hero2, HeroInfoKey.先攻.value)
        
        if 获取对比行动优先级(hero1_xg, hero2_xg):
            return hero1
        else:
            return hero2

    def msg_重置武将行动状态():
        for hero in team1.firstHero, team1.secondHero, team1.thirdHero, \
                    team2.firstHero, team2.secondHero, team2.thirdHero:
            hero: Hero
            setattr(hero, HeroInfoKey.已行动状态.value, False)


    msg_重置武将行动状态()
    order_list = []
    while msg_检索未行动武将() == True:
        get_fast_team1 = msg_获取队伍中先攻最高的武将(team1)
        get_fast_team2 = msg_获取队伍中先攻最高的武将(team2)

        if get_fast_team1 != None and get_fast_team2 != None:
            check_fast = msg_两队先攻对比(get_fast_team1, get_fast_team2)
        elif get_fast_team1 != None:
            check_fast = get_fast_team1
        elif get_fast_team2 != None:
            check_fast = get_fast_team2
        setattr(check_fast, HeroInfoKey.已行动状态.value, True)
        order_list.append(check_fast)
    msg_重置武将行动状态()
    return order_list

def 获取武将所在的队伍(battleField, hero):
    from JDI_Team import Team
    from JDI_Hero import Hero
    from JDI_BattleField import BattleField

    battleField: BattleField
    hero: Hero

    team1: Team = battleField.getTeam1()
    team2: Team = battleField.getTeam2()

    if hero in [team1.firstHero, team1.secondHero, team1.thirdHero]:
        return team1
    elif hero in [team2.firstHero, team2.secondHero, team2.thirdHero]:
        return team2

def MSG_确定伤害类型(攻击者, 伤害类型):
    from JDI_Enum import DamageType
    from JDI_Hero import Hero

    攻击者: Hero
    确定伤害类型:DamageType = 伤害类型
    if 确定伤害类型 == DamageType.择优:
        wuli = 攻击者.get_武力()
        zhiLi = 攻击者.get_智力()
        if wuli >= zhiLi:
            确定伤害类型 = DamageType.兵刃
        else:
            确定伤害类型 = DamageType.谋略

    return 确定伤害类型

def MSG_兵力伤害公式(兵力: int):
    value_health = 1 + 0.2 * math.log10(兵力 / 10000)
    Log().show_debug_info('DEBUG------- 兵力伤害公式: {:.4f}'.format(value_health))
    return value_health

def MSG_武将伤害公式(攻击者, 防御者, 伤害类型: DamageType, 伤害值):

    if 伤害类型 == DamageType.谋略:
        攻方数值 = 攻击者.get_智力()
        防方数值 = (防御者.get_统帅() + 防御者.get_智力()) * 0.5
    elif 伤害类型 == DamageType.兵刃:
        攻方数值 = 攻击者.get_武力()
        防方数值 = 防御者.get_统帅()
    elif 伤害类型 == DamageType.逃兵:
        攻方数值 = 1
        防方数值 = 1
    elif 伤害类型 == DamageType.择优:
        wuli = 攻击者.get_武力()
        zhiLi = 攻击者.get_智力()
        if wuli > zhiLi:
            攻方数值 = wuli
            防方数值 = 防御者.get_统帅()
        else:
            攻方数值 = zhiLi
            防方数值 = (防御者.get_统帅() + 防御者.get_智力()) * 0.5

    p0=2.5279e+02
    p1=1.4024e+00
    p2=-1.3346e+00
    p3=7.4124e-04
    p4= -2.9490e-03
    p5=2.3750e-03

    attaValue = p0 + p1 * 攻方数值 + p2 * 防方数值 + p3 * 攻方数值 ** 2 + p4 * 攻方数值 * 防方数值 + p5 * 防方数值 ** 2
    Log().show_debug_info('DEBUG------- 攻方数值: {:.4f}, 防方数值: {:.4f}, 计算结果: {:.4f}'.format(攻方数值, 防方数值, attaValue))

    return attaValue

def MSG_兵种增伤公式(攻击者, 防御者):
    from JDI_Hero import Hero
    攻击者: Hero
    防御者: Hero

    攻击方兵种: WeaponType = 攻击者.get_武将兵种()
    防御方兵种: WeaponType = 防御者.get_武将兵种()

    增伤系数 = 0

    # 兵种克制关系为 盾克制弓，弓克制枪，枪克制骑，骑克制盾
    if (攻击方兵种 == WeaponType.盾 and 防御方兵种 == WeaponType.弓) or \
       (攻击方兵种 == WeaponType.弓 and 防御方兵种 == WeaponType.枪) or \
       (攻击方兵种 == WeaponType.枪 and 防御方兵种 == WeaponType.骑) or \
       (攻击方兵种 == WeaponType.骑 and 防御方兵种 == WeaponType.盾):
        增伤系数 = 0.15

    return 增伤系数

def MSG_兵种减伤公式(攻击者, 防御者):
    from JDI_Hero import Hero
    攻击者: Hero
    防御者: Hero

    攻击方兵种: WeaponType = 攻击者.get_武将兵种()
    防御方兵种: WeaponType = 防御者.get_武将兵种()

    减伤系数 = 0

    # 兵种克制关系为 盾克制弓，弓克制枪，枪克制骑，骑克制盾
    if (防御方兵种 == WeaponType.盾 and 攻击方兵种 == WeaponType.弓) or \
       (防御方兵种 == WeaponType.弓 and 攻击方兵种 == WeaponType.枪) or \
       (防御方兵种 == WeaponType.枪 and 攻击方兵种 == WeaponType.骑) or \
       (防御方兵种 == WeaponType.骑 and 攻击方兵种 == WeaponType.盾):
        减伤系数 = -0.15

    return 减伤系数

def MSG_武将增减伤公式(攻击者, 防御者, 伤害类型: DamageType, 战法类型: SkillType):
    from JDI_Hero import Hero
    攻击者: Hero
    防御者: Hero

    武将增减伤系数 = 1

    造成伤害提升 = 攻击者.get_造成伤害提升()
    Log().show_debug_info('DEBUG------- 攻击者 {} 造成伤害提升: {:.4f}'.format(攻击者.get_武将名称(), 造成伤害提升))
    兵种增伤系数 = MSG_兵种增伤公式(攻击者, 防御者)
    if 兵种增伤系数 != 0:
        造成伤害提升 += 兵种增伤系数
        Log().show_debug_info('DEBUG-------- 兵种增伤系数: {:.4f}, 造成伤害提升: {:.4f}'.format(兵种增伤系数, 造成伤害提升))

    武将增减伤系数 *= 造成伤害提升
    Log().show_debug_info('DEBUG------- 造成伤害提升: {:.4f}, 武将增减伤系数: {:.4f}'.format(造成伤害提升, 武将增减伤系数))

    受到伤害降低 = 防御者.get_受到伤害降低()
    Log().show_debug_info('DEBUG------- 防御者 {} 受到伤害降低: {:.4f}'.format(防御者.get_武将名称(), 受到伤害降低))
    兵种减伤系数 = MSG_兵种减伤公式(攻击者, 防御者)
    if 兵种减伤系数 != 0:
        实际兵种减伤 = (1 + 受到伤害降低) * 兵种减伤系数
        受到伤害降低 += 实际兵种减伤
        Log().show_debug_info('DEBUG-------- 兵种减伤系数: {:.4f}, 受到伤害降低: {:.4f}'.format(兵种减伤系数, 受到伤害降低))

    武将增减伤系数 *= (1 + 受到伤害降低)
    Log().show_debug_info('DEBUG------- 受到伤害降低: {:.4f}, 武将增减伤系数: {:.4f}'.format(受到伤害降低, 武将增减伤系数))

    if 防御者.get_前排状态() == True:
        对前排造成伤害提升 = 攻击者.get_对前排造成伤害提升()
        武将增减伤系数 *= 对前排造成伤害提升
        Log().show_debug_info('DEBUG------- 对前排造成伤害提升: {:.4f}, 武将增减伤系数: {:.4f}'.format(对前排造成伤害提升, 武将增减伤系数))
    else:
        对后排造成伤害提升 = 攻击者.get_对后排造成伤害提升()
        造成伤害提升 *= 对后排造成伤害提升
        Log().show_debug_info('DEBUG------- 对后排造成伤害提升: {:.4f}, 武将增减伤系数: {:.4f}'.format(对后排造成伤害提升, 武将增减伤系数))

    if 伤害类型 == DamageType.谋略:
        受到谋略伤害降低 = 防御者.get_受到谋略伤害降低()
        武将增减伤系数 *= (1 + 受到谋略伤害降低)
        Log().show_debug_info('DEBUG------- 受到谋略伤害降低: {:.4f}, 武将增减伤系数: {:.4f}'.format(受到谋略伤害降低, 武将增减伤系数))

    return 武将增减伤系数

# 伤害计算 这个方法可能会传入大量的参数
def 计算伤害(battleField, 攻击者, 防御者, 伤害类型: DamageType, 战法类型: SkillType, 伤害值 = 1.0):

    from JDI_BattleField import BattleField
    from JDI_Hero import Hero

    battleField: BattleField

    攻击者: Hero
    防御者: Hero

    确定伤害类型 = MSG_确定伤害类型(攻击者, 伤害类型)

    武将伤害公式 = MSG_武将伤害公式(攻击者, 防御者, 确定伤害类型, 伤害值)

    兵力伤害公式 = MSG_兵力伤害公式(攻击者.get_兵力())

    武将增减伤公式 = MSG_武将增减伤公式(攻击者, 防御者, 确定伤害类型, 战法类型)

    队伍造成伤害降低 = 获取武将所在的队伍(battleField, 攻击者).造成伤害降低


    伤害系数 = 伤害值
    暴击伤害 = 随机暴击伤害(攻击者, 确定伤害类型)


    Log().show_debug_info('DEBUG------- 计算伤害: {} 对 {} 造成伤害'.format(攻击者.get_武将名称(), 防御者.get_武将名称()))
    attack_damage = (武将伤害公式 * 伤害系数 * 兵力伤害公式 * 武将增减伤公式 * (1 + 暴击伤害) * (1 + 队伍造成伤害降低))
    Log().show_debug_info('DEBUG------- 武将伤害公式: {:.4f}, 伤害系数: {:.4f}, 兵力伤害公式: {:.4f}, 武将增减伤公式: {:.4f}, 暴击伤害: {:.4f}, 队伍造成伤害降低: {:.4f}'
                          .format(武将伤害公式, 伤害系数, 兵力伤害公式, 武将增减伤公式, (1 + 暴击伤害), (1 + 队伍造成伤害降低)))
    Log().show_debug_info('DEBUG------- 最后结果: {:.4f}'.format(attack_damage))
    return attack_damage





# dmga->B = (f1 + f2) • (1 + IncA - Deca) • (1 + Inc - Dec) • R • (1 + Crt) • I ri
# 其中：
# f1为兵力伤害公式，见公式二；
# f2为武将伤害*公式，见公式三。
# Inc、Dec为增减伤，共有4类：己方增伤、己方減伤（伤害降低）、敌方增伤（易伤）、敌方減伤。增减伤主要来自于战法、城内建筑，同类增减伤之间加算。
# R为技能系数*，即战法中的伤書系数，普攻默认为100％。
# Crt为会心伤害*，即会心时触发的会心伤害加成。
# ri为其他的额外增减伤乘区，同类乘区内加算。不同乘区包括兵种克制系数*，士气減伤*，兵书，州战法等