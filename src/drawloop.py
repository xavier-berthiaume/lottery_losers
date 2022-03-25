from tkinter import *
import random
import secrets
import main_window
from threading import Thread
from stats import *
import time


class DrawEngine():

    def __init__(self, runner):
        self.runner = runner
        self.winnings = 0
        self.total_cost = 0
        self.matches = [0, 0, 0, 0, 0, 0, 0, 0]
        self.draws = 0
        self.drawing = False
        #self.stat_engine = StatEngine(self)
        self.__first_draw = True
        self.window = runner.root_window
        self.generateWinningCombination()
        self.draw_thread = Thread(target = self.conductDraw)


    def startDrawing(self):
        if self.__first_draw:
            self.__first_draw = False
            self.draw_thread.start()
        self.drawing = True


    def conductDraw(self):
        while True:
            time.sleep(.001)
            if self.drawing:
                self.drawn_values = []
                self.buyTicket()
                combination = [x for x in range(0,50)]
                random.shuffle(combination)
                for x in range(0, 43):
                    combination.pop()

                self.drawn_values = combination
                self.drawn_bonus = combination[6]

                for x in range(0,7):
                    self.window.draw_entries[x].delete(0, END)
                    self.window.draw_entries[x].insert(0, str(self.drawn_values[x]))

                self.checkMatches()
                if (self.draws % 10000) == 0:
                    self.runner.saveRun()


    def stopDrawing(self):
        self.drawing = False


    def checkMatches(self):
        match = 0
        isBonus = False
        if self.bonus == self.drawn_bonus:
            isBonus = True

        for x in range(0,6):
            if self.drawn_values[x] in self.winningCombination:
                match += 1
        else:
            if match == 2 and isBonus:
                self.matches[6] += 1
                self.window.match_labels[6].config(text = f"2 match /w Bonus: {self.matches[6]}")
                self.updateWinning(match, isBonus)
            elif match == 5 and isBonus:
                self.matches[7] += 1
                self.window.match_labels[7].config(text = f"5 match /w Bonus: {self.matches[7]}")
                self.updateWinning(match, isBonus)
            elif match > 0:
                #the amount of matches have been calculated, now update the array indicating the number of matches and then update the gui
                self.matches[match-1] += 1
                self.window.match_labels[match-1].config(text = f"{match} match: {self.matches[match-1]}")

            self.updateWinning(match, isBonus)


    def generateWinningCombination(self):
        #brute force way of generating a list with random numbers in it that are non repeating.
        combination = [x for x in range(0,50)]
        random.shuffle(combination)
        for x in range(0, 43):
            combination.pop()

        self.winningCombination = tuple(combination[0:6])
        self.bonus = combination[6]

        '''
        incorrect way of generating the winning combination. In 6/49 the numbers cannot repeat themselves.

        for x in range(0,6):
            combination.append(secrets.randbelow(50))
        else:
            self.winningCombination = tuple(combination)
        '''


    def buyTicket(self):
        self.total_cost += 3
        self.window.updateCostLabel(self.total_cost)
        self.draws += 1
        self.window.updateDrawLabel(self.draws)


    def updateWinning(self, match, isBonus):
        if not match == 0:
            if isBonus:
                win_dict = {
                    1: 0,
                    2: 5,
                    3: 10,
                    4: 78,
                    5: 110841,
                    6: 8811827
                    }
            else:
                #The value that will be passed will be from 1 to 6, symbolizing a 1 to 6 matching values.
                #Wins have the following payout without bonus:
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
