#import numpy as np
import logging
from drawloop import *

class StatEngine():

    def __init__(self, engine):
        self.draw_engine = engine
        self.setupLogging()
        self.logger.info('Stat engine initialized.')


    def setupLogging(self):
        #create logger
        self.logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler('../log/stats.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        self.logger.info('Logging has been set up.')


    def averageCost(self):
        pass
