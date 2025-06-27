
from JDI_Enum import SkillName, HeroName, Faction, WeaponType, HeroInfoKey
from JDI_Skill import Skill

class HeroInfo():
    def __init__(self, heroName):

        heroes = {
            HeroName.Sp_诸葛亮: {HeroInfoKey.武将名称:HeroName.Sp_诸葛亮,
                                HeroInfoKey.武将阵营:Faction.蜀,
                                HeroInfoKey.武将兵种:WeaponType.盾,
                                HeroInfoKey.武将性别:1,
                                HeroInfoKey.初始武力:53,
                                HeroInfoKey.武力成长:0.56,
                                HeroInfoKey.初始智力:125,
                                HeroInfoKey.智力成长:3.00,
                                HeroInfoKey.初始统帅:104,
                                HeroInfoKey.统帅成长:2.24,
                                HeroInfoKey.初始先攻:61,
                                HeroInfoKey.先攻成长:1.71,
                                HeroInfoKey.自带战法:SkillName.星罗棋布.value},
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
                            HeroInfoKey.自带战法:SkillName.七进七出.value},
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
                            HeroInfoKey.自带战法:SkillName.骁勇无前.value},
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
                            HeroInfoKey.自带战法:SkillName.皇思淑仁.value},
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
                            HeroInfoKey.自带战法:SkillName.携民渡江.value},
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
                            HeroInfoKey.自带战法:SkillName.九伐中原.value}}
        
        for keyName in heroes[heroName]:
            # key 为 HeroInfoKey.NAME ， 取出对应枚举中的字符
            if isinstance(keyName, HeroInfoKey):
                keyStr = keyName.value
                setattr(self, keyStr, heroes[heroName][keyName])
            
    def set_extra(self, wl_extra=0, zl_extra=0, ts_extra=0, xg_extra=0, rank_info=0, premium_info=0):
        setattr(self, HeroInfoKey.武将升阶.value, rank_info)
        setattr(self, HeroInfoKey.武将升品.value, premium_info)
        setattr(self, HeroInfoKey.武力加点.value, wl_extra)
        setattr(self, HeroInfoKey.智力加点.value, zl_extra)
        setattr(self, HeroInfoKey.统帅加点.value, ts_extra)
        setattr(self, HeroInfoKey.先攻加点.value, xg_extra)

    def set_skills(self, firstSkill, firstSkill_RankUp, secondSkill, secondSkill_RankUp):
        setattr(self, HeroInfoKey.第一战法.value, firstSkill)
        setattr(self, HeroInfoKey.第一战法升阶.value, firstSkill_RankUp)
        setattr(self, HeroInfoKey.第二战法.value, secondSkill)
        setattr(self, HeroInfoKey.第二战法升阶.value, secondSkill_RankUp)

class Hero():
    def __init__(self, heroInfo):
        
        setattr(self, HeroInfoKey.武将信息.value, heroInfo)
        setattr(self, HeroInfoKey.被击溃状态.value, False)
        setattr(self, HeroInfoKey.兵力.value, 10000)
        setattr(self, HeroInfoKey.等级.value, 50)

        self.init_base_values()
        self.init_battle_values()

    def 武将信息(self):
        return getattr(self, HeroInfoKey.武将信息.value)
    
    def 武将名称(self):
        return getattr(self.武将信息, HeroInfoKey.武将名称.value)

    def 等级(self):
        return getattr(self, HeroInfoKey.等级.value)


    # 初始化基础数值
    def init_base_values(self):
        real_wl = getattr(self.武将信息, HeroInfoKey.初始武力.value) + getattr(self.武将信息, HeroInfoKey.武力成长.value) * (self.等级 - 5) + getattr(self.武将信息, HeroInfoKey.武力加点.value)
        setattr(self, HeroInfoKey.武力.value, real_wl)
        real_zl = getattr(self.武将信息, HeroInfoKey.初始智力.value) + getattr(self.武将信息, HeroInfoKey.智力成长.value) * (self.等级 - 5) + getattr(self.武将信息, HeroInfoKey.智力加点.value)
        setattr(self, HeroInfoKey.智力.value, real_zl)
        real_ts = getattr(self.武将信息, HeroInfoKey.初始统帅.value) + getattr(self.武将信息, HeroInfoKey.统帅成长.value) * (self.等级 - 5) + getattr(self.武将信息, HeroInfoKey.统帅加点.value)
        setattr(self, HeroInfoKey.统帅.value, real_ts)
        real_xg = getattr(self.武将信息, HeroInfoKey.初始先攻.value) + getattr(self.武将信息, HeroInfoKey.先攻成长.value) * (self.等级 - 5) + getattr(self.武将信息, HeroInfoKey.先攻加点.value)
        setattr(self, HeroInfoKey.先攻.value, real_xg)

    # 初始化战斗数值
    def init_battle_values(self):
        setattr(self, HeroInfoKey.前排.value, True)
        setattr(self, HeroInfoKey.已行动状态.value, False)
        setattr(self, HeroInfoKey.受击率.value, 0)
        setattr(self, HeroInfoKey.锁定受击率.value, False)
        setattr(self, HeroInfoKey.连击几率.value, 0)
        setattr(self, HeroInfoKey.闪避几率.value, 0)
        setattr(self, HeroInfoKey.会心几率.value, 0)
        setattr(self, HeroInfoKey.奇谋几率.value, 0)
        setattr(self, HeroInfoKey.造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.对前排造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.对后排造成伤害提升.value, 1)
        setattr(self, HeroInfoKey.受到伤害降低.value, 0)
        setattr(self, HeroInfoKey.受到谋略伤害降低.value, 0)

    # 载入初始技能 
    def load_skill(self):

        D_skill = Skill(self, getattr(self.武将信息, HeroInfoKey.自带战法.value))
        D_skill.set_RankUp(getattr(self.武将信息, HeroInfoKey.武将升阶.value))
        setattr(self, HeroInfoKey.D_SkillClass.value, D_skill)

        F_skill = Skill(self, getattr(self.武将信息, HeroInfoKey.第一战法.value))
        F_skill.set_RankUp(getattr(self.武将信息, HeroInfoKey.第一战法升阶.value))
        setattr(self, HeroInfoKey.F_SkillClass.value, F_skill)

        S_skill = Skill(self, getattr(self.武将信息, HeroInfoKey.第二战法.value))
        S_skill.set_RankUp(getattr(self.武将信息, HeroInfoKey.第二战法升阶.value))
        setattr(self, HeroInfoKey.S_SkillClass.value, S_skill)

