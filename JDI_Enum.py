
from enum import Enum

class ResponseStatus(Enum):
    阵型结束 = '阵型结束'
    战法布阵开始 = '战法布阵开始'

class SkillType(Enum):
    指挥 = '指挥'
    主动 = '主动'
    被动 = '被动'
    追击 = '追击'

class SkillName(Enum):
    星罗棋布 = "星罗棋布"
    七进七出 = "七进七出"
    骁勇无前 = "骁勇无前"
    皇思淑仁 = "皇思淑仁"
    携民渡江 = "携民渡江"
    九伐中原 = "九伐中原"

class SkillInfoKey(Enum):

    战法信息 = '战法信息'
    战法名称 = '战法名称'
    战法类型 = '战法类型'
    战法响应时机列表 = '战法响应时机列表'
    持有者 = '持有者'
    加载状态 = '加载状态'
    战法升阶 = '战法升阶'

class HeroName(Enum):
    Sp_诸葛亮 = "Sp_诸葛亮"
    赵云 = "赵云"
    吕布 = "吕布"
    甘夫人 = "甘夫人"
    刘备 = "刘备"
    姜维 = "姜维"

class Faction(Enum):
    魏 = '魏'
    蜀 = '蜀'
    吴 = '吴'
    群 = '群'

class WeaponType(Enum):
    盾 = '盾'
    骑 = '骑'
    枪 = '枪'
    弓 = '弓'

class HeroInfoKey(Enum):
    
    武将信息 = '武将信息'

    武将名称 = '武将名称'
    武将阵营 = '武将阵营'
    武将兵种 = '武将兵种'
    武将性别 = '武将性别'

    武力 = '武力'
    初始武力 = '初始武力'
    武力成长 = '武力成长'
    武力加点 = '武力加点'

    智力 = '智力'
    初始智力 = '初始智力'
    智力成长 = '智力成长'
    智力加点 = '智力加点'

    统帅 = '统帅'
    初始统帅 = '初始统帅'
    统帅成长 = '统帅成长'
    统帅加点 = '统帅加点'

    先攻 = '先攻'
    初始先攻 = '初始先攻'
    先攻成长 = '先攻成长'
    先攻加点 = '先攻加点'

    武将升阶 = 'rank_info'
    武将升品 = 'premium_info'

    自带战法 = '自带战法'
    第一战法 = '第一战法'
    第一战法升阶 = '第一战法升阶'
    第二战法 = '第二战法'
    第二战法升阶 = '第二战法升阶'

    被击溃状态 = '被击溃状态'
    兵力 = '兵力'
    等级 = '等级'

    前排 = '前排'
    已行动状态 = '已行动状态'
    受击率 = '受击率'
    锁定受击率 = '锁定受击率'

    连击几率 = '连击几率'                   # 连击
    闪避几率 = '闪避几率'                 # 闪避
    会心几率 = '会心几率'           # 会心
    奇谋几率 = '奇谋几率'     # 奇谋
    造成伤害提升 = '造成伤害提升'       # 增伤系数
    对前排造成伤害提升 = '对前排造成伤害提升'
    对后排造成伤害提升 = '对后排造成伤害提升'
    受到伤害降低 = '受到伤害降低'                       # 减伤系数
    受到谋略伤害降低 = '受到谋略伤害降低'   # 谋略减伤系数

    TeamOrder = 'teamorder'

    D_SkillClass = 'D_SkillClass'
    F_SkillClass = 'F_SkillClass'
    S_SkillClass = 'S_SkillClass'

    

class Formation(Enum):
    一字阵 = '一字阵'
    萁型阵 = '萁型阵'
    雁型阵 = '雁型阵'
    方圆阵 = '方圆阵'
    锥型阵 = '锥型阵'
    鱼鳞阵 = '鱼鳞阵'
    钩型阵 = '钩型阵'
    偃月阵 = '偃月阵'

class SoulSourceType(Enum):
    None_Source                   = 'None_Source'
    阵型加成                       = '阵型加成'

    heroSkill                     = 'hero_skill'

    星罗棋布_阵型加成              = '星罗棋布_阵型加成'
    星罗棋布_双前排阵型加成         = '星罗棋布_双前排阵型加成'

class SoulResponseTime(Enum):
    None_Response = 'None_Response'
    BEFORE_SKILL = 'before_skill'
    AFTER_SKILL = 'after_skill'

class SoulEffectType(Enum):

    None_Effect = 'None_Effect'

    DamageIncrease = 'damage_increase'
    DamageIncrease_FrontLine = 'damage_increase_frontline'
    DamageIncrease_BackLine = 'damage_increase_backline'

    DamageReduce = 'damage_reduce'
    DamageReduce_MagniRate = 'DamageReduce_MagniRate'  # 受到谋略伤害降低

    武力 = '武力'
    智力 = '智力'
    统帅 = '统帅'
    先攻 = '先攻'

    ChainHit = 'chainhit'                   # 连击
    DodgeRate = 'dodgerate'                 # 闪避
    CriticalRate = 'criticalrate'           # 会心
    MagnificentRate = 'magnificentrate'     # 奇谋

    LockHitRate = 'lockhitrate'

class SimulatorMode(Enum):
    VS_1 = 'VS_1'
    VS_Team = 'VS_Team'
    VS_Random = 'VS_Random'