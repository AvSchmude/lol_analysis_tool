import pprint

queue_id = {400: 'Draft Pick',
            420: 'Ranked Solo',
            440: 'Ranked Flex',
            450: 'Aram'}


class Participants:
    def __init__(self, p):
        try:
            self.name = p['summonerName']
            # self.player_level = p['summonerLevel']
            # self._player_puuid = p['puuid']
            # self._summoner_id = p['summonerId']
            if p['teamId'] == 100:
                self.team_colour = 'blue'
            else:
                self.team_colour = 'red'
            self.win = p['win']
            self.surrender = p['gameEndedInSurrender']
            # self.game_early_surrendered = p['gameEndedInSurrender']
            self.champion = p['championName']
            self.champion_level = p['champLevel']
            self.position = p['individualPosition']
            if self.position == 'UTILITY':
                self.position = 'SUPPORT'
            self.kills = p['kills']
            self.assists = p['assists']
            self.deaths = p['deaths']

            self.minions_killed = p['totalMinionsKilled']
            self.monsters_killed = p['neutralMinionsKilled']
            self.creep_score = self.minions_killed + self.monsters_killed
            self.gold_earned = p['goldEarned']
            self.gold_spent = p['goldSpent']

            self.first_blood = p['firstBloodKill']
            self.first_tower = p['firstTowerKill']

            self.damage_dealt_total = p['totalDamageDealtToChampions']
            self.damage_dealt_magic = p['magicDamageDealtToChampions']
            self.damage_dealt_physical = p['physicalDamageDealtToChampions']
            self.damage_dealt_true = p['trueDamageDealtToChampions']
            self.damage_dealt_objectives = p['damageDealtToObjectives']
            self.damage_dealt_turrets = p['damageDealtToTurrets']

            self.damage_taken_total = p['totalDamageTaken']
            self.damage_taken_magic = p['magicDamageTaken']
            self.damage_taken_physical = p['physicalDamageTaken']
            self.damage_taken_true = p['trueDamageTaken']

            self.healing_total = p['totalHeal']
            self.healing_teammates = p['totalHealsOnTeammates']
            self.shielding_teammates = p['totalDamageShieldedOnTeammates']

            self.vision_score = p['visionScore']
            self.wards_placed = p['wardsPlaced']
            self.pinks_placed = p['detectorWardsPlaced']
            self.wards_killed = p['wardsKilled']

            self.turret_kills = p['turretKills']
            self.longest_time_alive = p['longestTimeSpentLiving']

            self.spell_count_q = p['spell1Casts']
            self.spell_count_w = p['spell2Casts']
            self.spell_count_e = p['spell3Casts']
            self.spell_count_r = p['spell4Casts']

            self.ping_count = 0
            for key in p.keys():
                if "Pings" in key:
                    self.ping_count += p[key]

            self.item0_id = p['item0']
            self.item1_id = p['item1']
            self.item2_id = p['item2']
            self.item3_id = p['item3']
            self.item4_id = p['item4']
            self.item5_id = p['item5']
            self.item6_id = p['item6']

        except KeyError:
            print(traceback.format_exc())

    def __repr__(self):
        print(f"Name: {self.player_name}, Level: {self.player_level}\n"
              f"Team: {self.team_id}, Game won: {self.game_won}, Surrendered: "
              f"{self.game_surrendered}/{self.game_early_surrendered}\n"
              f"Champion: {self.champion}, Level: {self.champion_level}, Position: {self.position}\n"
              f"Kills {self.kills}, Death {self.deaths}, Assists {self.assists}, KDA {self.kda}\n"
              f"Vision score: {self.vision_score}\n"
              f"Damage dealt: {self.damage_dealt_total}\n"
              f"Damage taken: {self.damage_taken_total}\n"
              f"Healing done: {self.healing_total}\n"
              f"Creep score: {self.minions_killed_total+self.minions_killed_neutral}\n"
              f"Longest time alive: {self.longest_time_alive}\n"
              f"Number of pings: {self.count_pings}")

    def to_dict(self):
        pprint.pprint(self.__dict__, sort_dicts=False)

    def to_list(self):
        variables = self.__dict__.keys()
        print(len(variables))

    def prep_for_database(self):
        from lol_analysis_tool.endpoints.tables import part_keywords
        data = []
        print(list(set(part_keywords) - set(self.__dict__.keys())))
        for key in part_keywords:
            if key in self.__dict__.keys():
                data.append(self.__dict__[key])
            else:
                continue
        # print(len(part_keywords), len(data), data)
        return data
