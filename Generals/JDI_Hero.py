
from Control.Imports.hero_imports import *
import random

class HeroInfo():
    def __init__(self, heroName):

        heroes = {}

        # 检查武将是否存在于预设中
        if heroName not in heroes:
            # 生成随机武将数据
            random_data = self.generate_random_hero_data(heroName)
            heroes[heroName] = random_data

        # 遍历heroes字典中指定武将的信息
        for keyName in heroes[heroName]:
            if isinstance(keyName, HeroInfoKey):
                keyStr = keyName.value
            # 判断keyName是否是HeroInfoKey的实例
            if isinstance(keyName, HeroInfoKey):
                # 获取keyName的值
                keyStr = keyName.value
                # 使用setattr函数将值赋给当前对象的属性
                setattr(self, keyStr, heroes[heroName][keyName])
            
    def set_extra(self, wl_extra=0, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=0, premium_info=0):
        setattr(self, HeroInfoKey.武将升阶.value, rank_info)
        setattr(self, HeroInfoKey.武将升品.value, premium_info)
        setattr(self, HeroInfoKey.武力加点.value, wl_extra)
        setattr(self, HeroInfoKey.智力加点.value, zl_extra)
        setattr(self, HeroInfoKey.统率加点.value, ts_extra)
        setattr(self, HeroInfoKey.先攻加点.value, xg_extra)

    @staticmethod
    def generate_random_hero_data(heroName):
        """生成随机武将数据"""
        # 随机选择阵营
        factions = [Faction.魏, Faction.蜀, Faction.吴, Faction.群]
        random_faction = random.choice(factions)
        
        # 随机选择兵种
        weapons = [WeaponType.骑, WeaponType.枪, WeaponType.弓, WeaponType.盾]
        random_weapon = random.choice(weapons)
        
        # 随机生成属性值 (参考现有武将的属性范围)
        random_data = {
            HeroInfoKey.武将名称: heroName,
            HeroInfoKey.武将阵营: random_faction,
            HeroInfoKey.武将兵种: random_weapon,
            HeroInfoKey.武将性别: random.choice([0, 1]),  # 0女 1男
            HeroInfoKey.初始武力: random.randint(25, 125),
            HeroInfoKey.武力成长: round(random.uniform(0.3, 3.0), 2),
            HeroInfoKey.初始智力: random.randint(38, 111),
            HeroInfoKey.智力成长: round(random.uniform(0.7, 2.6), 2),
            HeroInfoKey.初始统率: random.randint(91, 109),
            HeroInfoKey.统率成长: round(random.uniform(1.6, 2.2), 2),
            HeroInfoKey.初始先攻: random.randint(53, 90),
            HeroInfoKey.先攻成长: round(random.uniform(1.7, 2.6), 2),
            HeroInfoKey.自带战法: None
        }
        
        return random_data

    def set_team_name(self, teamName):
        setattr(self, HeroInfoKey.队伍名称.value, teamName)

    def set_skills(self, firstSkill, firstSkill_RankUp, secondSkill, secondSkill_RankUp):
        setattr(self, HeroInfoKey.第一战法.value, firstSkill)
        setattr(self, HeroInfoKey.第一战法升阶.value, firstSkill_RankUp)

        setattr(self, HeroInfoKey.第二战法.value, secondSkill)
        setattr(self, HeroInfoKey.第二战法升阶.value, secondSkill_RankUp)

