import drawloop
import main_window
import run

import random, secrets
import time
import sys

from threading import Thread

sys.path.append('../src')

from etc import db_handler, log

#main class that will centralize all the elements of the app and allow them to easily pass information from one module to the other
class LotteryRunner():
    num_runners = 0

    def __init__(self):
        LotteryRunner.num_runners += 1
        self.name = LotteryRunner.generateName()
        self.save_to_db = False


    def start(self):
        self.initializeEngines()
        self.log.logInfoMessage('set up without issue')

        self.initializeDB()
        self.log.logInfoMessage('connection to database successful')
        self.root_window.initializeFrames()


    def initializeEngines(self):
        self.root_window = main_window.Root(self)
        self.draw_engine = drawloop.DrawEngine(self)
        self.log = log.LogEngine(self)


    def initializeDB(self):
        self.db_thread = Thread(target = self.dbFunction)
        self.db_thread.start()


    def dbFunction(self):
        self.db = db_handler.Db(self)
        self.db.createControllers()

        while True:
            time.sleep(1)
            if self.save_to_db:
                run_to_save = run.Run(self)
                self.db.storeRun(run_to_save)
                self.save_to_db = False


    def saveRun(self):
        self.save_to_db = True


    @staticmethod
    def generateName():
        str_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rand_str = random.choices(str_list, k = 8)
        rand_int = random.randint(0,99)
        str_name = ''
        str_name = str_name.join([str(elem) for elem in rand_str])
        name = str(rand_int) + str(str_name) + str(LotteryRunner.num_runners)
        return name
