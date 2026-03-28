from core.team import Team
from core.battle import Battle
from core.hero import load_heroes_from_json

def main():
    print("=== 三国谋定天下 ===\n")
    
    max_battles = 8
    battle_count = 0
    
    # 创建战场
    battle = Battle()
    
    # 从 JSON 文件中加载武将池
    hero_pool = load_heroes_from_json()
    
    # 第一局：创建队伍并确定阵容
    team1 = Team("我方")
    team2 = Team("敌方")
    
    # 从武将池中随机添加三个武将（不重复）
    team1.add_random_heroes(hero_pool, 3)
    team2.add_random_heroes(hero_pool, 3)
    
    # 将队伍设置到战场
    battle.team1 = team1
    battle.team2 = team2
    
    print("=== 阵容确定 ===")
    print(f"队伍1: {battle.team1.name}")
    for hero in battle.team1.heroes:
        print(f"  - {hero.name} (兵力: {hero.hp})")
    print(f"队伍2: {battle.team2.name}")
    for hero in battle.team2.heroes:
        print(f"  - {hero.name} (兵力: {hero.hp})")
    print()
    
    while battle_count < max_battles:
        battle_count += 1
        print(f"\n{'='*50}")
        print(f"=== 第 {battle_count} 局 ===")
        print(f"{'='*50}")
        
        # 开始战斗
        result = battle.start_battle()
        
        # 如果分出胜负，结算
        if result == 1:
            print(f"\n我方获胜！")
            break
        elif result == 2:
            print(f"\n敌方获胜！")
            break
        else:
            print(f"\n进入第 {battle_count + 1} 局...")
            
            # 将剩余血量作为下局的血量上限（只对存活的武将）
            if battle_count < max_battles:
                for hero in team1.heroes:
                    if hero.alive:
                        hero.max_hp = hero.hp
                        hero.hp = hero.max_hp
                
                for hero in team2.heroes:
                    if hero.alive:
                        hero.max_hp = hero.hp
                        hero.hp = hero.max_hp
        
        if battle_count == max_battles:
            # 八局结束，依据剩余总血量结算
            team1_total_hp = battle.get_remaining_hp(team1)
            team2_total_hp = battle.get_remaining_hp(team2)
            
            print(f"\n{'='*50}")
            print("=== 八局结束，依据剩余血量结算 ===")
            print(f"我方剩余总血量: {team1_total_hp}")
            print(f"敌方剩余总血量: {team2_total_hp}")
            
            if team1_total_hp > team2_total_hp:
                print(f"我方获胜！")
            elif team2_total_hp > team1_total_hp:
                print(f"敌方获胜！")
            else:
                print(f"平局！")
            print(f"{'='*50}")

if __name__ == "__main__":
    main()
