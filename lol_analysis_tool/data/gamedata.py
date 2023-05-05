import datetime
import json
from lol_analysis_tool.data.participants import Participants, queue_id


class GameData:
    def __init__(self, file_path):
        file = open(file_path)
        game = json.load(file)
        game = game['info']
        stamp = game['gameCreation']
        self.date = datetime.date.fromtimestamp(stamp / 1e3)
        self.id = game['gameId']
        self.patch = game['gameVersion']
        self.platform = game['platformId']

        self.game_type_id = game['queueId']
        self.duration = game['gameDuration'] / 60

        self.participants = game['participants'] # list of dict for each player
        self.player_list = self.player_info() # list of participant created from participant dict

        self.teams = game['teams'] # list of 2 dicts
        self.team1 = self.teams[0]
        self.team1_objectives = self.team1['objectives']
        self.team2 = self.teams[1]
        self.team2_objectives = self.team2['objectives']

    def __repr__(self):
        print(f"GameData representation:\n"
              f"Game ID: {self.id}, Game type: {queue_id[self.game_type_id]}\n"
              f"Patch: {self.patch}, Platform: {self.platform}\n"
              f"Game duration: {self.duration}\n")

    def player_info(self):
        lst = []
        for summoner in self.participants:
            p = Participants(summoner)
            lst.append(p)
        return lst
