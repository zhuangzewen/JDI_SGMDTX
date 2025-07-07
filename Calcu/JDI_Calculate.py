
from Log.JDI_Log import Log
from Calcu.JDI_RanVal import *
import math
from JDI_Enum import DamageType, SkillType, WeaponType

def msg_过滤掉被击溃的武将(heroes):
    from Generals.JDI_Hero import Hero
    from JDI_Enum import HeroInfoKey

    heroes: list[Hero]

    result = []
    for hero in heroes:
        if getattr(hero, HeroInfoKey.被击溃状态.value) == False:
            result.append(hero)
    return result

def msg_判断己方前排武将数量(skill, battleField):
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team
    from Soul.JDI_Soul import Soul, SoulSourceType

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
    from Generals.JDI_Hero import Hero
    hero: Hero
    
    # 先判断固定受击率
    if hero.get_固定受击率() != 0:
        return hero.get_固定受击率()
    
    # 获取受击率 是否为 0.6
    if hero.get_受击率() != 0.6:
        return hero.get_受击率()
    
    # 受击率 = -7.5e-9 * 兵力^2 + 0.0001625 * 兵力 - 0.275
    if hero.get_受击率() == 0.6:
        rate = -7.5e-9 * hero.get_兵力() ** 2 + 0.0001625 * hero.get_兵力() - 0.275
        if rate < 0.34:
            rate = 0.34
        return rate

    return 0

def 从队列确定受击武将(heroList):
    from Generals.JDI_Hero import Hero
    heroList: list[Hero]

    # 创建受击率数组
    hit_rate_list = []
    for hero in heroList:
        hero: Hero
        hit_rate = 实际受击率(hero)
        hit_rate_list.append(hit_rate)

    randomInt = 根据受击率列表随机一个敌方(hit_rate_list)

    selected_hero = heroList[randomInt]
    return selected_hero

def 对敌方所有目标生效(skill, battleField):
    from External.Fitting.JDI_Skill import Skill
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team

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
    from Simulator.JDI_BattleField import BattleField
    from Simulator.Team.JDI_Team import Team
    from Generals.JDI_Hero import Hero
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

        from Calcu.JDI_RanVal import 获取对比行动优先级

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
    from Simulator.Team.JDI_Team import Team
    from Generals.JDI_Hero import Hero
    from Simulator.JDI_BattleField import BattleField

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
    from Generals.JDI_Hero import Hero

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

def MSG_智力影响治疗公式(智力: float):
    # 套用伦同学的 智力影响治疗公式
    value_health = 0.00257413709518457 * (智力 ** 2) + 0.0558280362334805 * 智力 + 1177.637581883191
    return value_health

def MSG_兵力治疗公式(兵力: int):
    # 套用伦同学的 兵力影响治疗公式
    value_health =  0.9300942060815 + 0.0055332101979583 * (兵力 ** 0.274780014559044)
    return value_health

def MSG_兵力伤害公式(兵力: int):
    troop_count = 兵力

    # 处理兵力为0的特殊情况
    if troop_count <= 0:
        return 0.0
    
    # 定义关键点列表 [(兵力阈值, 衰减比例), ...]
    key_points = [
        (9000, 0.0),
        (5000, 0.2),
        (3700, 0.3),
        (2500, 0.4),
        (1600, 0.5),
        (700, 0.6),
        (300, 0.7),
        (1, 0.8)
    ]
    
    # 找到对应的区间
    for i, (threshold, reduction) in enumerate(key_points):
        if troop_count >= threshold:
            # 如果是最高区间，直接返回对应的衰减比例
            if i == 0:
                return 1.0 - reduction
            
            # 计算当前区间的斜率和基础衰减
            next_threshold, next_reduction = key_points[i-1]
            slope = (next_reduction - reduction) / (next_threshold - threshold)
            current_reduction = reduction + slope * (troop_count - threshold)
            
            # 返回实际伤害比值（1 - 削减比例）
            value_health = 1.0 - current_reduction
            
            return value_health
    
    # 默认返回值（理论上不会执行到这里）
    return 1.0

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

    return attaValue

def MSG_兵种增伤公式(攻击者, 防御者):
    from Generals.JDI_Hero import Hero
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
    from Generals.JDI_Hero import Hero
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
    from Generals.JDI_Hero import Hero
    攻击者: Hero
    防御者: Hero

    武将增减伤系数 = 1

    造成伤害提升 = 攻击者.get_造成伤害提升()
    兵种增伤系数 = MSG_兵种增伤公式(攻击者, 防御者)
    if 兵种增伤系数 != 0:
        造成伤害提升 += 兵种增伤系数

    武将增减伤系数 *= 造成伤害提升

    受到伤害降低 = 防御者.get_受到伤害降低()
    兵种减伤系数 = MSG_兵种减伤公式(攻击者, 防御者)
    if 兵种减伤系数 != 0:
        实际兵种减伤 = (1 + 受到伤害降低) * 兵种减伤系数
        受到伤害降低 += 实际兵种减伤

    武将增减伤系数 *= (1 + 受到伤害降低)

    if 防御者.get_前排状态() == True:
        对前排造成伤害提升 = 攻击者.get_对前排造成伤害提升()
        武将增减伤系数 *= 对前排造成伤害提升
    else:
        对后排造成伤害提升 = 攻击者.get_对后排造成伤害提升()
        造成伤害提升 *= 对后排造成伤害提升

    if 伤害类型 == DamageType.谋略:
        受到谋略伤害降低 = 防御者.get_受到谋略伤害降低()
        武将增减伤系数 *= (1 + 受到谋略伤害降低)

    return 武将增减伤系数

def 治疗计算(battleField, 施救者, 受助者, 治疗率 = 1.0):
    from Simulator.JDI_BattleField import BattleField
    from Generals.JDI_Hero import Hero

    battleField: BattleField
    施救者: Hero
    受助者: Hero

    施救者兵力 = 施救者.get_兵力()
    施救者智力 = 施救者.get_智力()

    其他因素 = 1

    Y = MSG_兵力治疗公式(施救者兵力) * 治疗率 * MSG_智力影响治疗公式(施救者智力) * 其他因素

    return Y

# 伤害计算 这个方法可能会传入大量的参数
def 计算伤害(battleField, 攻击者, 防御者, 伤害类型: DamageType, 战法类型: SkillType, 伤害值 = 1.0):

    from Simulator.JDI_BattleField import BattleField
    from Generals.JDI_Hero import Hero

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


    attack_damage = (武将伤害公式 * 伤害系数 * 兵力伤害公式 * 武将增减伤公式 * (1 + 暴击伤害) * (1 + 队伍造成伤害降低))
    return attack_damage
