#import numpy as np
import logging
from drawloop import *

class StatEngine():

    def __init__(self, engine):
        self.draw_engine = engine
        self.setupLogging()
        self.log.info('======= --- ======= --- ======= --- ======= Stat Engine Initialized ======= --- ======= --- ======= --- =======')


    def setupLogging(self):
        #create logger
        logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt = "%d/%m/%Y %H:%M:%S")
        logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler('../log/stats.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        #logging.debug('Does this shit work?')
        self.log = logger


    def createLogDump(self):
        self.log.info('======= --- ======= Start of Data Dump ======= --- =======')
        self.logRunInfo()
        self.logStats()
        self.log.info('======= --- ======= End of Data Dump ======= --- =======')


    def logStats(self):
        stat_list = [self.averageCost(), self.averageRevenue(), self.percentWinningTickets()]
        self.log.info('----- Run Statistics -----')
        message = ""
        for x in stat_list:
            message += "\n" + x

        self.log.info(message)


    def logRunInfo(self):
        engine = self.draw_engine
        run_info = [engine.draws, engine.total_cost, engine.winnings]
        self.log.info('----- Run information -----')
        self.log.info(f'''
            Total number of draws: {engine.draws}
            Total cost: {engine.total_cost}
            Total winnings: {engine.winnings} ''')

    #calculate the average cost of a lottery ticket considering the value gained from winnings
    def averageCost(self):
        engine = self.draw_engine
        av_cost = (engine.total_cost - engine.winnings)/engine.draws
        return f"\t\t\tRun average cost per ticket: {av_cost}"


    #calculate the average revenue that a single ticket generates
    def averageRevenue(self):
        engine = self.draw_engine
        av_rev = engine.winnings/engine.draws
        return f"\t\t\tRun average revenue per ticket: {av_rev}"


    #calculate the % chance of just winning, regardless of the amount of matches. Doesn't count 1 match since it doesn't win any money.
    def percentWinningTickets(self):
        engine = self.draw_engine
        per_winning = ((sum(engine.matches)-engine.matches[0])/engine.draws)*100
        return f"\t\t\tRun percentages of winning per ticket (any match that won money): {per_winning}%"
