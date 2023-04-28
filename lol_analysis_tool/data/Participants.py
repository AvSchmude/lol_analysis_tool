import pprint

queue_id = {400: 'Draft Pick',
            420: 'Ranked Solo',
            440: 'Ranked Flex',
            450: 'Aram'}


class Participants:
    def __init__(self, p):
        try:
            self.player_name = p['summonerName']
            self.player_level = p['summonerLevel']
            self._player_puuid = p['puuid']
            self._summoner_id = p['summonerId']

            self.team_id = p['teamId']
            self.game_won = p['win']
            self.game_surrendered = p['gameEndedInSurrender']
            self.game_early_surrendered = p['gameEndedInSurrender']

            self.champion = p['championName']
            self.champion_level = p['champLevel']
            self.position = p['individualPosition']
            if self.position == 'UTILITY':
                self.position = 'SUPPORT'
            self.kills = p['kills']
            self.assists = p['assists']
            self.deaths = p['deaths']
            self.kda = (self.kills + self.assists) / self.deaths

            self.vision_score = p['visionScore']
            self.vision_wards_placed = p['wardsPlaced']
            self.vision_pinks_placed = p['detectorWardsPlaced']
            self.vision_wards_killed = p['wardsKilled']

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
            self.damage_shielded_teammates = p['totalDamageShieldedOnTeammates']

            self.minions_killed_total = p['totalMinionsKilled']
            self.minions_killed_neutral = p['neutralMinionsKilled']

            self.turret_kills = p['turretKills']
            self.longest_time_alive = p['longestTimeSpentLiving']

            self.count_spell1 = p['spell1Casts']
            self.count_spell2 = p['spell2Casts']
            self.count_spell3 = p['spell3Casts']
            self.count_spell4 = p['spell4Casts']

            self.count_pings = 0
            for key in p.keys():
                if "Pings" in key:
                    self.count_pings += p[key]

            self.gold_earned = p['goldEarned']
            self.gold_spent = p['goldSpent']

            self.item_ids = [p['item0'],
                             p['item1'],
                             p['item2'],
                             p['item3'],
                             p['item4'],
                             p['item5'],
                             p['item6']]
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
        data = list(self.__dict__.values())
        print(data)
