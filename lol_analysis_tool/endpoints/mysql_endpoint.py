import mysql
import mysql.connector
from lol_analysis_tool.endpoints.Tables import TABLES, item_keywords, part_keywords, match_keywords
from mysql.connector import errorcode
from lol_analysis_tool.config import mysql_config


class DatabaseEndpoint:
    def __init__(self):
        self.con = mysql.connector.connect(**mysql_config)
        self.cursor = self.con.cursor()
        self.setup_database()

    def setup_database(self):
        self.create_database()
        self.use_database()
        self.create_tables()

    def create_database(self, db_name='match_history'):
        """Executes MySQL query to create database.

        :param str db_name: database name
        """
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
        except mysql.connector.Error as err:
            print("Cannot create database.")
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print("Database already exists.")
            pass

    def use_database(self, db_name='match_history'):
        """Executes MySQL query to use database

        :param str db_name: database name
        """
        try:
            self.cursor.execute("USE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Database {} does not exist.".format(db_name))
            exit(1)

    def table_exists(self):
        """Executes MySQL query to check if the table defined in TABLES exists in the database.

        Returns binary value.

        :param str table_name: name of the table
        :returns: binary value
        """
        try:
            keys = list(TABLES.keys())
            self.cursor.execute("SELECT table_name "
                                "FROM information_schema.tables "
                                "WHERE table_name IN ('{}', '{}', '{}')".format(*keys), multi=True)
            query_results = self.cursor.fetchall()
            flattened_results = [item for sublist in query_results for item in sublist]
            if flattened_results == keys:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def create_tables(self):
        """Executes MySQL queries specified in TABLES to create tables."""
        try:
            if not self.table_exists():
                for table in TABLES.values():
                    self.cursor.execute(table)
        except mysql.connector.Error as err:
            print("Failed creating table: {}".format(err))
            pass

    def drop_database(self, db_name: str):
        """Executes MySQL query to drop the database.

        :param str db_name: name of the database"""
        try:
            self.cursor.execute("DROP DATABASE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Failed dropping table: {}".format(err))

    def insert_data(self, table_name, data):
        """Executes MySQL query to insert data into a table.

        :param str table_name: name of the table
        :param object data: object including stored data
        """
        match table_name:
            case 'items':
                self.cursor.execute(f"INSERT INTO {table_name} "
                                    f"{*item_keywords,} "
                                    f"VALUES{*data,}")
            case 'participants':
                self.cursor.execute(f"INSERT INTO {table_name} "
                                    f"{*part_keywords,} "
                                    f"VALUES{*data,}")
            case 'matches':
                self.cursor.execute(f"INSERT INTO {table_name} "
                                    f"{*match_keywords,} "
                                    f"VALUES{*data,}")
            case _:
                print("Table does not exist!")
