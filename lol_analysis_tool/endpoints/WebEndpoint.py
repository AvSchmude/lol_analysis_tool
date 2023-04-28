import traceback
import requests
import json
from lol_analysis_tool.config import riot_api


class WebEndpoint:
    def __init__(self):
        self.key = riot_api
        self.url = r'https://euw1.api.riotgames.com'
        self.url2 = r'https://europe.api.riotgames.com'
        self.queueId = {400: 'Draft Pick',
                        420: 'Ranked Solo',
                        440: 'Ranked Flex',
                        450: 'Aram'}

    def request_summoner_by_name(self, name):
        """Request the summoner data by summoner name.

        :param name: str Summoner name
        :return: Response containing summoner information
        """
        query = requests.get(url=self.url + f'/lol/summoner/v4/summoners/by-name/{name}',
                             headers={'X-Riot-Token': self.key})
        return query

    def request_match_ids(self, puuid, queueid, type='ranked', count=100):
        """Requests match ids using summoner puuid.

        :param int puuid: summoner ID
        :param int queueid: game type ID
        :param str type: game type description
        :param int count: number of match IDs
        """
        match_ids = requests.get(url=self.url2 + f'/lol/match/v5/matches/by-puuid/{puuid}/ids',
                                 params={'queue': queueid, 'type': type, 'count': count},
                                 headers={'X-Riot-Token': self.key})
        return match_ids

    def request_matches_from_id_list(self, id_list):
        """Requests for each ID the game data and saves it as a json file.

        :param list id_list: List containing match IDs
        """
        for match_id in id_list:
            r = requests.get(url=self.url2 + f'/lol/match/v5/matches/{match_id}', headers={'X-Riot-Token': self.key})
            data = json.dumps(r.json(), indent=4, separators=(',', ': '), sort_keys=True)
            file_path = os.path.join(r'.\ranked_solo', f'{match_id}.json')
            with open(file_path, 'w') as f:
                f.write(data)

    @staticmethod
    def request_matches_from_file(self, file_name):
        """Calls request_matches_from_id_list with id read from file"""
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.request_matches_from_id_list(lines)

    @staticmethod
    def write_summoner_data_to_json(name, summoner):
        data = json.dumps(summoner.json(), indent=4, separators=(',', ': '), sort_keys=True)
        with open(f'{name}.json', 'w') as file:
            file.write(data)

    @staticmethod
    def write_match_ids_to_txt(name, id_list):
        with open(f'endpoint\\{name}_match_ids.txt', 'w') as file:
            for index, i in enumerate(id_list):
                if index < len(id_list) - 1:
                    file.write(i)
                    file.write('\n')
                else:
                    file.write(i)
