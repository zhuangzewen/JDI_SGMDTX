from core.team import Team
from core.battle import Battle
from core.hero import load_heroes_from_json, Hero
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
    
    # 第一局：创建队伍并确定阵容
    team1 = Team("我方")
    team2 = Team("敌方")
    
    # 从武将池中随机添加三个武将
    # 两队可以选到相同的武将，但一个队伍内部不能有重复
    # 为每个队伍创建新的 Hero 对象，避免引用同一个对象
    selected1 = random.sample(hero_pool, min(3, len(hero_pool)))
    selected2 = random.sample(hero_pool, min(3, len(hero_pool)))
    
    # 记录武将选择
    logger.log_hero_selection("我方", selected1)
    logger.log_hero_selection("敌方", selected2)
    
    # 为每个队伍创建新的 Hero 对象
    team1.heroes = [Hero(
        hero.name, hero.hp, hero.wuli, hero.zhili, hero.tongshuai, hero.xiangong
    ) for hero in selected1]
    team2.heroes = [Hero(
        hero.name, hero.hp, hero.wuli, hero.zhili, hero.tongshuai, hero.xiangong
    ) for hero in selected2]
    
    # 将队伍设置到战场
    battle.team1 = team1
    battle.team2 = team2
    
    print("=== 初始阵容 ===")
    print(f"队伍 1: {battle.team1.name}")
    for hero in battle.team1.heroes:
        print(f"  - {hero.name} (兵力：{hero.hp})")
    print(f"队伍 2: {battle.team2.name}")
    for hero in battle.team2.heroes:
        print(f"  - {hero.name} (兵力：{hero.hp})")
    print()
    
    while battle_count < max_battles:
        battle_count += 1
        print(f"\n{'='*50}")
        print(f"=== 第 {battle_count} 局 ===")
        print(f"{'='*50}")
        
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
            
            # 将剩余血量作为下局的血量上限（只对存活的武将）
            if battle_count < max_battles:
                # 清理已溃败的武将
                team1.heroes = [hero for hero in team1.heroes if hero.alive]
                team2.heroes = [hero for hero in team2.heroes if hero.alive]
                
                # 更新存活武将的血量
                for hero in team1.heroes:
                    hero.max_hp = hero.hp
                    hero.hp = hero.max_hp
                
                for hero in team2.heroes:
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
