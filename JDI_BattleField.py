
from JDI_Log import Log
from JDI_Enum import ResponseStatus, SkillName, SkillInfoKey, WeaponType, HeroInfoKey, Formation, SoulSourceType, SoulEffectType, SkillType, DamageType
from JDI_Team import TeamInfo, Team
from JDI_Hero import Hero
from JDI_Skill import Skill
from JDI_Soul import Soul
from JDI_Calculate import *

class BattleField():

    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.command_handle_respon = []
        self.soul_list = []
        Log().show_debug_info('DEBUG------- 战场初始化完成')

    def getTeam1(self):
        return self.team1
    
    def getTeam2(self):
        return self.team2
    
    def getCommandHandleRespon(self):
        return self.command_handle_respon
    
    def getSoulList(self):
        return self.soul_list

    # 请善待这个方法
    def respond(self, status: ResponseStatus, actor: Hero = None):

        # print  当前响应时机为:
        # DEBUG----------- 当前响应时机为
        Log().show_debug_info('DEBUG------- 当前响应时机为: {}'.format(status))

        # 检索所有战法，并根据战法响应
        for skill in self.getCommandHandleRespon():
            skill: Skill
            respon_list = skill.get_战法响应时机列表()
            Log().show_debug_info('DEBUG------- 当前检索战法响应时机为: {}'.format(respon_list))

            if status in respon_list:
                hero: Hero = skill.get_持有者()
                heroName = hero.get_武将名称()
                Log().show_debug_info('DEBUG------- 当前检索成功 武将: {}'.format(heroName))
                skillName = skill.get_战法名称()
                Log().show_debug_info('DEBUG------- 当前检索成功 战法: {}'.format(skillName))

                if skillName == SkillName.星罗棋布:
                    if status == ResponseStatus.阵型结束:
                        Log().show_battle_info('  [{}]发动战法【{}】'.format(heroName.value, skillName.value))
                        def 星罗棋布_阵型强化效果(self): 
                            for soul in 对己方阵型强化SOUL生效(skill, self):
                                soul: Soul
                                targetHero = soul.target
                                target_name = targetHero.get_武将名称().value

                                # 判断已经存在 星罗棋布_阵型强化效果的soul continue
                                is_exist = False
                                for exist_soul in self.getSoulList():
                                    if exist_soul.sourceType == SoulSourceType.星罗棋布_阵型强化 and exist_soul.target == targetHero and exist_soul.effect_type == soul.effect_type and exist_soul.skill == skill:
                                        is_exist = True
                                        break
                                if is_exist:
                                    continue

                                Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-阵型]效果'.format(target_name, skillName.value))
                                strengRatio = skill.星罗棋布_阵型强化系数() * soul.effect_value
                                newSoul = Soul(target=soul.target, sourceType=SoulSourceType.星罗棋布_阵型强化, skill=skill, effect_type=soul.effect_type, effect_value=strengRatio)
                                newSoul.deploy_initial()
                                self.getSoulList().append(newSoul)
                        星罗棋布_阵型强化效果(self)
                    elif status == ResponseStatus.战法布阵开始:
                        Log().show_battle_info('  [{}]发动战法【{}】'.format(heroName.value, skillName.value))
                        def 星罗棋布_谋略减伤效果():
                            valueList = 对己方所有目标生效(skill, self)
                            for hero in valueList:
                                reduce_value = skill.星罗棋布_受到谋略伤害降低系数()
                                if hero == skill.get_持有者():
                                    reduce_value = reduce_value * 1.3
                                soul = Soul(target=hero, 
                                        initiator=skill.get_持有者(), 
                                        sourceType=SoulSourceType.武将战法, 
                                        skill=skill, 
                                        effect_type=SoulEffectType.受到谋略伤害, 
                                        effect_value= - reduce_value)
                                soul.deploy_initial()
                                self.getSoulList().append(soul)
                        星罗棋布_谋略减伤效果()

                        Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-额外效果]效果'.format(heroName.value, skillName.value))
                        def 星罗棋布_额外效果():
                            if msg_判断己方前排武将数量(skill, self) == 1:
                                Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-单前排阵型]效果'.format(heroName.value, skillName.value))
                                frontLineHero = msg_对我方的单前排生效(skill, self)

                                lock_soul = Soul(target=frontLineHero,
                                                initiator=skill.get_持有者(), 
                                                sourceType=SoulSourceType.武将战法, 
                                                skill=skill, 
                                                effect_type=SoulEffectType.固定受击率, 
                                                effect_value=0.85)
                                lock_soul.deploy_initial()
                                self.getSoulList().append(lock_soul)

                                soul = Soul(target=frontLineHero, 
                                            initiator=skill.get_持有者(), 
                                            sourceType=SoulSourceType.武将战法, 
                                            skill=skill, 
                                            effect_type=SoulEffectType.受到伤害, 
                                            effect_value= - skill.星罗棋布_单前排_受到伤害降低系数())
                                soul.deploy_initial()
                                self.getSoulList().append(soul)                    
                            elif msg_判断己方前排武将数量(skill, self) == 2:
                                Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-双前排阵型]效果'.format(heroName.value, skillName.value))
                                lowest_ts_hero = msg_对我方统帅最低的武将(skill, self)

                                soul = Soul(target=lowest_ts_hero, 
                                                initiator=skill.get_持有者(), 
                                                sourceType=SoulSourceType.武将战法, 
                                                skill=skill, 
                                                effect_type=SoulEffectType.对前排造成伤害, 
                                                effect_value= skill.星罗棋布_双前排_对前排造成伤害提升系数())
                                soul.deploy_initial()
                                self.getSoulList().append(soul)

                                murder_soul = Soul(target=lowest_ts_hero,
                                                   initiator=skill.get_持有者(),
                                                   sourceType=SoulSourceType.武将战法,
                                                   skill=skill,
                                                   effect_type=SoulEffectType.借刀_星罗棋布_双前排阵型)
                                murder_soul.deploy_initial()
                                self.getSoulList().append(murder_soul)
                                skill.get_Soul_list().append(murder_soul)
                            elif msg_判断己方前排武将数量(skill, self) == 3:
                                Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-三前排阵型]效果'.format(heroName.value, skillName.value))
                                lowest_ts_hero = msg_对我方智力最高的武将(skill, self)

                                soul = Soul(target=lowest_ts_hero, 
                                                initiator=skill.get_持有者(), 
                                                sourceType=SoulSourceType.武将战法, 
                                                skill=skill, 
                                                effect_type=SoulEffectType.借刀_星罗棋布_三前排阵型)
                                soul.deploy_initial()
                                self.getSoulList().append(soul)
                                skill.get_Soul_list().append(soul)
                        星罗棋布_额外效果()
                    elif status == ResponseStatus.回合行动时:
                        soul_list = skill.get_Soul_list()
                        for soul in soul_list:
                            soul: Soul
                            if soul.effect_type == SoulEffectType.借刀_星罗棋布_双前排阵型 and soul.target == actor:
                                # 对敌军随机1-2人造成160%伤害(伤害类型由武力或智力高的一项决定)
                                Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-双前排阵型]效果'.format(heroName.value, skillName.value))

                                # 发起攻击的武将
                                atta_hero = soul.target
                                attacked_heroes = 对敌方所有目标生效(skill, self)

                                # 发起攻击次数
                                attack_times = int_随机一到两个敌方()
                                for i in range(attack_times):
                                    attacked: Hero = 从队列确定受击武将(attacked_heroes)
                                    attacked_heroes.remove(attacked)
                                    Log().show_battle_info('        [{}]对 [{}] 发起攻击'.format(atta_hero.get_武将名称().value, attacked.get_武将名称().value))
                                    value = 计算伤害(self, atta_hero, attacked, DamageType.择优, SkillType.指挥, 伤害值= 1.6)
                                    Log().show_battle_info('        [{}]对 [{}] 造成伤害 {:.2f}'.format(atta_hero.get_武将名称().value, attacked.get_武将名称().value, value))
                    elif status == ResponseStatus.回合结束后:
                        # 对敌军全体造成60%谋略伤害(额外受全军累积治疗量影响)
                        pass

    def 重置武将状态(self):

        for hero in self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero, \
                    self.team2.firstHero, self.team2.secondHero, self.team2.thirdHero:
            hero: Hero
            Log().show_debug_info('DEBUG------- 武将初始化成功')
            hero.init_base_values()
            hero.init_battle_values()
 
    def 填充战法(self):
        
        order_list_hero = 武将行动队列(self)
        for hero in order_list_hero:
            hero: Hero
            hero_name = hero.get_武将名称().value
            Log().show_debug_info('DEBUG------- 填充布阵阶段战法 -- 当前武将队列【{}】'.format(hero_name))

        for hero in order_list_hero:

            hero: Hero
            hero_info = getattr(hero, HeroInfoKey.武将信息.value)
            hero_name = getattr(hero_info, HeroInfoKey.武将名称.value).value

            # 输出名
            Log().show_debug_info('DEBUG------- 填充指挥战法 -- 当前检索武将【{}】'.format(hero_name))

            D_SkillClass: Skill = getattr(hero, HeroInfoKey.D_SkillClass.value)

            F_SkillClass: Skill = getattr(hero, HeroInfoKey.F_SkillClass.value)

            S_SkillClass: Skill = getattr(hero, HeroInfoKey.S_SkillClass.value)


            # 查询三个战法 先加载 被动战法 再加载 指挥战法
            # 只有包含 SkillInfoKey.战法响应时机列表 : [ResponseStatus.阵型结束, ResponseStatus.战法布阵开始] 这两个的才会被加载
            for skill in [D_SkillClass, F_SkillClass, S_SkillClass]:
                # 被动
                if skill.加载状态 == True :
                    Log().show_debug_info('DEBUG------- 填充被动战法 -- 当前检索战法类型【{}】'.format(skill.战法类型()))
                    if skill.战法类型() == SkillType.被动:
                        self.getCommandHandleRespon().append(skill)
                        skill_name = getattr(skill.战法信息, SkillInfoKey.战法名称.value)
                        Log().show_debug_info('DEBUG------- 填充被动战法 -- 成功填充被动战法【{}】'.format(skill_name))

            for skill in [D_SkillClass, F_SkillClass, S_SkillClass]:
                # 指挥
                if skill.加载状态 == True :
                    Log().show_debug_info('DEBUG------- 填充指挥战法 -- 当前检索战法类型【{}】'.format(skill.战法类型()))
                    if skill.战法类型() == SkillType.指挥:
                        self.getCommandHandleRespon().append(skill)
                        skill_name = getattr(skill.战法信息, SkillInfoKey.战法名称.value)
                        Log().show_debug_info('DEBUG------- 填充指挥战法 -- 成功填充指挥战法【{}】'.format(skill_name))

            for skill in [D_SkillClass, F_SkillClass, S_SkillClass]:
                # 主动 && 追击
                if skill.加载状态 == True :
                    Log().show_debug_info('DEBUG------- 填充主动战法 -- 当前检索战法类型【{}】'.format(skill.战法类型()))
                    if skill.战法类型() == SkillType.主动 or skill.战法类型() == SkillType.追击:
                        self.getCommandHandleRespon().append(skill)
                        skill_name = getattr(skill.战法信息, SkillInfoKey.战法名称.value)
                        Log().show_debug_info('DEBUG------- 填充主动战法 -- 成功填充主动战法【{}】'.format(skill_name))


    def 列队布阵(self):
        Log().show_battle_info('[列队布阵阶段]')
 
        def 列队布阵_补给强化(self):
            # 当队伍的补给小于100时 队伍中存活的武将 造成的伤害降低10%
            if self.team1.teamInfo.supply < 100:
                Log().show_battle_info('  [{}]的补给为{},造成伤害降低{}%'.format(self.team1.teamInfo.teamName, self.team1.teamInfo.supply, 10))
                self.team1.造成伤害降低 -= 0.1
            else:
                Log().show_battle_info('  [{}]的补给为{},造成伤害降低{}%'.format(self.team1.teamInfo.teamName, self.team1.teamInfo.supply, 0))
            if self.team2.teamInfo.supply < 100:
                Log().show_battle_info('  [{}]的补给为{},造成伤害降低{}%'.format(self.team2.teamInfo.teamName, self.team2.teamInfo.supply, 10))
                self.team2.造成伤害降低 -= 0.1
            else:
                Log().show_battle_info('  [{}]的补给为{},造成伤害降低{}%'.format(self.team2.teamInfo.teamName, self.team2.teamInfo.supply, 0))

        def 列队布阵_阵型强化(self):
            for team in [self.team1, self.team2]:
                firstHero = team.firstHero
                secondHero = team.secondHero
                thirdHero = team.thirdHero
                if team.teamInfo.formation == Formation.一字阵:
                    Log().show_battle_info('  [{}]获得【阵型-一字阵】强化效果'.format(team.teamInfo.teamName))
                    # 队伍阵型为一字阵
                    # 三前排 收到的伤害降低 8%
                    # 中间受击率 34%

                    setattr(firstHero, HeroInfoKey.前排.value, True)
                    setattr(secondHero, HeroInfoKey.前排.value, True)
                    setattr(thirdHero, HeroInfoKey.前排.value, True)

                    setattr(firstHero, HeroInfoKey.受击率.value, 0.33)
                    setattr(secondHero, HeroInfoKey.受击率.value, 0.34)
                    setattr(thirdHero, HeroInfoKey.受击率.value, 0.33)

                    for hero in firstHero, secondHero, thirdHero:
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.08)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                elif team.teamInfo.formation == Formation.萁型阵:
                    Log().show_battle_info('  [{}]获得【阵型-萁型阵】强化效果'.format(team.teamInfo.teamName))
                    # 队伍阵型为萁型阵
                    # 一号位前排 受击率 60% 受到的伤害降低 6%
                    # 二三号位后排 受击率 20% 造成的伤害提升 12%

                    setattr(firstHero, HeroInfoKey.前排.value, True)
                    setattr(firstHero, HeroInfoKey.受击率.value, 0.6)
                    firstHero_soul = Soul(target=firstHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.06)
                    firstHero_soul.deploy_initial()
                    self.soul_list.append(firstHero_soul)

                    for hero in secondHero, thirdHero:
                        setattr(hero, HeroInfoKey.前排.value, False)
                        setattr(hero, HeroInfoKey.受击率.value, 0.2)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.造成伤害, effect_value=0.12)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                elif team.teamInfo.formation == Formation.雁型阵:
                    Log().show_battle_info('  [{}]获得【阵型-雁型阵】强化效果'.format(team.teamInfo.teamName))
                    # 队伍阵型为雁型阵
                    # 一号位后排 受击率 20% 造成的伤害提升 15%
                    # 二三号位前排 受击率 40% 统帅提升 20点
                    
                    setattr(firstHero, HeroInfoKey.前排.value, False)
                    setattr(firstHero, HeroInfoKey.受击率.value, 0.2)
                    firstHero_soul = Soul(target=firstHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.造成伤害, effect_value=0.15)
                    firstHero_soul.deploy_initial()
                    self.soul_list.append(firstHero_soul)

                    for hero in secondHero, thirdHero:
                        setattr(hero, HeroInfoKey.前排.value, True)
                        setattr(hero, HeroInfoKey.受击率.value, 0.4)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.统帅, effect_value=20)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                elif team.teamInfo.formation == Formation.方圆阵:
                    # 队伍阵型为方圆阵
                    # 一二号位前排 受击率 40% 受到的伤害降低 5%
                    # 三号位后排 受击率 20% 连击率提升 40%
                    Log().show_battle_info('  [{}]获得【阵型-方圆阵】强化效果'.format(team.teamInfo.teamName))
                    
                    for hero in firstHero, secondHero:
                        setattr(hero, HeroInfoKey.前排.value, True)
                        setattr(hero, HeroInfoKey.受击率.value, 0.4)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.05)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                    setattr(thirdHero, HeroInfoKey.前排.value, False)
                    setattr(thirdHero, HeroInfoKey.受击率.value, 0.2)
                    thirdHero_soul = Soul(target=thirdHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.连击, effect_value=0.4)
                    thirdHero_soul.deploy_initial()
                    self.soul_list.append(thirdHero_soul)

                elif team.teamInfo.formation == Formation.锥型阵:
                    # 队伍阵型为锥型阵
                    # 一三号位后排 受击率 20% 受到的伤害降低 5%
                    # 二号位前排 受击率 60% 造成的伤害提升 16%
                    Log().show_battle_info('  [{}]获得【阵型-锥型阵】强化效果'.format(team.teamInfo.teamName))
                    
                    for hero in firstHero, thirdHero:
                        setattr(hero, HeroInfoKey.前排.value, False)
                        setattr(hero, HeroInfoKey.受击率.value, 0.2)
                        soul = Soul( target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.05)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                    setattr(secondHero, HeroInfoKey.前排.value, True)
                    setattr(secondHero, HeroInfoKey.受击率.value, 0.6)
                    secondHero_soul = Soul(target=secondHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.造成伤害, effect_value=0.16)
                    secondHero_soul.deploy_initial()
                    self.soul_list.append(secondHero_soul)

                elif team.teamInfo.formation == Formation.鱼鳞阵:
                    # 队伍阵型为鱼鳞阵
                    # 一号位前排 受击率 60% 规避提升 12%
                    # 二三号位后排 受击率 20% 会心&奇谋提升 8%
                    Log().show_battle_info('  [{}]获得【阵型-鱼鳞阵】强化效果'.format(team.teamInfo.teamName))
                    
                    setattr(firstHero, HeroInfoKey.前排.value, True)
                    setattr(firstHero, HeroInfoKey.受击率.value, 0.6)
                    firstHero_soul = Soul(target=firstHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DodgeRate, effect_value=0.12)
                    firstHero_soul.deploy_initial()
                    self.soul_list.append(firstHero_soul)

                    for hero in secondHero, thirdHero:
                        setattr(hero, HeroInfoKey.前排.value, False)
                        setattr(hero, HeroInfoKey.受击率.value, 0.2)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.CriticalRate, effect_value=0.08)
                        soul.deploy_initial()
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.MagnificentRate, effect_value=0.08)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                elif team.teamInfo.formation == Formation.钩型阵:
                    # 队伍阵型为钩型阵
                    # 一二号位后排 受击率 20% 连击率提升 25%
                    # 三号位前排 受击率 60% 受到的伤害降低 8%
                    Log().show_battle_info('  [{}]获得【阵型-钩型阵】强化效果'.format(team.teamInfo.teamName))
                    
                    for hero in firstHero, secondHero:
                        setattr(hero, HeroInfoKey.前排.value, False)
                        setattr(hero, HeroInfoKey.受击率.value, 0.2)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.连击, effect_value=0.25)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                    setattr(thirdHero, HeroInfoKey.前排.value, True)
                    setattr(thirdHero, HeroInfoKey.受击率.value, 0.6)
                    thirdHero_soul = Soul(target=thirdHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.08)
                    thirdHero_soul.deploy_initial()
                    self.soul_list.append(thirdHero_soul)

                elif team.teamInfo.formation == Formation.偃月阵:
                    # 队伍阵型为偃月阵
                    # 一三号位前排 受击率 40% 造成的伤害提升 14%
                    # 二号位后排 受击率 20% 受到的伤害降低 5%
                    Log().show_battle_info('  [{}]获得【阵型-偃月阵】强化效果'.format(team.teamInfo.teamName))
                    
                    for hero in firstHero, thirdHero:
                        setattr(hero, HeroInfoKey.前排.value, True)
                        setattr(hero, HeroInfoKey.受击率.value, 0.4)
                        soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.造成伤害, effect_value=0.14)
                        soul.deploy_initial()
                        self.soul_list.append(soul)

                    setattr(secondHero, HeroInfoKey.前排.value, False)
                    setattr(secondHero, HeroInfoKey.受击率.value, 0.2)
                    secondHero_soul = Soul(target=secondHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.受到伤害, effect_value=-0.05)
                    secondHero_soul.deploy_initial()
                    self.soul_list.append(secondHero_soul)

                self.respond(ResponseStatus.阵型结束)

        def 列队布阵_阵营强化(self):
            for team in [self.team1, self.team2]:
                firstHero = team.firstHero
                secondHero = team.secondHero
                thirdHero = team.thirdHero

                firstHero_country = getattr(getattr(firstHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将阵营.value).value
                secondHero_country = getattr(getattr(secondHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将阵营.value).value
                thirdHero_country = getattr(getattr(thirdHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将阵营.value).value
                
                if (firstHero_country == secondHero_country and secondHero_country == thirdHero_country):
                    bonus = 0.1
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【{firstHero_country}】强化效果,属性提升{bonus*100}%')
                    for hero in firstHero, secondHero, thirdHero:
                        for effectType in [SoulEffectType.武力, SoulEffectType.智力, SoulEffectType.统帅, SoulEffectType.先攻]:
                            # 取出当前的值 * 0.05 后相加
                            current_value = getattr(hero, effectType.value)
                            real_value = current_value * bonus
                            soul = Soul(target=hero, effect_type=effectType, effect_value=real_value)
                            soul.deploy_initial()
                elif (firstHero_country == secondHero_country or secondHero_country == thirdHero_country or firstHero_country == thirdHero_country):
                    if secondHero_country == thirdHero_country:
                        same_country = secondHero_country
                    else:
                        same_country = firstHero_country

                    bonus = 0.05
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【{same_country}】强化效果,属性提升 {bonus*100}%')
                    for hero in firstHero, secondHero, thirdHero:
                        for effectType in [SoulEffectType.武力, SoulEffectType.智力, SoulEffectType.统帅, SoulEffectType.先攻]:
                            # 取出当前的值 * 0.05 后相加
                            current_value = getattr(hero, effectType.value)
                            real_value = current_value * bonus
                            soul = Soul(target=hero, effect_type=effectType, effect_value=real_value) 
                            soul.deploy_initial()

        def 列队布阵_兵种强化(self):
            for team in [self.team1, self.team2]:

                firstHero = team.firstHero
                secondHero = team.secondHero
                thirdHero = team.thirdHero

                firstHero_army = getattr(getattr(firstHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将兵种.value).value
                secondHero_army = getattr(getattr(secondHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将兵种.value).value
                thirdHero_army = getattr(getattr(thirdHero, HeroInfoKey.武将信息.value), HeroInfoKey.武将兵种.value).value

                hypaspist = 0
                gunner = 0
                bowman = 0
                cavalryman = 0

                for heroWeaponType in firstHero_army, secondHero_army, thirdHero_army:
                    if heroWeaponType == WeaponType.盾.value:
                        hypaspist += 1
                    elif heroWeaponType == WeaponType.枪.value:
                        gunner += 1
                    elif heroWeaponType == WeaponType.弓.value:
                        bowman += 1
                    elif heroWeaponType == WeaponType.骑.value:
                        cavalryman += 1

                if hypaspist >= 2:
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-盾】强化效果')
                    for hero in firstHero, secondHero, thirdHero:
                        if hypaspist == 3:
                            soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.05)
                        else:
                            soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.035)
                        soul.deploy_initial()
                elif gunner >= 2:
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-枪】强化效果')
                    for hero in firstHero, secondHero, thirdHero:
                        if gunner == 3:
                            increase_soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.03)
                            reduce_soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.02)
                        else:
                            increase_soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.021)
                            reduce_soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.014)

                        increase_soul.deploy_initial()
                        reduce_soul.deploy_initial()
                elif bowman >= 2:
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-弓】强化效果')
                    for hero in firstHero, secondHero, thirdHero:
                        if bowman == 3:
                            soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.05)
                        else:
                            soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.035)
                        soul.deploy_initial()
                elif cavalryman >= 2:
                    Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-骑】强化效果')
                    for hero in firstHero, secondHero, thirdHero:
                        if cavalryman == 3:
                            increase_soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.02)
                            reduce_soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.03)
                        else:
                            increase_soul = Soul(target=hero, effect_type=SoulEffectType.造成伤害, effect_value=0.014)
                            reduce_soul = Soul(target=hero, effect_type=SoulEffectType.受到伤害, effect_value=-0.021)
                        increase_soul.deploy_initial()
                        reduce_soul.deploy_initial()

        列队布阵_补给强化(self)

        列队布阵_阵型强化(self)

        列队布阵_阵营强化(self)

        列队布阵_兵种强化(self)
 
    def simulate(self, team1: TeamInfo, team2: TeamInfo):

        self.team1_hero1 = Hero(team1.firstHeroInfo)
        self.team1_hero1.load_skill()
        setattr(self.team1_hero1, HeroInfoKey.TeamOrder.value, 1)

        self.team1_hero2 = Hero(team1.secondHeroInfo)
        self.team1_hero2.load_skill()
        setattr(self.team1_hero2, HeroInfoKey.TeamOrder.value, 2)
        self.team1_hero3 = Hero(team1.thirdHeroInfo)
        self.team1_hero3.load_skill()
        setattr(self.team1_hero3, HeroInfoKey.TeamOrder.value, 3)

        self.team2_hero1 = Hero(team2.firstHeroInfo)
        self.team2_hero1.load_skill()
        setattr(self.team2_hero1, HeroInfoKey.TeamOrder.value, 1)
        self.team2_hero2 = Hero(team2.secondHeroInfo)
        self.team2_hero2.load_skill()
        setattr(self.team2_hero2, HeroInfoKey.TeamOrder.value, 2)
        self.team2_hero3 = Hero(team2.thirdHeroInfo)
        self.team2_hero3.load_skill()
        setattr(self.team2_hero3, HeroInfoKey.TeamOrder.value, 3)

        self.team1 = Team(team1, self.team1_hero1, self.team1_hero2, self.team1_hero3)
        self.team2 = Team(team2, self.team2_hero1, self.team2_hero2, self.team2_hero3)

    def fight(self):

        for _ in range(1):
            Log().show_battle_info('\n[第 {} 局]'.format(_ + 1))
            self.command_handle_respon = []
            self.soul_list = []

            self.重置武将状态()

            self.填充战法()

            self.列队布阵()

            self.respond(ResponseStatus.战法布阵开始)

            # 八个回合
            for i in range(1):

                # 行动顺序判断
                order_list_hero = 武将行动队列(self)
                for hero in order_list_hero:
                    hero: Hero
                    hero_name = hero.get_武将名称().value
                    team_name = hero.get_队伍名称()
                    Log().show_debug_info('DEBUG------- 当前武将队列[{}]【{}】'.format(team_name, hero_name))

                self.respond(ResponseStatus.回合开始时)

                for hero in order_list_hero:
                    hero: Hero
                    hero_name = hero.get_武将名称().value
                    Log().show_battle_info('[{}]开始行动'.format(hero.get_武将名称().value))
                    self.respond(ResponseStatus.回合行动时, actor=hero)

                self.respond(ResponseStatus.回合结束时)

                self.respond(ResponseStatus.回合结束后)



        return True
    