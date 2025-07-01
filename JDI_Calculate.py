
from JDI_RanVal import *

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




def MSG_兵力伤害公式(兵力):
# 9000-10000：基本不变
# 5000-9000：每少200兵，伤害平均减1.18%
# 2600-5000：每少200兵，伤害平均减1.55%
# 1400-2600：每少200兵，伤害平均减2.08%
# 1400往下：每少200兵，伤害减3%以上
# 几个关键节点：
# 7200：90%
# 5600：80%
# 4200：70%
# 2900：60%
# 1900：50%
# 1100：40%
# 550：30%
# 150：20%
# 1：10%

    # 兵力伤害公式
    return 1

def MSG_武将伤害公式():
    return 1



# 伤害计算 这个方法可能会传入大量的参数
def 计算伤害(攻击者, 防御者, 伤害类型, 伤害值):

    from JDI_Hero import Hero
    from JDI_Enum import HeroInfoKey

    攻击者: Hero
    防御者: Hero

    IncA = 攻击者.get_造成伤害提升()
    Deca = 防御者.get_己方减伤()
    R = 伤害值
    Crt = 0.5

    MSG_兵力伤害公式() * MSG_武将伤害公式() * IncA * ( 1 + Deca) * R * (1 + Crt)





# dmga->B = (f1 + f2) • (1 + IncA - Deca) • (1 + Inc - Dec) • R • (1 + Crt) • I ri
# 其中：
# f1为兵力伤害公式，见公式二；
# f2为武将伤害*公式，见公式三。
# Inc、Dec为增减伤，共有4类：己方增伤、己方減伤（伤害降低）、敌方增伤（易伤）、敌方減伤。增减伤主要来自于战法、城内建筑，同类增减伤之间加算。
# R为技能系数*，即战法中的伤書系数，普攻默认为100％。
# Crt为会心伤害*，即会心时触发的会心伤害加成。
# ri为其他的额外增减伤乘区，同类乘区内加算。不同乘区包括兵种克制系数*，士气減伤*，兵书，州战法等