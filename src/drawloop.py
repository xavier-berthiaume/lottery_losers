from tkinter import *
import random
import secrets
import main_window
import time
from threading import Thread
from stats import *


class DrawEngine():

    def __init__(self, handler):
        self.winnings = 0
        self.total_cost = 0
        self.matches = [0, 0, 0, 0, 0, 0]
        self.draws = 0
        self.drawing = False
        self.stat_engine = StatEngine(self)
        if handler.__class__.__name__ == 'Root':
            self.window = handler
            self.generateWinningCombination()
        elif handler.__class__.__name__ == 'StatEngine':
            pass
        self.draw_thread = Thread(target = self.startDrawing)


    def startDrawing(self):
        self.drawing = True
        while True:
            if self.drawing:
                self.drawn_values = []
                self.buyTicket()
                for x in range(0,6):
                    self.drawn_values.append(random.randint(0, 49))
                    self.window.draw_entries[x].delete(0, END)
                    self.window.draw_entries[x].insert(0, str(self.drawn_values[-1]))
                self.checkMatches()
                #time.sleep(1)
            else:
                break


    def stopDrawing(self):
        self.drawing = False
        #time.sleep(.1)
        #self.draw_thread.join()


    def checkMatches(self):
        match = 0
        for x in range(0,6):
            if self.drawn_values[x] == self.winningCombination[x]:
                match += 1
        else:
            if match > 0:
                #the amount of matches have been calculated, now update the array indicating the number of matches and then update the gui
                self.matches[match-1] += 1
                self.window.match_labels[match-1].config(text = f"{match} match: {self.matches[match-1]}")
                self.updateWinning(match)
                #print(self.matches)


    def generateWinningCombination(self):
        combination = []
        for x in range(0,6):
            combination.append(secrets.randbelow(50))
        else:
            self.winningCombination = tuple(combination)


    def buyTicket(self):
        self.total_cost += 3
        self.window.updateCostLabel(self.total_cost)
        self.draws += 1
        self.window.updateDrawLabel(self.draws)


    def updateWinning(self, match):
        #The value that will be passed will be from 1 to 6, symbolizing a 1 to 6 matching values.
        #Wins have the following payout:
        #1 = $0, 2 = $3, 3 = $10, 4 = $78, 5 = $2199, 6 = $8811827
        win_dict = {
            1: 0,
            2: 3,
            3: 10,
            4: 78,
            5: 2199,
            6: 8811827
            }
        self.winnings += win_dict[match]
        self.window.updateWinningsLabel(self.winnings)