class Hero():

    def get_持有Soul列表(self):
        return getattr(self, HeroInfoKey.持有Soul列表.value)
    def get_响应Soul列表(self):
        return getattr(self, HeroInfoKey.响应Soul列表.value)

    def get_缘分列表(self):
        if hasattr(self.get_武将信息(), HeroInfoKey.缘分列表.value):
            return getattr(self.get_武将信息(), HeroInfoKey.缘分列表.value)
        return []

    def get_武将信息(self):
        return getattr(self, HeroInfoKey.武将信息.value)
    def get_前排状态(self):
        return getattr(self, HeroInfoKey.前排.value)
    def get_已行动状态(self):
        return getattr(self, HeroInfoKey.已行动状态.value)
    def get_受击率(self):
        return getattr(self, HeroInfoKey.受击率.value)
    def get_固定受击率(self):
        return getattr(self, HeroInfoKey.固定受击率.value)
    
    def get_看破(self):
        return getattr(self, HeroInfoKey.看破.value)
    def get_破甲(self):
        return getattr(self, HeroInfoKey.破甲.value)
    def get_抵御(self):
        return getattr(self, HeroInfoKey.抵御.value)
    def get_攻心(self):
        return getattr(self, HeroInfoKey.攻心.value)
    def get_受治疗效果(self):
        return getattr(self, HeroInfoKey.受治疗效果.value)
    def get_连击几率(self):
        return getattr(self, HeroInfoKey.连击几率.value)
    def get_规避(self):
        return getattr(self, HeroInfoKey.规避.value)
    def get_会心几率(self):
        return getattr(self, HeroInfoKey.会心几率.value)
    def get_会心伤害(self):
        return getattr(self, HeroInfoKey.会心伤害.value)
    def get_奇谋几率(self):
        return getattr(self, HeroInfoKey.奇谋几率.value)
    def get_奇谋伤害(self):
        return getattr(self, HeroInfoKey.奇谋伤害.value)

    def get_造成伤害提升(self):
        return getattr(self, HeroInfoKey.造成伤害提升.value)
    def get_造成伤害降低(self):
        return getattr(self, HeroInfoKey.造成伤害降低.value)
    def get_受到伤害提升(self):
        return getattr(self, HeroInfoKey.受到伤害提升.value)
    def get_受到伤害降低(self):
        return getattr(self, HeroInfoKey.受到伤害降低.value)

    def get_受到异性伤害提升(self):
        return getattr(self, HeroInfoKey.受到异性伤害提升.value)
    def get_受到异性伤害降低(self):
        return getattr(self, HeroInfoKey.受到异性伤害降低.value)

    def get_对前排造成伤害提升(self):
        return getattr(self, HeroInfoKey.对前排造成伤害提升.value)
    def get_对前排造成伤害降低(self):
        return getattr(self, HeroInfoKey.对前排造成伤害降低.value)

    def get_造成谋略伤害提升(self):
        return getattr(self, HeroInfoKey.造成谋略伤害提升.value)
    def get_造成谋略伤害降低(self):
        return getattr(self, HeroInfoKey.造成谋略伤害降低.value)
    def get_受到谋略伤害提升(self):
        return getattr(self, HeroInfoKey.受到谋略伤害提升.value)
    def get_受到谋略伤害降低(self):
        return getattr(self, HeroInfoKey.受到谋略伤害降低.value)

    def get_造成兵刃伤害提升(self):
        return getattr(self, HeroInfoKey.造成兵刃伤害提升.value)
    def get_造成兵刃伤害降低(self):
        return getattr(self, HeroInfoKey.造成兵刃伤害降低.value)
    def get_受到兵刃伤害提升(self):
        return getattr(self, HeroInfoKey.受到兵刃伤害提升.value)
    def get_受到兵刃伤害降低(self):
        return getattr(self, HeroInfoKey.受到兵刃伤害降低.value)

    def get_普通攻击造成伤害提升(self):
        return getattr(self, HeroInfoKey.普通攻击造成伤害提升.value)
    def get_普通攻击造成伤害降低(self):
        return getattr(self, HeroInfoKey.普通攻击造成伤害降低.value)
    def get_受到普通攻击伤害提升(self):
        return getattr(self, HeroInfoKey.受到普通攻击伤害提升.value)
    def get_受到普通攻击伤害降低(self):
        return getattr(self, HeroInfoKey.受到普通攻击伤害降低.value)

    def get_主动战法造成伤害提升(self):
        return getattr(self, HeroInfoKey.主动战法造成伤害提升.value)
    def get_主动战法造成伤害降低(self):
        return getattr(self, HeroInfoKey.主动战法造成伤害降低.value)
    def get_受到主动战法伤害提升(self):
        return getattr(self, HeroInfoKey.受到主动战法伤害提升.value)
    def get_受到主动战法伤害降低(self):
        return getattr(self, HeroInfoKey.受到主动战法伤害降低.value)

    def get_追击战法造成伤害提升(self):
        return getattr(self, HeroInfoKey.追击战法造成伤害提升.value)
    def get_追击战法造成伤害降低(self):
        return getattr(self, HeroInfoKey.追击战法造成伤害降低.value)
    def get_受到追击战法伤害提升(self):
        return getattr(self, HeroInfoKey.受到追击战法伤害提升.value)
    def get_受到追击战法伤害降低(self):
        return getattr(self, HeroInfoKey.受到追击战法伤害降低.value)

    def get_主动战法发动率降低(self):
        return getattr(self, HeroInfoKey.主动战法基础发动率.value)

    def get_被击溃状态(self):
        return getattr(self, HeroInfoKey.被击溃状态.value)
    def get_兵力(self):
        return getattr(self, HeroInfoKey.兵力.value)
    def get_等级(self):
        return getattr(self, HeroInfoKey.等级.value)
    
    def get_伤兵(self):
        return getattr(self, HeroInfoKey.伤兵.value)
    def get_亖兵(self):
        return getattr(self, HeroInfoKey.亖兵.value)
    
    def get_队伍名称(self):
        return getattr(self.get_武将信息(), HeroInfoKey.队伍名称.value)
    def get_武将名称(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将名称.value)
    def get_武将阵营(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将阵营.value)
    def get_武将兵种(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将兵种.value)
    def get_武将性别(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将性别.value)
    def get_武将升阶(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将升阶.value)
    def get_武将升品(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武将升品.value)
    
    def get_初始武力(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始武力.value)
    def get_初始智力(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始智力.value)
    def get_初始统率(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始统率.value)
    def get_初始先攻(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始先攻.value)
    
    def get_武力成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武力成长.value)
    def get_智力成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.智力成长.value)
    def get_统率成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.统率成长.value)
    def get_先攻成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.先攻成长.value)
    
    def get_武力加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武力加点.value)
    def get_智力加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.智力加点.value)
    def get_统率加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.统率加点.value)
    def get_先攻加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.先攻加点.value)
    
    def get_武力(self):
        return getattr(self, HeroInfoKey.武力.value)
    def get_智力(self):
        return getattr(self, HeroInfoKey.智力.value)
    def get_统率(self):
        return getattr(self, HeroInfoKey.统率.value)
    def get_先攻(self):
        return getattr(self, HeroInfoKey.先攻.value)

    def __init__(self, heroInfo):

        setattr(self, HeroInfoKey.武将信息.value, heroInfo)
        setattr(self, HeroInfoKey.被击溃状态.value, False)
        setattr(self, HeroInfoKey.兵力.value, 10000)

        setattr(self, HeroInfoKey.等级.value, 50)

        self.init_base_values()
        self.init_battle_values()

    # 载入初始技能 
    def load_skill(self):
        hero_info: HeroInfo = getattr(self, HeroInfoKey.武将信息.value)

        D_skill = get_skill(getattr(hero_info, HeroInfoKey.自带战法.value), self)
        D_skill.设置战法升阶(getattr(hero_info, HeroInfoKey.武将升品.value))
        setattr(self, HeroInfoKey.D_SkillClass.value, D_skill)

        F_skill = get_skill(getattr(hero_info, HeroInfoKey.第一战法.value), self)
        F_skill.设置战法升阶(getattr(hero_info, HeroInfoKey.第一战法升阶.value))
        setattr(self, HeroInfoKey.F_SkillClass.value, F_skill)

        S_skill = get_skill(getattr(hero_info, HeroInfoKey.第二战法.value), self)
        S_skill.设置战法升阶(getattr(hero_info, HeroInfoKey.第二战法升阶.value))
        setattr(self, HeroInfoKey.S_SkillClass.value, S_skill)

        # 普攻战法
        P_skill = get_skill(Fitting_List_Enum.普攻, self)
        P_skill.设置战法升阶(0)  # 普攻没有升阶
        setattr(self, HeroInfoKey.P_SkillClass.value, P_skill)

    # 初始化基础数值
    def init_base_values(self):

        level = self.get_等级()

        real_wl = self.get_初始武力() + self.get_武力成长() * (level - 5) + self.get_武力加点()
        setattr(self, HeroInfoKey.武力.value, real_wl)
        real_zl = self.get_初始智力() + self.get_智力成长() * (level - 5) + self.get_智力加点()
        setattr(self, HeroInfoKey.智力.value, real_zl)
        real_ts = self.get_初始统率() + self.get_统率成长() * (level - 5) + self.get_统率加点()
        setattr(self, HeroInfoKey.统率.value, real_ts)
        real_xg = self.get_初始先攻() + self.get_先攻成长() * (level - 5) + self.get_先攻加点()
        setattr(self, HeroInfoKey.先攻.value, real_xg)

    # 初始化战斗数值
    def init_battle_values(self):
        setattr(self, HeroInfoKey.前排.value, True)
        setattr(self, HeroInfoKey.已行动状态.value, False)
        setattr(self, HeroInfoKey.受击率.value, 0)
        setattr(self, HeroInfoKey.固定受击率.value, 0)

        setattr(self, HeroInfoKey.看破.value, 0)
        setattr(self, HeroInfoKey.破甲.value, 0)
        setattr(self, HeroInfoKey.抵御.value, 0)
        setattr(self, HeroInfoKey.攻心.value, 0)
        setattr(self, HeroInfoKey.受治疗效果.value, 1)
        setattr(self, HeroInfoKey.连击几率.value, 0)
        setattr(self, HeroInfoKey.规避.value, 0)
        setattr(self, HeroInfoKey.会心几率.value, 0)
        setattr(self, HeroInfoKey.会心伤害.value, 1.5)
        setattr(self, HeroInfoKey.奇谋几率.value, 0)
        setattr(self, HeroInfoKey.奇谋伤害.value, 1.5)

        setattr(self, HeroInfoKey.造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.造成伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到伤害降低.value, 0)

        setattr(self, HeroInfoKey.受到异性伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到异性伤害降低.value, 0)

        setattr(self, HeroInfoKey.对前排造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.对前排造成伤害降低.value, 0)

        setattr(self, HeroInfoKey.造成谋略伤害提升.value, 1)
        setattr(self, HeroInfoKey.造成谋略伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到谋略伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到谋略伤害降低.value, 0)

        setattr(self, HeroInfoKey.造成兵刃伤害提升.value, 1)
        setattr(self, HeroInfoKey.造成兵刃伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到兵刃伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到兵刃伤害降低.value, 0)

        setattr(self, HeroInfoKey.普通攻击造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.普通攻击造成伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到普通攻击伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到普通攻击伤害降低.value, 0)

        setattr(self, HeroInfoKey.主动战法造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.主动战法造成伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到主动战法伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到主动战法伤害降低.value, 0)

        setattr(self, HeroInfoKey.追击战法造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.追击战法造成伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到追击战法伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到追击战法伤害降低.value, 0)

        setattr(self, HeroInfoKey.主动战法基础发动率.value, 0)

        setattr(self, HeroInfoKey.伤兵.value, 0)
        setattr(self, HeroInfoKey.亖兵.value, 0)

        setattr(self, HeroInfoKey.持有Soul列表.value, [])
        setattr(self, HeroInfoKey.响应Soul列表.value, [])


    # 响应针对武将的response
    def response(self, status, battleField=None, hero=None, sourceSoul=None):

        if self.get_被击溃状态():
            return
        
        if status == SoulResponseTime.武将溃败 and hero == self:

            setattr(self, HeroInfoKey.被击溃状态.value, True)

            self.get_响应Soul列表().clear()

            for soul in self.get_持有Soul列表():
                soul: Soul
                soul.response(status=status, battleField=self, hero=hero, sourceSoul=sourceSoul)

            self.get_持有Soul列表().clear()

        elif status == SoulResponseTime.造成伤害时:

            if hero == self and self.get_攻心() > 0 and sourceSoul.damage.type == SoulDamageType.谋略:
                Log().battle_L2('[{}]触发攻心'.format(self.get_武将名称().value))
                伤害SOUL: Soul = sourceSoul
                恢复兵力 = int(伤害SOUL.effect_value * self.get_攻心())

                from Soul.JDI_Soul import Soul
                from Soul.Enum.SoulEffectType_Enum import SoulEffectType
                恢复soul = Soul(target=self,
                                initiator=self,
                                skill=None,
                                effect_type=SoulEffectType.恢复兵力,
                                effect_value=恢复兵力,
                                battleField=battleField)
                恢复soul.deploy_initial()

        if (status == SoulResponseTime.普攻行动时 or status == SoulResponseTime.连击行动时 or status == SoulResponseTime.主动战法行动时) and hero != self:
            # 不是自己不响应
            return
            
        if status == SoulResponseTime.普攻行动时 or status == SoulResponseTime.连击行动时:
            from Calcu.JDI_Calculate import msg_普攻发起判断
            if not msg_普攻发起判断(self):
                Log().battle_L1('[{}]无法普攻'.format(self.get_武将名称().value))
                return
        
        if status == SoulResponseTime.主动战法行动时:
            from Calcu.JDI_Calculate import msg_主动战法发起判断
            if not msg_主动战法发起判断(self):
                Log().battle_L1('[{}]无法主动战法'.format(self.get_武将名称().value))
                return

        for soul in self.get_响应Soul列表():
            from Soul.JDI_Soul import Soul
            soul: Soul
            soul.response(status=status, battleField=battleField, hero=hero, sourceSoul=sourceSoul)

def get_hero_info(heroName):
    """
    动态获取武将信息，避免穷举
    使用约定优于配置的方式自动查找武将模块
    """

    hero_name = heroName
    
    try:
        # 动态导入武将模块

        # heroName 为 Generals_Name_Enum.诸葛亮SP
        # 获取枚举的key作为字符串（使用name属性）
        hero_name = heroName.name

        import importlib
        module_path = f"Generals.List.{hero_name}"
        module = importlib.import_module(module_path)
        
        # 获取对应的info类
        info_class_name = f"{hero_name}_info"
        if hasattr(module, info_class_name):
            info_class = getattr(module, info_class_name)
            return info_class()
        else:
            return HeroInfo(heroName)
            
    except ImportError:
        Log().battle_L0(f"[get_hero_info] 武将名称错误: {heroName}")
        return HeroInfo(heroName)
