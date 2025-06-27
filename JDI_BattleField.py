
from JDI_Log import Log
from JDI_Enum import ResponseStatus, SkillType, SkillName, SkillInfoKey, WeaponType, HeroInfoKey, Formation, SoulSourceType, SoulEffectType
from JDI_Hero import Hero
from JDI_Team import TeamInfo, Team
from JDI_Soul import Soul
from JDI_Calculate import 重置武将状态, sort_action_order

class BattleField():

    # 获取队伍中统帅最低的武将
    def get_lowest_ts_hero(self, team):
        lowest_ts_hero = None
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if getattr(hero, HeroInfoKey.被击溃状态.value) != True:
                if lowest_ts_hero == None:
                    lowest_ts_hero = hero
                elif getattr(hero, HeroInfoKey.初始统帅.value) < getattr(lowest_ts_hero, HeroInfoKey.初始统帅.value):
                    lowest_ts_hero = hero
        return lowest_ts_hero

    # 取出一个前排武将
    def get_one_frontline_hero(self, team):
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.前排.value) == True:
                return hero

    # 判断队伍中有几个前排
    def count_frontline_heroes(self, team):
        frontLineCount = 0
        for hero in team.firstHero, team.secondHero, team.thirdHero:
            if getattr(hero, HeroInfoKey.被击溃状态.value) != True and getattr(hero, HeroInfoKey.前排.value) == True:
                frontLineCount += 1
        return frontLineCount

    # 判断两个武将是否属于同一队伍
    def is_same_team(self, hero1, hero2):
        if hero1 in [self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero]:
            return hero2 in [self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero]
        elif hero2 in [self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero]:
            return hero1 in [self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero]

    # 将队伍中被击溃的武将剔除
    def remove_breakdown_heroes(self, heroList):
        return list(filter(lambda x: not getattr(x, HeroInfoKey.被击溃状态.value), [heroList.firstHero, heroList.secondHero, heroList.thirdHero]))

    # 获取技能所属队伍
    def get_team_by_skill(self, skill):
        owner = skill.owner
        if owner in [self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero]:
            return self.team1
        elif owner in [self.team2.firstHero, self.team2.secondHero, self.team2.thirdHero]:
            return self.team2

    # 请善待这个方法
    def respond(self, status):
        for skill in self.command_handle_respon:
            skillInfo = skill.skillInfo
            if hasattr(skillInfo, SkillInfoKey.战法名称.value):
                respon_list = getattr(skillInfo, SkillInfoKey.战法响应时机列表.value)
                if status in respon_list:
                    skillName = getattr(skillInfo, SkillInfoKey.战法名称.value)
                    if skillName == SkillName.星罗棋布:
                        if status == ResponseStatus.阵型结束:
                            Log().show_battle_info('  [{}]发动战法【{}】'.format(skill.owner.武将信息.武将名称.value, skillName.value))
                            def 星罗棋布_阵型强化效果(self): 
                                for soul in self.soul_list:
                                    if soul.sourceType == SoulSourceType.阵型加成:
                                        isCheckSoul = False
                                        for checkSoul in self.soul_list:
                                            if self.is_same_team(skill.owner, checkSoul.target) and checkSoul.target == soul.target and checkSoul.sourceType == SoulSourceType.星罗棋布_阵型加成 and checkSoul.effect_type == soul.effect_type:
                                                isCheckSoul = True
                                                break
                                        if isCheckSoul == False:
                                            targetHero = soul.target
                                            target_Info = getattr(targetHero, HeroInfoKey.武将信息.value)
                                            target_name = getattr(target_Info, HeroInfoKey.武将名称.value).value
                                            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-阵型]效果'.format(target_name, skillName.value))
                                            strengRatio = skill.get_Strength_enhancement() * soul.effect_value
                                            newSoul = Soul(target=soul.target, sourceType=SoulSourceType.星罗棋布_阵型加成, skill=skill, effect_type=soul.effect_type, effect_value=strengRatio)
                                            newSoul.deploy_initial()
                                            self.soul_list.append(newSoul)
                            星罗棋布_阵型强化效果(self)
                        elif status == ResponseStatus.战法布阵开始:
                            Log().show_battle_info('  [{}]发动战法【{}】'.format(skill.owner.武将信息.武将名称.value, skillName.value))
                            def 星罗棋布_谋略减伤效果():
                                valueList = self.remove_breakdown_heroes(self.get_team_by_skill(skill))
                                for hero in valueList:
                                    reduce_value = skill.get_Damage_reduction_strategy()
                                    if hero == skill.owner:
                                        reduce_value = reduce_value * 1.3
                                    soul = Soul(target=hero, 
                                            initiator=skill.owner, 
                                            sourceType=SoulSourceType.heroSkill, 
                                            skill=skill, 
                                            effect_type=SoulEffectType.DamageReduce_MagniRate, 
                                            effect_value= - reduce_value)
                                    soul.deploy_initial()
                                    self.soul_list.append(soul)
                            星罗棋布_谋略减伤效果()
                            owner_name = getattr(skill.owner.武将信息, HeroInfoKey.武将名称.value).value
                            Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-额外效果]效果'.format(owner_name, skillName.value))
                            def 星罗棋布_额外效果():
                                if self.count_frontline_heroes(self.get_team_by_skill(skill)) == 1:
                                    Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-单前排阵型]效果'.format(owner_name, skillName.value))
                                    frontLineHero = self.get_one_frontline_hero(self.get_team_by_skill(skill))
                                    setattr(frontLineHero, HeroInfoKey.锁定受击率.value, True)
                                    Log().show_battle_info('        [{}]的固定受击率锁定为85%'.format(owner_name))
                                    reduce_value = skill.get_Damage_reduction()
                                    soul = Soul(target=frontLineHero, 
                                                initiator=skill.owner, 
                                                sourceType=SoulSourceType.heroSkill, 
                                                skill=skill, 
                                                effect_type=SoulEffectType.DamageReduce, 
                                                effect_value= - reduce_value)
                                    soul.deploy_initial()
                                    self.soul_list.append(soul)
                                elif self.count_frontline_heroes(self.get_team_by_skill(skill)) == 2:
                                    Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-双前排阵型]效果'.format(owner_name, skillName.value))
                                    # 取出统帅最低的未被击溃的武将
                                    lowest_ts_hero = self.get_lowest_ts_hero(self.remove_breakdown_heroes(self.get_team_by_skill(skill)))

                                    soul = Soul(target=lowest_ts_hero, 
                                                    initiator=skill.owner, 
                                                    sourceType=SoulSourceType.heroSkill, 
                                                    skill=skill, 
                                                    effect_type=SoulEffectType.DamageReduce, 
                                                    effect_value= - skill.get_Damage_reduction())
                                    soul.deploy_initial()
                                    self.soul_list.append(soul)
                                elif self.count_frontline_heroes(self.get_team_by_skill(skill)) == 3:
                                    Log().show_battle_info('        [{}]执行来自【{}】的[星罗棋布-三前排阵型]效果'.format(owner_name, skillName.value))
                            星罗棋布_额外效果()

    # 列队布阵 - 补给
    def arrange_formation_supply(self):
        # 当队伍的补给小于100时 队伍中存活的武将 造成的伤害降低10%
        if self.team1.teamInfo.supply < 100:
            Log().show_battle_info('  [{}]的补给为{}，造成伤害降低{}%'.format(self.team1.teamInfo.teamName, self.team1.teamInfo.supply, 10))
            for hero in self.team1.firstHero, self.team1.secondHero, self.team1.thirdHero:
                soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=-0.1)
                soul.deploy_initial()
        else:
            Log().show_battle_info('  [{}]的补给为{}，造成伤害降低{}%'.format(self.team1.teamInfo.teamName, self.team1.teamInfo.supply, 0))
        if self.team2.teamInfo.supply < 100:
            Log().show_battle_info('  [{}]的补给为{}，造成伤害降低{}%'.format(self.team2.teamInfo.teamName, self.team2.teamInfo.supply, 10))
            for hero in self.team2.firstHero, self.team2.secondHero, self.team2.thirdHero:
                soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=-0.1)
                soul.deploy_initial()
        else:
            Log().show_battle_info('  [{}]的补给为{}，造成伤害降低{}%'.format(self.team2.teamInfo.teamName, self.team2.teamInfo.supply, 0))

     # 列队布阵 - 阵型强化阶段
    
    # 列队布阵 - 阵型
    def arrange_formation_strength(self):
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
                    soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.08)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

            elif team.teamInfo.formation == Formation.萁型阵:
                Log().show_battle_info('  [{}]获得【阵型-萁型阵】强化效果'.format(team.teamInfo.teamName))
                # 队伍阵型为萁型阵
                # 一号位前排 受击率 60% 受到的伤害降低 6%
                # 二三号位后排 受击率 20% 造成的伤害提升 12%

                setattr(firstHero, HeroInfoKey.前排.value, True)
                setattr(firstHero, HeroInfoKey.受击率.value, 0.6)
                firstHero_soul = Soul(target=firstHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.06)
                firstHero_soul.deploy_initial()
                self.soul_list.append(firstHero_soul)

                for hero in secondHero, thirdHero:
                    setattr(hero, HeroInfoKey.前排.value, False)
                    setattr(hero, HeroInfoKey.受击率.value, 0.2)
                    soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageIncrease, effect_value=0.12)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

            elif team.teamInfo.formation == Formation.雁型阵:
                Log().show_battle_info('  [{}]获得【阵型-雁型阵】强化效果'.format(team.teamInfo.teamName))
                # 队伍阵型为雁型阵
                # 一号位后排 受击率 20% 造成的伤害提升 15%
                # 二三号位前排 受击率 40% 统帅提升 20点
                
                setattr(firstHero, HeroInfoKey.前排.value, False)
                setattr(firstHero, HeroInfoKey.受击率.value, 0.2)
                firstHero_soul = Soul(target=firstHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageIncrease, effect_value=0.15)
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
                    soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.05)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

                setattr(thirdHero, HeroInfoKey.前排.value, False)
                setattr(thirdHero, HeroInfoKey.受击率.value, 0.2)
                thirdHero_soul = Soul(target=thirdHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.ChainHit, effect_value=0.4)
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
                    soul = Soul( target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.05)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

                setattr(secondHero, HeroInfoKey.前排.value, True)
                setattr(secondHero, HeroInfoKey.受击率.value, 0.6)
                secondHero_soul = Soul(target=secondHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageIncrease, effect_value=0.16)
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
                    soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.ChainHit, effect_value=0.25)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

                setattr(thirdHero, HeroInfoKey.前排.value, True)
                setattr(thirdHero, HeroInfoKey.受击率.value, 0.6)
                thirdHero_soul = Soul(target=thirdHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.08)
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
                    soul = Soul(target=hero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageIncrease, effect_value=0.14)
                    soul.deploy_initial()
                    self.soul_list.append(soul)

                setattr(secondHero, HeroInfoKey.前排.value, False)
                setattr(secondHero, HeroInfoKey.受击率.value, 0.2)
                secondHero_soul = Soul(target=secondHero, sourceType=SoulSourceType.阵型加成, effect_type=SoulEffectType.DamageReduce, effect_value=-0.05)
                secondHero_soul.deploy_initial()
                self.soul_list.append(secondHero_soul)

            self.respond(ResponseStatus.阵型结束)

    # 列队布阵 - 阵营
    def arrange_formation_campaign(self):
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

    # 列队布阵 - 兵种
    def arrange_formation_army(self):
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
                        soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.05)
                    else:
                        soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.035)
                    soul.deploy_initial()
            elif gunner >= 2:
                Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-枪】强化效果')
                for hero in firstHero, secondHero, thirdHero:
                    if gunner == 3:
                        increase_soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.03)
                        reducte_soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.02)
                    else:
                        increase_soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.021)
                        reduce_soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.014)

                    increase_soul.deploy_initial()
                    reduce_soul.deploy_initial()
            elif bowman >= 2:
                Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-弓】强化效果')
                for hero in firstHero, secondHero, thirdHero:
                    if bowman == 3:
                        soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.05)
                    else:
                        soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.035)
                    soul.deploy_initial()
            elif cavalryman >= 2:
                Log().show_battle_info(f' 【{team.teamInfo.teamName}】获得【兵种-骑】强化效果')
                for hero in firstHero, secondHero, thirdHero:
                    if cavalryman == 3:
                        increase_soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.02)
                        reduce_soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.03)
                    else:
                        increase_soul = Soul(target=hero, effect_type=SoulEffectType.DamageIncrease, effect_value=0.014)
                        reduce_soul = Soul(target=hero, effect_type=SoulEffectType.DamageReduce, effect_value=-0.021)
                    increase_soul.deploy_initial()
                    reduce_soul.deploy_initial()

    # 列队布阵
    def arrange_fight(self):
        Log().show_battle_info('[列队布阵阶段]')

        self.arrange_formation_supply()

        self.arrange_formation_strength()

        self.arrange_formation_campaign()

        self.arrange_formation_army()

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

        for _ in range(8):
            Log().show_battle_info('\n[第 {} 局]'.format(_ + 1))
            self.command_handle_respon = []
            self.soul_list = []

            重置武将状态(self)

            order_list_hero = sort_action_order(self.team1, self.team2)
            for hero in order_list_hero:
                D_SkillClass = getattr(hero, HeroInfoKey.D_SkillClass.value)
                if D_SkillClass.加载状态 == True:
                    if D_SkillClass.战法类型 == SkillType.指挥:
                        self.command_handle_respon.append(D_SkillClass)

            self.arrange_fight()

            self.respond(ResponseStatus.战法布阵开始)

        return True