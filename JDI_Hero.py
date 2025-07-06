
from JDI_Enum import SkillName, HeroName, Faction, WeaponType, HeroInfoKey
from JDI_Skill import Skill, get_skill
from JDI_Log import Log

class HeroInfo():
    def __init__(self, heroName):

        heroes = {
            HeroName.赵云 :{HeroInfoKey.武将名称:HeroName.赵云,
                            HeroInfoKey.武将阵营:Faction.蜀,
                            HeroInfoKey.武将兵种:WeaponType.骑,
                            HeroInfoKey.武将性别:1,
                            HeroInfoKey.初始武力:117,
                            HeroInfoKey.武力成长:2.65,
                            HeroInfoKey.初始智力:77,
                            HeroInfoKey.智力成长:1.52,
                            HeroInfoKey.初始统帅:107,
                            HeroInfoKey.统帅成长:2.15,
                            HeroInfoKey.初始先攻:66,
                            HeroInfoKey.先攻成长:2.29,
                            HeroInfoKey.自带战法:SkillName.七进七出},
            HeroName.吕布 :{HeroInfoKey.武将名称:HeroName.吕布,
                            HeroInfoKey.武将阵营:Faction.群,
                            HeroInfoKey.武将兵种:WeaponType.骑,
                            HeroInfoKey.武将性别:1,
                            HeroInfoKey.初始武力:125,
                            HeroInfoKey.武力成长:3.00,
                            HeroInfoKey.初始智力:38,
                            HeroInfoKey.智力成长:0.70,
                            HeroInfoKey.初始统帅:93,
                            HeroInfoKey.统帅成长:1.89,
                            HeroInfoKey.初始先攻:76,
                            HeroInfoKey.先攻成长:2.57,
                            HeroInfoKey.自带战法:SkillName.骁勇无前},
            HeroName.甘夫人 :{HeroInfoKey.武将名称:HeroName.甘夫人,
                            HeroInfoKey.武将阵营:Faction.蜀,
                            HeroInfoKey.武将兵种:WeaponType.弓,
                            HeroInfoKey.武将性别:0,
                            HeroInfoKey.初始武力:25,
                            HeroInfoKey.武力成长:0.29,
                            HeroInfoKey.初始智力:102,
                            HeroInfoKey.智力成长:1.95,
                            HeroInfoKey.初始统帅:106,
                            HeroInfoKey.统帅成长:1.62,
                            HeroInfoKey.初始先攻:90,
                            HeroInfoKey.先攻成长:1.68,
                            HeroInfoKey.自带战法:SkillName.皇思淑仁},
            HeroName.刘备 :{HeroInfoKey.武将名称:HeroName.刘备,
                            HeroInfoKey.武将阵营:Faction.蜀,
                            HeroInfoKey.武将兵种:WeaponType.盾,
                            HeroInfoKey.武将性别:1,
                            HeroInfoKey.初始武力:80,
                            HeroInfoKey.武力成长:1.43,
                            HeroInfoKey.初始智力:94,
                            HeroInfoKey.智力成长:2.31,
                            HeroInfoKey.初始统帅:109,
                            HeroInfoKey.统帅成长:2.12,
                            HeroInfoKey.初始先攻:53,
                            HeroInfoKey.先攻成长:1.72,
                            HeroInfoKey.自带战法:SkillName.携民渡江},
            HeroName.姜维 :{HeroInfoKey.武将名称:HeroName.姜维,
                            HeroInfoKey.武将阵营:Faction.蜀,
                            HeroInfoKey.武将兵种:WeaponType.枪,
                            HeroInfoKey.武将性别:1,
                            HeroInfoKey.初始武力:101,
                            HeroInfoKey.武力成长:2.39,
                            HeroInfoKey.初始智力:111,
                            HeroInfoKey.智力成长:2.52,
                            HeroInfoKey.初始统帅:91,
                            HeroInfoKey.统帅成长:2.01,
                            HeroInfoKey.初始先攻:76,
                            HeroInfoKey.先攻成长:1.99,
                            HeroInfoKey.自带战法:SkillName.九伐中原}}
        
        # 输出调试信息，表示武将信息配置成功
        Log().show_debug_info('DEBUG------- 武将INFO配置成功')

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
                # 输出调试信息，显示武将信息和对应的属性值
                Log().show_debug_info('DEBUG----------- 武将INFO -- {}: {}'.format(keyStr, getattr(self, keyStr)))
            
    def set_extra(self, wl_extra=0, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=0, premium_info=0):
        setattr(self, HeroInfoKey.武将升阶.value, rank_info)
        setattr(self, HeroInfoKey.武将升品.value, premium_info)
        setattr(self, HeroInfoKey.武力加点.value, wl_extra)
        setattr(self, HeroInfoKey.智力加点.value, zl_extra)
        setattr(self, HeroInfoKey.统帅加点.value, ts_extra)
        setattr(self, HeroInfoKey.先攻加点.value, xg_extra)

        Log().show_debug_info('DEBUG------- 武将EXTRA配置成功')
        Log().show_debug_info('DEBUG----------- 武将EXTRA -- 武力加点: {}, 智力加点: {}, 统帅加点: {}, 先攻加点: {}, 武将升阶: {}, 武将升品: {}'.format(wl_extra, zl_extra, ts_extra, xg_extra, rank_info, premium_info))
        
    def set_team_name(self, teamName):
        setattr(self, HeroInfoKey.队伍名称.value, teamName)


    def set_skills(self, firstSkill, firstSkill_RankUp, secondSkill, secondSkill_RankUp):
        setattr(self, HeroInfoKey.第一战法.value, firstSkill)
        setattr(self, HeroInfoKey.第一战法升阶.value, firstSkill_RankUp)
        Log().show_debug_info('DEBUG----------- 武将INFO -- 第一战法: {}, 第一战法升阶: {}'.format(firstSkill, firstSkill_RankUp))

        setattr(self, HeroInfoKey.第二战法.value, secondSkill)
        setattr(self, HeroInfoKey.第二战法升阶.value, secondSkill_RankUp)
        Log().show_debug_info('DEBUG----------- 武将INFO -- 第二战法: {}, 第二战法升阶: {}'.format(secondSkill, secondSkill_RankUp))

