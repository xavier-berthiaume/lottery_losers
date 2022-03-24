#import numpy as np
import logging
from drawloop import *

#Don't want to use logging to keep stats, it's a pretty poor way of doing this. Instead logging will be moved to it's own 'engine' called log
#Data will be stored on a DB, with each run of the program having its unique ID, won't be handled by this module however, instead this module will extrapolate information from the retrieved data.

class StatEngine():


    def __init__(self, runner):
        self.runner = runner
        self.draw_engine = runner.draw_engine


    #calculate the average cost of a lottery ticket considering the value gained from winnings
    def averageCost(self):
        engine = self.draw_engine
        av_cost = (engine.total_cost - engine.winnings)/engine.draws
        return f"Run average cost per ticket: {av_cost}"


    #calculate the average revenue that a single ticket generates
    def averageRevenue(self):
        engine = self.draw_engine
        av_rev = engine.winnings/engine.draws
        return f"Run average revenue per ticket: {av_rev}"


    #calculate the % chance of just winning, regardless of the amount of matches. Doesn't count 1 match since it doesn't win any money.
    def percentWinningTickets(self):
        engine = self.draw_engine
        per_winning = ((sum(engine.matches)-engine.matches[0])/engine.draws)*100
        return f"Run percentages of winning per ticket (any match that won money): {per_winning}%"


        #below classes will be used to store a run's information and statistics within, and will be stored to the database.
        #functionality to retrieve this information and feed it to a decoder/numpy project that will extrapolate information from these stats is to come.
class RunInfo():
    pass


class StatInfo():
    pass
