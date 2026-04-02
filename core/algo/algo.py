import random
import math

def compare_initiative(hero1, hero2):
    """
    比较两个武将的先攻顺序
    
    规则：
    1. 先攻差值超过 70 点时，先攻高者必定先手
    2. 否则先攻越高，概率越高先出手（概率只与差值有关，使用平方根曲线）
    
    参数：
        hero1: 武将 1 对象
        hero2: 武将 2 对象
    
    返回值：
        int: 返回 1 表示 hero1 先手，返回 2 表示 hero2 先手
    """
    initiative1 = hero1.xiangong
    initiative2 = hero2.xiangong
    
    diff = abs(initiative1 - initiative2)
    
    # 如果差值超过 70，先攻高者必定先手
    if diff > 70:
        return 1 if initiative1 > initiative2 else 2
    
    # 否则按照差值计算概率（使用平方根曲线）
    # 平方根曲线特点：差值较小时变化快，接近 70 时变化慢
    # 公式：概率 = 0.5 + sqrt(差值 / 70) * 0.5
    # 
    # 示例：
    # - 差值 5：sqrt(5/70) = sqrt(0.071) = 0.267, 概率 = 63.4%
    # - 差值 10：sqrt(10/70) = sqrt(0.143) = 0.378, 概率 = 68.9%
    # - 差值 20：sqrt(20/70) = sqrt(0.286) = 0.535, 概率 = 76.7%
    # - 差值 35：sqrt(35/70) = sqrt(0.5) = 0.707, 概率 = 85.4%
    # - 差值 50：sqrt(50/70) = sqrt(0.714) = 0.845, 概率 = 92.3%
    # - 差值 70：sqrt(70/70) = sqrt(1) = 1.0, 概率 = 100%
    ratio = diff / 70
    prob_high = 0.5 + math.sqrt(ratio) * 0.5
    
    if random.random() < prob_high:
        return 1 if initiative1 > initiative2 else 2
    else:
        return 2 if initiative1 > initiative2 else 1


def sort_by_initiative_probabilistic(heroes):
    """
    按照先攻概率对武将列表进行排序
    
    参数：
        heroes: 武将列表
    
    返回值：
        list: 排序后的武将列表
    """
    if len(heroes) <= 1:
        return heroes
    
    # 使用冒泡排序，每次比较两个武将
    result = heroes.copy()
    n = len(result)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # 比较相邻两个武将
            winner = compare_initiative(result[j], result[j + 1])
            # 如果后者先手，则交换
            if winner == 2:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result


def merge_sort_two_teams(team1_heroes, team2_heroes):
    """
    两队交叉排序：从两队中各取未排序的先攻最高者进行比较，胜者进入攻击顺序
    
    方法：
    1. 将两队武将按先攻降序排列
    2. 从两队中各取先攻最高的武将进行比较
    3. 胜者加入攻击顺序（不去重，允许同一武将在两队中都出现）
    4. 重复步骤 2-3，直到所有武将都排序完成
    
    参数：
        team1_heroes: 队伍 1 的武将列表
        team2_heroes: 队伍 2 的武将列表
    
    返回值：
        list: 合并后的攻击顺序列表
    """
    # 将两队武将按先攻降序排列
    team1_sorted = sorted(team1_heroes, key=lambda h: h.xiangong, reverse=True)
    team2_sorted = sorted(team2_heroes, key=lambda h: h.xiangong, reverse=True)
    
    result = []
    i = 0  # team1 的索引
    j = 0  # team2 的索引
    
    # 循环比较，直到所有武将都排序完成
    while i < len(team1_sorted) and j < len(team2_sorted):
        hero1 = team1_sorted[i]
        hero2 = team2_sorted[j]
        
        # 比较两个武将
        winner = compare_initiative(hero1, hero2)
        
        # 胜者加入攻击顺序（不去重）
        if winner == 1:
            result.append(hero1)
            i += 1
        else:
            result.append(hero2)
            j += 1
    
    # 将剩余的武将加入攻击顺序（不去重）
    while i < len(team1_sorted):
        result.append(team1_sorted[i])
        i += 1
    
    while j < len(team2_sorted):
        result.append(team2_sorted[j])
        j += 1
    
    return result