class Hero():

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
    
    def get_攻心(self):
        return getattr(self, HeroInfoKey.攻心.value)
    def get_连击几率(self):
        return getattr(self, HeroInfoKey.连击几率.value)
    def get_闪避几率(self):
        return getattr(self, HeroInfoKey.闪避几率.value)
    def get_会心几率(self):
        return getattr(self, HeroInfoKey.会心几率.value)
    def get_奇谋几率(self):
        return getattr(self, HeroInfoKey.奇谋几率.value)
    def get_造成伤害提升(self):
        return getattr(self, HeroInfoKey.造成伤害提升.value)
    def get_对前排造成伤害提升(self):
        return getattr(self, HeroInfoKey.对前排造成伤害提升.value)
    def get_对后排造成伤害提升(self):
        return getattr(self, HeroInfoKey.对后排造成伤害提升.value)
    def get_受到伤害降低(self):
        return getattr(self, HeroInfoKey.受到伤害降低.value)
    def get_受到谋略伤害降低(self):
        return getattr(self, HeroInfoKey.受到谋略伤害降低.value)

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
    def get_初始统帅(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始统帅.value)
    def get_初始先攻(self):
        return getattr(self.get_武将信息(), HeroInfoKey.初始先攻.value)
    
    def get_武力成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武力成长.value)
    def get_智力成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.智力成长.value)
    def get_统帅成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.统帅成长.value)
    def get_先攻成长(self):
        return getattr(self.get_武将信息(), HeroInfoKey.先攻成长.value)
    
    def get_武力加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.武力加点.value)
    def get_智力加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.智力加点.value)
    def get_统帅加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.统帅加点.value)
    def get_先攻加点(self):
        return getattr(self.get_武将信息(), HeroInfoKey.先攻加点.value)
    
    def get_武力(self):
        return getattr(self, HeroInfoKey.武力.value)
    def get_智力(self):
        return getattr(self, HeroInfoKey.智力.value)
    def get_统帅(self):
        return getattr(self, HeroInfoKey.统帅.value)
    def get_先攻(self):
        return getattr(self, HeroInfoKey.先攻.value)

    def __init__(self, heroInfo):
        
        Log().show_debug_info('DEBUG------- 武将初始化成功')

        setattr(self, HeroInfoKey.武将信息.value, heroInfo)
        setattr(self, HeroInfoKey.被击溃状态.value, False)
        setattr(self, HeroInfoKey.兵力.value, 10000)
        setattr(self, HeroInfoKey.等级.value, 50)

        self.init_base_values()
        self.init_battle_values()
        
        # 逐条输出所有参数
        for key in HeroInfoKey:

            if key == HeroInfoKey.武将信息:
                Log().show_debug_info('DEBUG------- info -- {}'.format(self.get_武将信息()))
            else :
                if hasattr(self, key.value):
                    Log().show_debug_info('DEBUG------- hero -- {}: {}'.format(key.value, getattr(self, key.value)))

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
        P_skill = get_skill(SkillName.普攻, self)
        P_skill.设置战法升阶(0)  # 普攻没有升阶
        setattr(self, HeroInfoKey.P_SkillClass.value, P_skill)

    # 初始化基础数值
    def init_base_values(self):

        Log().show_debug_info('DEBUG------- 武将基础数值初始化完成')

        level = self.get_等级()

        real_wl = self.get_初始武力() + self.get_武力成长() * (level - 5) + self.get_武力加点()
        Log().show_debug_info('DEBUG------- real_wl: {} = {} + {} * ({} - 5) + {}'.format(real_wl, self.get_初始武力(), self.get_武力成长(), level, self.get_武力加点()))
        setattr(self, HeroInfoKey.武力.value, real_wl)
        real_zl = self.get_初始智力() + self.get_智力成长() * (level - 5) + self.get_智力加点()
        Log().show_debug_info('DEBUG------- real_zl: {} = {} + {} * ({} - 5) + {}'.format(real_zl, self.get_初始智力(), self.get_智力成长(), level, self.get_智力加点()))
        setattr(self, HeroInfoKey.智力.value, real_zl)
        real_ts = self.get_初始统帅() + self.get_统帅成长() * (level - 5) + self.get_统帅加点()
        Log().show_debug_info('DEBUG------- real_ts: {} = {} + {} * ({} - 5) + {}'.format(real_ts, self.get_初始统帅(), self.get_统帅成长(), level, self.get_统帅加点()))
        setattr(self, HeroInfoKey.统帅.value, real_ts)
        real_xg = self.get_初始先攻() + self.get_先攻成长() * (level - 5) + self.get_先攻加点()
        Log().show_debug_info('DEBUG------- real_xg: {} = {} + {} * ({} - 5) + {}'.format(real_xg, self.get_初始先攻(), self.get_先攻成长(), level, self.get_先攻加点()))
        setattr(self, HeroInfoKey.先攻.value, real_xg)



    # 初始化战斗数值
    def init_battle_values(self):
        setattr(self, HeroInfoKey.前排.value, True)
        setattr(self, HeroInfoKey.已行动状态.value, False)
        setattr(self, HeroInfoKey.受击率.value, 0)
        setattr(self, HeroInfoKey.固定受击率.value, 0)
        setattr(self, HeroInfoKey.攻心.value, 0)    
        setattr(self, HeroInfoKey.连击几率.value, 0)
        setattr(self, HeroInfoKey.闪避几率.value, 0)
        setattr(self, HeroInfoKey.会心几率.value, 0)
        setattr(self, HeroInfoKey.奇谋几率.value, 0)
        setattr(self, HeroInfoKey.造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.造成伤害降低.value, 0)
        setattr(self, HeroInfoKey.对前排造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.对后排造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到谋略伤害降低.value, 0)
        setattr(self, HeroInfoKey.伤兵.value, 0)
        setattr(self, HeroInfoKey.亖兵.value, 0)

        Log().show_debug_info('DEBUG------- 武将战斗数值初始化完成')

def get_hero_info(heroName):
    if heroName == HeroName.Sp_诸葛亮:
        from Generals.SP诸葛亮 import SP诸葛亮_info
        heroInfo = SP诸葛亮_info()
    elif heroName == HeroName.诸葛亮:
        from Generals.诸葛亮 import 诸葛亮_info
        heroInfo = 诸葛亮_info()
    else:
        heroInfo = HeroInfo(heroName)
    return heroInfo
