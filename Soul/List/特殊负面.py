# 特殊负面效果 deploy/restore 方法
from Control.Log.JDI_Log import Log
from Calcu.JDI_Calculate import msg_移除响应
from Soul.Enum.SoulEffectType_Enum import SoulEffectType

def deploy_震慑_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.震慑 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[震慑]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[震慑]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_震慑_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[震慑]效果已消失')
    return True

def deploy_缴械_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.缴械 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[缴械]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[缴械]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_缴械_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[缴械]效果已消失')
    return True

def deploy_技穷_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.技穷 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[技穷]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[技穷]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_技穷_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[技穷]效果已消失')
    return True

def deploy_混乱_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.混乱 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[混乱]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[混乱]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_混乱_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[混乱]效果已消失')
    return True

def deploy_嘲讽_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.嘲讽 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[嘲讽]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[嘲讽]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_嘲讽_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[嘲讽]效果已消失')
    return True

def deploy_虚弱_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.虚弱 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[虚弱]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[虚弱]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_虚弱_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[虚弱]效果已消失')
    return True

def deploy_断粮_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        if soul.effect_type == SoulEffectType.断粮 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[断粮]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[断粮]效果已施加')
    # respond逻辑已移除，主流程统一控制
    return True

def restore_断粮_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[断粮]效果已消失')
    return True

def deploy_洪水_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        # 修复 SoulEffectType 局部作用域问题，直接引用全局导入的 SoulEffectType
        if soul.effect_type == SoulEffectType.洪水 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[洪水]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[洪水]效果已施加')
    # 降低统率属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, Soul
    统率soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.统率,
                  effect_value=-20,
                  source_soul=self)
    统率soul.deploy_initial()
    return True

def restore_洪水_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[洪水]效果已消失')
    # 返还统率属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, SoulEffectType, Soul
    统率soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.统率,
                  effect_value=20,
                  source_soul=self)
    统率soul.deploy_initial()
    return True

def deploy_火攻_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        # 修复 SoulEffectType 局部作用域问题，直接引用全局导入的 SoulEffectType
        if soul.effect_type == SoulEffectType.火攻 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[火攻]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[火攻]效果已施加')
    # 降低智力属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, Soul
    智力soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.智力,
                  effect_value=-15,
                  source_soul=self)
    智力soul.deploy_initial()
    return True

def restore_火攻_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[火攻]效果已消失')
    # 返还智力属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, SoulEffectType, Soul
    智力soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.智力,
                  effect_value=15,
                  source_soul=self)
    智力soul.deploy_initial()
    return True

def deploy_风暴_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        # 修复 SoulEffectType 局部作用域问题，直接引用全局导入的 SoulEffectType
        if soul.effect_type == SoulEffectType.风暴 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[风暴]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[风暴]效果已施加')
    # 降低先攻属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, Soul
    先攻soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.先攻,
                  effect_value=-30,
                  source_soul=self)
    先攻soul.deploy_initial()
    return True

def restore_风暴_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[风暴]效果已消失')
    # 返还先攻属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, SoulEffectType, Soul
    先攻soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.先攻,
                  effect_value=30,
                  source_soul=self)
    先攻soul.deploy_initial()
    return True

def deploy_畏惧_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        # 修复 SoulEffectType 局部作用域问题，直接引用全局导入的 SoulEffectType
        if soul.effect_type == SoulEffectType.畏惧 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[畏惧]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[畏惧]效果已施加')
    # 降低受到伤害降低固定值属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, Soul
    受到伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.受到伤害降低固定值,
                  effect_value=0.1,
                  source_soul=self)
    受到伤害soul.deploy_initial()
    return True

def restore_畏惧_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[畏惧]效果已消失')
    # 返还受到伤害降低固定值属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, SoulEffectType, Soul
    受到伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.受到伤害降低固定值,
                  effect_value=-0.1,
                  source_soul=self)
    受到伤害soul.deploy_initial()
    return True

def deploy_妖术_initial(self):
    heroName = self.target.get_武将名称().value
    is存在同类状态 = False
    for soul in self.target.get_响应Soul列表():
        # 修复 SoulEffectType 局部作用域问题，直接引用全局导入的 SoulEffectType
        if soul.effect_type == SoulEffectType.妖术 and soul != self:
            is存在同类状态 = True
            msg_移除响应(soul)
    if is存在同类状态:
        Log().battle_L2(f'[{heroName}]的[妖术]效果已刷新')
    else:
        Log().battle_L2(f'[{heroName}]的[妖术]效果已施加')
    # 降低会心伤害和奇谋伤害属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, Soul
    会心伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.会心伤害,
                  effect_value=-0.15,
                  source_soul=self)
    会心伤害soul.deploy_initial()
    奇谋伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.奇谋伤害,
                  effect_value=-0.15,
                  source_soul=self)
    奇谋伤害soul.deploy_initial()
    return True

def restore_妖术_initial(self):
    heroName = self.target.get_武将名称().value
    msg_移除响应(self)
    Log().battle_L2(f'[{heroName}]的[妖术]效果已消失')
    # 返还会心伤害和奇谋伤害属性，采用异常状态效果_额外效果
    from Soul.JDI_Soul import SoulSourceDetail, SoulEffectType, Soul
    会心伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.会心伤害,
                  effect_value=0.15,
                  source_soul=self)
    会心伤害soul.deploy_initial()
    奇谋伤害soul = Soul(target=self.target,
                  sourceDetail=[SoulSourceDetail.异常状态效果_额外效果],
                  skill=self.skill,
                  effect_type=SoulEffectType.奇谋伤害,
                  effect_value=0.15,
                  source_soul=self)
    奇谋伤害soul.deploy_initial()
    return True
