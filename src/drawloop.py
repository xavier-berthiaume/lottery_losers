from tkinter import *
import random
import secrets
import main_window
import time
from threading import Thread


class DrawEngine():

    def __init__(self, window):
        self.winnings = 0
        self.total_cost = 0
        self.matches = [0, 0, 0, 0, 0, 0]
        self.drawing = False
        self.window = window
        self.generateWinningCombination()
        self.draw_thread = Thread(target = self.startDrawing)


    def startDrawing(self):
        self.drawing = True
        while self.drawing:
            self.drawn_values = []
            self.buyTicket()
            for x in range(0,6):
                self.drawn_values.append(random.randint(0, 49))
                self.window.draw_entries[x].delete(0, END)
                self.window.draw_entries[x].insert(0, str(self.drawn_values[-1]))
            self.checkMatches()
            #time.sleep(1)


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
                print(self.matches)


    def generateWinningCombination(self):
        combination = []
        for x in range(0,6):
            combination.append(secrets.randbelow(50))
        else:
            self.winningCombination = tuple(combination)

    def buyTicket(self):
        self.total_cost += 3
        self.window.updateCostLabel(self.total_cost)


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
