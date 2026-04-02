from core.team import Team
from core.battle import Battle
from core.hero import load_heroes_from_json, Hero
from core.formation import load_formations_from_json
from core.log.log import BattleLogger
import random
import os

def main():
    print("=== 三国谋定天下 ===\n")
    
    max_battles = 8
    battle_count = 0
    
    # 创建战场和日志记录器
    battle = Battle()
    logger = battle.logger
    
    # 从 JSON 文件中加载武将池
    hero_pool = load_heroes_from_json()
    
    # 加载阵型数据
    formations = load_formations_from_json()
    
    # 创建队伍
    team1 = Team("我方")
    team2 = Team("敌方")
    
    # 从武将池中随机选择三个武将（游戏开始时确定）
    selected1 = random.sample(hero_pool, min(3, len(hero_pool)))
    selected2 = random.sample(hero_pool, min(3, len(hero_pool)))
    
    # 记录武将选择
    logger.log_hero_selection("我方", selected1)
    logger.log_hero_selection("敌方", selected2)
    
    # 为每个队伍创建新的 Hero 对象
    team1.heroes = [Hero(
        hero.name, hero.hp, hero.wuli, hero.zhili, hero.tongshuai, hero.xiangong, hero.troop_type
    ) for hero in selected1]
    team2.heroes = [Hero(
        hero.name, hero.hp, hero.wuli, hero.zhili, hero.tongshuai, hero.xiangong, hero.troop_type
    ) for hero in selected2]
    
    # 为队伍随机选择阵型（游戏开始时确定）
    formation1 = random.choice(formations)
    formation2 = random.choice(formations)
    team1.set_formation(formation1)
    team2.set_formation(formation2)
    
    # 为队伍分配位置（1 号位、2 号位、3 号位）- 游戏开始时确定
    for i, hero in enumerate(team1.heroes, 1):
        team1.set_position(i, hero)
    for i, hero in enumerate(team2.heroes, 1):
        team2.set_position(i, hero)
    
    # 将队伍设置到战场
    battle.team1 = team1
    battle.team2 = team2
    
    # 显示初始阵容
    print("=== 初始阵容 ===")
    print(f"我方武将：{', '.join([h.name for h in team1.heroes])}")
    print(f"  阵型：{team1.formation.name} - {team1.formation.effect}")
    for i in range(1, 4):
        if i in team1.positions:
            hero = team1.positions[i]
            pos_effect = team1.get_position_effect(i)
            print(f"  {i}号位 ({pos_effect}): {hero.name}")
    print(f"\n敌方武将：{', '.join([h.name for h in team2.heroes])}")
    print(f"  阵型：{team2.formation.name} - {team2.formation.effect}")
    for i in range(1, 4):
        if i in team2.positions:
            hero = team2.positions[i]
            pos_effect = team2.get_position_effect(i)
            print(f"  {i}号位 ({pos_effect}): {hero.name}")
    print()
    
    while battle_count < max_battles:
        battle_count += 1
        print(f"\n{'='*50}")
        print(f"=== 第 {battle_count} 局 ===")
        print(f"{'='*50}")
        
        # 准备阶段
        print()
        
        # 记录战斗开始
        logger.log_battle_start(battle_count)
        
        # 开始战斗（包含布阵阶段）
        result = battle.start_battle()
        
        # 如果分出胜负，立即结束整个对战
        if result == 1:
            print(f"\n=== 对战结束 ===")
            print(f"我方获胜！")
            logger.log_tournament_end("我方", battle.get_remaining_hp(team1), battle.get_remaining_hp(team2))
            break
        elif result == 2:
            print(f"\n=== 对战结束 ===")
            print(f"敌方获胜！")
            logger.log_tournament_end("敌方", battle.get_remaining_hp(team1), battle.get_remaining_hp(team2))
            break
        else:
            # 平局，检查是否还有武将存活
            if not team1.is_alive() and not team2.is_alive():
                # 双方都全灭，结束对战
                print(f"\n=== 对战结束 ===")
                print(f"双方武将全部溃败，平局！")
                break
            
            # 检查某一方是否全员溃败
            if not team1.is_alive():
                print(f"\n=== 对战结束 ===")
                print(f"敌方获胜！")
                break
            elif not team2.is_alive():
                print(f"\n=== 对战结束 ===")
                print(f"我方获胜！")
                break
            
            # 进入下一局
            print(f"\n进入第 {battle_count + 1} 局...")
            
            # 记录进入下一局
            logger.log_next_battle(battle_count)
            
            # 恢复武将血量到满血状态
            for hero in team1.heroes:
                if hero.alive:
                    hero.hp = hero.max_hp
            
            for hero in team2.heroes:
                if hero.alive:
                    hero.hp = hero.max_hp
        
        if battle_count == max_battles:
            # 八局结束，依据剩余总血量结算
            team1_total_hp = battle.get_remaining_hp(team1)
            team2_total_hp = battle.get_remaining_hp(team2)
            
            print(f"\n{'='*50}")
            print("=== 八局结束，依据剩余血量结算 ===")
            print(f"我方剩余总血量: {team1_total_hp}")
            print(f"敌方剩余总血量: {team2_total_hp}")
            
            logger.log_tournament_end("平局", team1_total_hp, team2_total_hp)
            
            if team1_total_hp > team2_total_hp:
                print(f"我方获胜！")
            elif team2_total_hp > team1_total_hp:
                print(f"敌方获胜！")
            else:
                print(f"平局！")
            print(f"{'='*50}")
    
    # 保存日志
    logger.save_log()
    logger.save_html()
    print(f"\n日志已保存到 battle_log.txt 和 battle_log.html")
    
    # 自动打开 HTML 文件
    if os.path.exists("battle_log.html"):
        os.system("start battle_log.html")

if __name__ == "__main__":
    main()
