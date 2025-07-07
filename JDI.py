
from _Log.JDI_Log import Log
from JDI_Enum import HeroName, Formation, SimulatorMode
from Generals.JDI_Hero import HeroInfo, get_hero_info
from Simulator.Team.JDI_Team import TeamInfo
from Simulator.JDI_BattleField import BattleField

# 优化完成 1.0       
class Simulator():
    def __init__(self, mode=SimulatorMode.VS_1):
        self.mode = mode

    def vs1(self, team1: TeamInfo, team2: TeamInfo):

        # 模拟对战的次数为 101
        num_of_battles = 1
        Log().show_system_info('------------ 对抗的次数为 {}'.format(num_of_battles))
        # team1 获胜的次数
        num_of_wins_for_team1 = 0
        # team2 获胜的次数
        num_of_wins_for_team2 = 0

        for i in range(num_of_battles):

            Log().show_battle_info('------------ 当前第 {} 次对抗测试'.format(i + 1))

            battle = BattleField()
            battle.simulate(team1, team2)
            if battle.fight():
                num_of_wins_for_team1 += 1
            else:
                num_of_wins_for_team2 += 1
            Log().show_battle_info('------------ 当前对 {} 的第 {} 次对抗测试结束'.format(team2.teamName, i + 1))

        Log().show_system_info("------------ [{}] 获胜 {} 场，[{}] 获胜 {} 场".format(team1.teamName, num_of_wins_for_team1, team2.teamName, num_of_wins_for_team2))

# 优化完成 1.0       
def battle():

    Log().show_system_info('------------ 当前选择的模式是:{}'.format('1_VS_1'))
    
    team1_hero1 = get_hero_info(HeroName.诸葛亮)
    team1_hero1.set_extra(wl_extra=50, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team1_hero1.set_skills(None, 0, None, 0)
    team1_hero2 = get_hero_info(HeroName.Sp_诸葛亮)
    team1_hero2.set_extra(wl_extra=0, zl_extra=50, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team1_hero2.set_skills(None, 0, None, 0)
    team1_hero3 = get_hero_info(HeroName.甘夫人)
    team1_hero3.set_extra(wl_extra=0, zl_extra=50, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team1_hero3.set_skills(None, 0, None, 0)

    team2_hero1 = get_hero_info(HeroName.赵云)
    team2_hero1.set_extra(wl_extra=50, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team2_hero1.set_skills(None, 0, None, 0)
    team2_hero2 = get_hero_info(HeroName.Sp_诸葛亮)
    team2_hero2.set_extra(wl_extra=0, zl_extra=50, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team2_hero2.set_skills(None, 0, None, 0)
    team2_hero3 = get_hero_info(HeroName.刘备)
    team2_hero3.set_extra(wl_extra=0, zl_extra=50, ts_extra=0, xg_extra=0, rank_info=1, premium_info=1)
    team2_hero3.set_skills(None, 0, None, 0)

    team1 = TeamInfo(Formation.雁型阵, team1_hero1, team1_hero2, team1_hero3, '诸葛队')
    team2 = TeamInfo(Formation.一字阵, team2_hero1, team2_hero2, team2_hero3, '夫人队')

    Log().show_system_info('------------ 由 [{}] 对战 [{}]'.format(team1.teamName, team2.teamName))

    simulator = Simulator(SimulatorMode.VS_1)
    simulator.vs1(team1, team2)

# 优化完成 1.0       
def compare_teams():
    pass

# 优化完成 1.0       
def evolve_teams():
    pass

# 优化完成 1.0       
def main():
    battle()
    compare_teams()
    evolve_teams()

if __name__ == '__main__':
    main()
