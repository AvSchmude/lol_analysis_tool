import os
import json
import pandas as pd
from endpoints.WebEndpoint import WebEndpoint
from endpoints.DatabaseEndpoint import DatabaseEndpoint, TABLES
from lol_analysis_tool.data.GameData import GameData


def convert_to_pretty_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        d = json.load(json_file)
    # d = dict(data)
    pretty_json = json.dumps(d, indent=4, sort_keys=False)
    with open(file_path, 'w') as file:
        file.write(pretty_json)


def main():
    ep = WebEndpoint()
    # dbe = DatabaseEndpoint()

    gd = GameData(os.getcwd() + "\\data\\files\\ranked_solo\\EUW1_5988809047.json")
    # gd.player_list[7].__repr__()
    # gd.player_list[0].to_dict()
    # gd.player_list[0].to_list()
    gd.player_list[0].prep_for_database()


if __name__ == '__main__':
    # main()
    path = os.getcwd()
    print(path)
    d = r'\data\files\queues.json'
    p = path + d
    with open(p, 'r') as file:
        data = file.readlines()
