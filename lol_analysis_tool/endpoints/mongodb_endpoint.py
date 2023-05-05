import pymongo as pm
from lol_analysis_tool.config import mongodb_config


class MongoDBEndpoint:
    def __init__(self):
        self.client = None
        self.db_name = 'match_history'
        self.setup()

    def setup(self):
        try:
            self.client = pm.MongoClient(mongodb_config)

        except Error as err:
            print(err)

