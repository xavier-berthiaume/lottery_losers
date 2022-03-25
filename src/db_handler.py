import sqlite3
import os

class Db():

    def __init__(self, runner):
        self.runner = runner


    def createControllers(self):
        #If the db file already exists, assume the table was already created, if it doesn't exist, then create the table
        if os.path.isfile('./lottery_run_stats.db'):
            db_exists = True
            self.runner.log.logInfoMessage('the DB file already exists, not creating a new table.')
        else:
            db_exists = False
            self.runner.log.logInfoMessage("the DB file doesn't already exist, creating a new table.")

        self.connection = sqlite3.Connection('lottery_run_stats.db')
        self.cursor = self.connection.cursor()

        #unfortunate double negation here, code is only executed if the db doesn't exist
        if not db_exists:
            self.createTable()


    def createTable(self):
        try:
            self.cursor.execute("""CREATE TABLE runs (
                name text,
                draws integer,
                matches_one integer,
                matches_two integer,
                matches_three integer,
                matches_four integer,
                matches_five integer,
                matches_six integer,
                matches_two_bonus integer,
                matches_five_bonus integer,
                total_cost integer,
                total_winnings integer,
                winning_combination text,
                winning_bonus integer
                )""")
            self.runner.log.logInfoMessage('Table successfully created')
        except sqlite3.OperationalError as e:
            self.runner.log.logWarningMessage('error when creating the table, error: ' + str(e))


    def storeRun(self, run):
        try:
            self.cursor.execute("INSERT INTO runs VALUES(:name, :draws, :matches_one, :matches_two, :matches_three, :matches_four, :matches_five, :matches_six, :matches_two_bonus, :matches_five_bonus, :total_cost, :total_winnings, :winning_combination, :winning_bonus)",
                {
                    'name': run.name,
                    'draws': run.draws,
                    'matches_one': run.matches[0],
                    'matches_two': run.matches[1] ,
                    'matches_three': run.matches[2],
                    'matches_four': run.matches[3],
                    'matches_five': run.matches[4],
                    'matches_six': run.matches[5],
                    'matches_two_bonus': run.matches[6],
                    'matches_five_bonus': run.matches[7],
                    'total_cost': run.total_cost,
                    'total_winnings': run.winnings,
                    'winning_combination': run.winningCombinationToString(),
                    'winning_bonus': run.winning_bonus
                })

            self.connection.commit()
            self.runner.log.logInfoMessage('successfully wrote run data to the database')
        except sqlite3.Error as e:
            self.runner.log.logWarningMessage('error when writing to the database file, error: ' + str(e))
