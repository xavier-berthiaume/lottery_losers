import sqlite3
from os import *

class Db():

    def __init__(self):
        #If the db file already exists, assume the table was already created, if it doesn't exist, then create the table
        if os.path.isfile('./lottery_run_stats.db'):
            db_exists = True
        else:
            db_exists = False

        self.__connection = sqlite3.Connection('lottery_run_stats.db')
        self.__cursor = self.__connection.cursor()

        #unfortunate double negation here, code is only executed if the db doesn't exist
        if not db_exists:
            self.createTable()


    def createTable(self):
        self.__cursor.execute('INSERT INTO stats VALUES (:name, :info, :stats, )')
