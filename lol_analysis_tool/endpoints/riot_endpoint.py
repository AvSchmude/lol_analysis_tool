import os
import pprint
import traceback
import requests
import json
from lol_analysis_tool.config import riot_api


class RiotEndpoint:
    def __init__(self):
        self.key = riot_api
        self.url = r'https://euw1.api.riotgames.com'
        self.url2 = r'https://europe.api.riotgames.com'
        self.queueId = {400: 'Draft Pick',
                        420: 'Ranked Solo',
                        440: 'Ranked Flex',
                        450: 'Aram'}

    def request_matches(self, name, queueid, type='ranked', count=100):
        """Requests match history and timelines based on summoner name

        :param str name: Summoner name
        :param int queueid: Queue ID
        :param str type: Game type
        :param int count: Number of matches
        """
        query = self.request_summoner_by_name(name)
        puuid = query.json()['puuid']
        match_ids = list(self.request_match_ids(puuid, queueid, type, count).json())
        matches, timelines = self.request_matches_from_id_list(match_ids)
        return matches, timelines

    def request_summoner_by_name(self, name):
        """Request the summoner data by summoner name.

        :param name: str Summoner name
        :return: Response containing summoner information
        """
        query = requests.get(url=f'{self.url}/lol/summoner/v4/summoners/by-name/{name}',
                             headers={'X-Riot-Token': self.key})
        return query

    def request_match_ids(self, puuid, queueid, type='ranked', count=100):
        """Requests match ids using summoner puuid.

        :param int puuid: summoner ID
        :param int queueid: game type ID
        :param str type: game type description
        :param int count: number of match IDs
        """
        match_ids = requests.get(url=f'{self.url2}/lol/match/v5/matches/by-puuid/{puuid}/ids',
                                 params={'queue': queueid, 'type': type, 'count': count},
                                 headers={'X-Riot-Token': self.key})
        return match_ids

    def request_matches_from_id_list(self, id_list):
        """Requests match history and timelines for each ID.

        Writes match history and timeline data into json files.
        Returns two dictionaries storing match histories and timelines separately.

        :param list id_list: List containing match IDs
        """
        matches = {}
        timelines = {}
        for match_id in id_list:
            match = requests.get(url=f'{self.url2}/lol/match/v5/matches/{match_id}', headers={'X-Riot-Token': self.key})
            match_data = json.dumps(match.json(), indent=4, separators=(',', ': '), sort_keys=True)
            matches[match_id] = match_data
            # match_path = os.path.join(os.path.dirname(r'.\data\files\ranked_solo\.'), f'{match_id}_match.json')
            # with open(match_path, 'w') as f:
            #    f.write(match_data)

            timeline = requests.get(url=f'{self.url2}/lol/match/v5/matches/{match_id}/timeline', headers={'X-Riot-Token': self.key})
            timeline_data = json.dumps(timeline.json(), indent=4, separators=(',', ': '), sort_keys=True)
            timelines[match_id] = timeline_data
            # timeline_path = os.path.join(os.path.dirname(r'.\data\files\timelines\.'), f'{match_id}_timeline.json')
            # with open(timeline_path, 'w') as f:
            #    f.write(timeline_data)
        return matches, timelines

    @staticmethod
    def write_summoner_data_to_json(name, summoner):
        data = json.dumps(summoner.json(), indent=4, separators=(',', ': '), sort_keys=True)
        with open(f'{name}.json', 'w') as file:
            file.write(data)

    @staticmethod
    def read_active_queues():
        queues = []
        file_path = r'S:\ProgProjects\PythonProjects\lol_analysis_tool\lol_analysis_tool\data\files\queues.json'
        with open(file_path, 'r') as f:
            data = json.load(f)
            for elem in data:
                if elem['notes'] is None and elem['description'] is not None:
                    queues.append(elem)

        new_path = r'S:\ProgProjects\PythonProjects\lol_analysis_tool\lol_analysis_tool\data\files\queues_active.json'
        with open(new_path, 'w') as f:
            q = json.dumps(queues, indent=4, separators=(',', ': '), sort_keys=False)
            f.write(q)

    def get_timeline_file(self, match_id):
        r = requests.get(url=self.url2 + f'/lol/match/v5/matches/{match_id}/timeline',
                         headers={'X-Riot-Token': self.key})
        data = json.dumps(r.json(), indent=4, separators=(',', ': '), sort_keys=True)
        file_path = os.path.join(
            r'S:\ProgProjects\PythonProjects\lol_analysis_tool\lol_analysis_tool\data\files\timelines',
            f'{match_id}.json')
        with open(file_path, 'w') as f:
            f.write(data)