
from JDI_Log import Log
from JDI_Enum import ResponseStatus, SkillType, SkillName, SkillInfoKey, HeroName, Faction, WeaponType, HeroInfoKey, Formation, SoulSourceType, SoulResponseTime, SoulEffectType, SimulatorMode
from JDI_Skill import SkillInfo, Skill
from JDI_Hero import HeroInfo, Hero
from JDI_Team import TeamInfo, Team
from JDI_Soul import Soul
import random

def sort_action_order(team1, team2):

    def reset_all_heroes_action():
        for hero in team1.firstHero, team1.secondHero, team1.thirdHero:
            setattr(hero, HeroInfoKey.已行动状态.value, False)
        for hero in team2.firstHero, team2.secondHero, team2.thirdHero:
            setattr(hero, HeroInfoKey.已行动状态.value, False)

    def get_fastest_unbroken_hero(team):
        fastest_hero = None
        for hero in team.firstHero, team.secondHero, team.thirdHero:

            if getattr(hero, HeroInfoKey.被击溃状态.value) == True or getattr(hero, HeroInfoKey.已行动状态.value) == True:
                continue

            if fastest_hero == None:
                fastest_hero = hero
            elif getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.先攻.value) > getattr(fastest_hero, HeroInfoKey.先攻.value):
                fastest_hero = hero
        return fastest_hero

    def check_if_any_heroes_not_actioned_and_not_breakdown():
        for hero in team1.firstHero, team1.secondHero, team1.thirdHero, team2.firstHero, team2.secondHero, team2.thirdHero :
            if getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.已行动状态.value) == False:
                return True
        return False

    # y = 0.004x² +0.4343x + 50
    def check_if_both_teams_exist(hero1, hero2):
        hero1_xg = getattr(hero1, HeroInfoKey.先攻.value)
        hero2_xg = getattr(hero2, HeroInfoKey.先攻.value)
        diff = abs(hero1_xg - hero2_xg)
        p1 = 0.004 * diff ** 2 + 0.4343 * diff + 50
        # 满足概率则返回先攻大的武将 否则返回先攻小的武将
        if random.random() < p1:
            # 返回先攻大的武将
            return hero1 if hero1_xg >= hero2_xg else hero2
        else:
            return hero2 if hero2_xg >= hero1_xg else hero1

    reset_all_heroes_action()
    order_list = []
    while check_if_any_heroes_not_actioned_and_not_breakdown() == True:
        get_fast_team1 = get_fastest_unbroken_hero(team1)
        get_fast_team2 = get_fastest_unbroken_hero(team2)

        if get_fast_team1 != None and get_fast_team2 != None:
            check_fast = check_if_both_teams_exist(get_fast_team1, get_fast_team2)
        elif get_fast_team1 != None:
            check_fast = get_fast_team1
        elif get_fast_team2 != None:
            check_fast = get_fast_team2
        setattr(check_fast, HeroInfoKey.已行动状态.value, True)
        order_list.append(check_fast)
    reset_all_heroes_action()
    return order_list