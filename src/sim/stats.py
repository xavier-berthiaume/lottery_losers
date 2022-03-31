#import numpy as np
import logging
from drawloop import *

#Don't want to use logging to keep stats, it's a pretty poor way of doing this. Instead logging will be moved to it's own 'engine' called log
#Data will be stored on a DB, with each run of the program having its unique ID, won't be handled by this module however, instead this module will extrapolate information from the retrieved data.

class StatEngine():

    def __init__(self, runner):
        self.runner = runner


    #calculate the average cost of a lottery ticket considering the value gained from winnings
    def averageCost(self):
        engine = self.runner.draw_engine
        av_cost = (engine.total_cost - engine.winnings)/engine.draws
        return av_cost


    #calculate the average revenue that a single ticket generates
    def averageRevenue(self):
        engine = self.runner.draw_engine
        av_rev = engine.winnings/engine.draws
        return av_rev


    #calculate the % chance of just winning, regardless of the amount of matches. Doesn't count 1 match since it doesn't win any money.
    def percentWinningTickets(self):
        engine = self.runner.draw_engine
        per_winning = ((sum(engine.matches)-engine.matches[0])/engine.draws)*100
        return per_winning
