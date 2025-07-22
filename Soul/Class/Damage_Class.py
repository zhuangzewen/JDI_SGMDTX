
# 构建一个伤害类 涵盖 来源 对象 伤害值 是否会心
class Damage:
    def __init__(self, source=None, target=None, type=None, damage_value=None, is_crit=False, skillEffectName=""):
        self.source = source                    # 伤害来源
        self.target = target                    # 伤害目标
        self.type = type                        # 伤害类型
        self.damage_value = damage_value        # 伤害值
        self.is_crit = is_crit                  # 是否会心
        self.skillEffectName = skillEffectName  # 技能效果名称
