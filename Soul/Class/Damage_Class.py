
# 构建一个伤害类 涵盖 来源 对象 伤害值 是否会心
class Damage:
    def __init__(self, source, target, damage_value, is_crit=False):
        self.source = source  # 伤害来源
        self.target = target  # 伤害目标
        self.damage_value = damage_value  # 伤害值
        self.is_crit = is_crit  # 是否会心
