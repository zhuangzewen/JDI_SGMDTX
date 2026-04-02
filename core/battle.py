import random
from .team import Team
from .algo.algo import merge_sort_two_teams
from .log.log import BattleLogger

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
        
        # 显示行动顺序
        print("\n行动顺序判断完毕：")
        for i, hero in enumerate(merged_order, 1):
            team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
            status = "溃败" if not hero.alive else f"{hero.hp}"
            print(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
        
        print()
        
        # 记录布阵阶段
        self.logger.log_formation(merged_order, team1_heroes, team2_heroes)
        
        # 展示阵型效果（在行动顺序之后）
        self._display_formation_effects()
        
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
            
            # 显示行动顺序
            print("\n行动顺序判断完毕：")
            for i, hero in enumerate(merged_order, 1):
                team_tag = "[我方]" if hero in team1_heroes else "[敌方]"
                status = "溃败" if not hero.alive else f"{hero.hp}"
                print(f"  {i}. {team_tag} {hero.name} (先攻：{hero.xiangong}, 兵力：{status})")
            
            print()
            
            # 记录回合行动顺序
            self.logger.log_round_order(merged_order, team1_heroes, team2_heroes)
            
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
            
            # 根据受击率选择目标
            target = self._select_target_by_hit_rate(enemy_team, enemy_heroes)
            
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
    
    def _display_formation_effects(self):
        """展示阵型效果"""
        print("\n=== 阵型效果 ===")
        
        # 兵种图标映射
        troop_icons = {
            '盾': '🛡️',  # 盾兵
            '弓': '🏹',  # 弓兵
            '骑': '🐎',  # 骑兵
            '枪': '🔱',  # 枪兵
        }
        
        # 显示我方阵型效果
        if self.team1.formation:
            print(f"\n[{self.team1.name}] 队获得【阵型——{self.team1.formation.name}】强化效果")
            effects_list = []
            for i in range(1, 4):
                if i in self.team1.positions:
                    hero = self.team1.positions[i]
                    pos_info = self.team1.formation.positions.get(str(i), {})
                    effect = pos_info.get('effect', '')
                    if effect:
                        # 获取兵种图标
                        icon = troop_icons.get(hero.troop_type, '✓')
                        print(f"  {icon} {hero.name}: {effect}")
                        effects_list.append((hero.name, effect))
            
            # 记录到日志
            self.logger.log_formation_effects(self.team1.name, self.team1.formation.name, effects_list)
        
        # 显示敌方阵型效果
        if self.team2.formation:
            print(f"\n[{self.team2.name}] 队获得【阵型——{self.team2.formation.name}】强化效果")
            effects_list = []
            for i in range(1, 4):
                if i in self.team2.positions:
                    hero = self.team2.positions[i]
                    pos_info = self.team2.formation.positions.get(str(i), {})
                    effect = pos_info.get('effect', '')
                    if effect:
                        # 获取兵种图标
                        icon = troop_icons.get(hero.troop_type, '✓')
                        print(f"  {icon} {hero.name}: {effect}")
                        effects_list.append((hero.name, effect))
            
            # 记录到日志
            self.logger.log_formation_effects(self.team2.name, self.team2.formation.name, effects_list)
    
    def _select_target_by_hit_rate(self, enemy_team, enemy_heroes):
        """
        根据受击率选择目标
        
        规则：
        - 单前排：受击率 60%
        - 双前排：每个前排受击率 40%
        - 后排：受击率 20%
        """
        import random
        
        # 统计前排和后排武将
        front_row_heroes = []
        back_row_heroes = []
        
        for hero in enemy_heroes:
            # 获取该武将的位置
            position_num = None
            for pos_num, h in enemy_team.positions.items():
                if h == hero:
                    position_num = pos_num
                    break
            
            if position_num is not None:
                role = enemy_team.get_position_role(position_num)
                if role == "前排":
                    front_row_heroes.append(hero)
                elif role == "后排":
                    back_row_heroes.append(hero)
            else:
                # 默认视为后排
                back_row_heroes.append(hero)
        
        # 根据前排数量确定受击率
        if len(front_row_heroes) == 1:
            # 单前排：前排 60%，后排 40% 平分
            front_hit_rate = 0.6
            back_hit_rate = 0.4 / len(back_row_heroes) if back_row_heroes else 0
        elif len(front_row_heroes) == 2:
            # 双前排：每个前排 40%，后排 20%
            front_hit_rate = 0.4
            back_hit_rate = 0.2
        elif len(front_row_heroes) == 3:
            # 三前排：每个前排平均分配
            front_hit_rate = 1.0 / len(front_row_heroes)
            back_hit_rate = 0
        else:
            # 无前排：后排平均分配
            front_hit_rate = 0
            back_hit_rate = 1.0 / len(back_row_heroes) if back_row_heroes else 0
        
        # 构建受击率列表
        hit_rates = []
        targets = []
        
        for hero in front_row_heroes:
            hit_rates.append(front_hit_rate)
            targets.append(hero)
        
        for hero in back_row_heroes:
            hit_rates.append(back_hit_rate)
            targets.append(hero)
        
        # 使用轮盘赌算法选择目标
        rand = random.random()
        cumulative_rate = 0
        for i, rate in enumerate(hit_rates):
            cumulative_rate += rate
            if rand <= cumulative_rate:
                return targets[i]
        
        # 如果因为浮点数精度问题没有选中，返回最后一个
        return targets[-1] if targets else enemy_heroes[0]
