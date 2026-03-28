import random
from .team import Team
from .algo.algo import merge_sort_two_teams
from .log import BattleLogger

class Battle:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.round = 0
        self.max_rounds = 8
        self.logger = BattleLogger()
    
    def formation_phase(self):
        """布阵阶段：确定双方武将的攻击顺序"""
        print("\n=== 布阵阶段 ===")
        
        # 获取两队所有武将（包括已溃败的）
        team1_heroes = self.team1.heroes
        team2_heroes = self.team2.heroes
        
        # 使用两队交叉排序算法生成融合的攻击顺序
        merged_order = merge_sort_two_teams(team1_heroes, team2_heroes)
        
        # 将合并后的顺序分别设置到两队
        self._apply_merged_order(team1_heroes, team2_heroes, merged_order)
        
        # 显示融合后的攻击顺序
        print("融合攻击顺序：")
        for i, hero in enumerate(merged_order, 1):
            team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
            status = "溃败" if not hero.alive else f"{hero.hp}"
            print(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
        
        # 记录布阵阶段
        self.logger.log_formation(merged_order, team1_heroes, team2_heroes)
        
        print()
    
    def start_battle(self):
        """开始战斗"""
        # 布阵阶段
        self.formation_phase()
        
        self.round = 0  # 重置回合数
        print("=== 战斗开始 ===")
        
        while self.team1.is_alive() and self.team2.is_alive() and self.round < self.max_rounds:
            self.round += 1
            print(f"\n--- 第 {self.round} 回合 ---")
            
            # 记录回合开始
            self.logger.log_round_start(self.round)
            
            # 每一回合都重新计算攻击顺序（两队交叉排序）
            # 获取两队所有武将（包括已溃败的）
            team1_heroes = self.team1.heroes
            team2_heroes = self.team2.heroes
            
            # 使用两队交叉排序算法
            merged_order = merge_sort_two_teams(team1_heroes, team2_heroes)
            
            # 将合并后的顺序分别设置到两队
            self._apply_merged_order(team1_heroes, team2_heroes, merged_order)
            
            # 显示融合后的攻击顺序
            print("融合攻击顺序：")
            for i, hero in enumerate(merged_order, 1):
                team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
                status = "溃败" if not hero.alive else f"{hero.hp}"
                print(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
            
            print()
            
            # 按照融合后的顺序进行攻击
            self._attack_by_merged_order(team1_heroes, team2_heroes, merged_order)
    
    def _apply_merged_order(self, team1_heroes, team2_heroes, merged_order):
        """
        将合并后的攻击顺序应用到两个队伍
        
        方法：
        1. 从合并顺序中提取各队的武将顺序
        2. 更新各队的 attack_order
        """
        # 提取 team1 的武将顺序
        team1_order = [hero for hero in merged_order if hero in team1_heroes]
        # 提取 team2 的武将顺序
        team2_order = [hero for hero in merged_order if hero in team2_heroes]
        
        # 更新两队的攻击顺序
        self.team1.attack_order = team1_order
        self.team2.attack_order = team2_order
    
    def _attack_by_merged_order(self, team1_heroes, team2_heroes, merged_order):
        """按照融合后的顺序进行攻击"""
        # 按照融合后的顺序进行攻击
        for attacker in merged_order:
            # 检查攻击者是否存活
            if not attacker.alive:
                continue
            
            # 确定攻击者属于哪一队
            if attacker in team1_heroes:
                attacker_team = self.team1
                enemy_team = self.team2
            else:
                attacker_team = self.team2
                enemy_team = self.team1
            
            # 每次攻击前重新获取敌方存活的武将
            enemy_heroes = enemy_team.get_alive_heroes()
            if not enemy_heroes:
                break
            
            # 随机选择一个敌方武将作为目标
            target = random.choice(enemy_heroes)
            
            # 造成随机伤害（100-500）
            damage = random.randint(100, 500)
            
            # 记录随机数
            self.logger.log_random_result(attacker.name, damage, f"伤害: 100-500")
            
            target.hp -= damage
            if target.hp <= 0:
                target.hp = 0
            
            # 添加标记
            attacker_tag = "[我方]" if attacker_team.name == "我方" else "[敌方]"
            target_tag = "[我方]" if enemy_team.name == "我方" else "[敌方]"
            print(f"{attacker_tag} {attacker.name} 对 {target_tag} {target.name} 造成 {damage} 点伤害，剩余兵力：{target.hp}")
            
            # 记录攻击
            self.logger.log_attack(attacker.name, target.name, damage, target.hp, attacker_tag)
            
            # 检查敌方是否全部溃败
            if not enemy_team.is_alive():
                break
        
        # 战斗结束
        print("\n=== 战斗结束 ===")
        team1_alive = self.team1.is_alive()
        team2_alive = self.team2.is_alive()
        
        if team1_alive and not team2_alive:
            print(f"{self.team1.name} 获胜！")
            self.logger.log_battle_end(1, self.team1.name, self.team2.name)
            return 1
        elif team2_alive and not team1_alive:
            print(f"{self.team2.name} 获胜！")
            self.logger.log_battle_end(2, self.team1.name, self.team2.name)
            return 2
        else:
            # 双方都全灭或平局
            print("平局！")
            self.logger.log_battle_end(0, self.team1.name, self.team2.name)
        
        # 记录回合总结
        team1_hp = self.get_remaining_hp(self.team1)
        team2_hp = self.get_remaining_hp(self.team2)
        self.logger.log_round_summary(self.round, team1_hp, team2_hp)
        
        return 0
    
    def get_remaining_hp(self, team):
        """获取队伍剩余总血量"""
        return sum(hero.hp for hero in team.heroes)
