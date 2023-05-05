import json
import pandas as pd
from endpoints.mongodb_endpoint import MongoDBEndpoint
from endpoints.riot_endpoint import RiotEndpoint, os, requests
from endpoints.mysql_endpoint import MySQLEndpoint, TABLES
from lol_analysis_tool.data.gamedata import GameData


def convert_to_pretty_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        d = json.load(json_file)
    # d = dict(data)
    pretty_json = json.dumps(d, indent=4, sort_keys=False)
    with open(file_path, 'w') as file:
        file.write(pretty_json)


def main():
    ep = RiotEndpoint()
    # dbe = DatabaseEndpoint()

    gd = GameData(os.getcwd() + "\\data\\files\\ranked_solo\\EUW1_5988809047.json")
    # gd.player_list[7].__repr__()
    # gd.player_list[0].to_dict()
    # gd.player_list[0].to_list()
    gd.player_list[0].prep_for_database()


if __name__ == '__main__':
    me = MongoDBEndpoint()
    re = RiotEndpoint()
    matches, timelines = re.request_matches('Skounge', 420)
    # print(os.path.dirname(r'.\data\files\timelines\.'))