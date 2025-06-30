
# 优化完成 1.0    
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

