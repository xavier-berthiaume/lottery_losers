import random
import main_window
import time

class DrawEngine():

    def __init__(self, window):
        self.drawn_values = []
        self.winnings = 0
        self.total_cost = 0
        self.matches = [0, 0, 0, 0, 0, 0]
        self.drawing = False
        self.window = window


    def startDrawing(self):
        self.drawing = True
        while self.drawing:
            for x in range(0,6):
                self.drawn_values.append(random.randint(0, 49))
                self.window.draw_entries[x].text = str(self.drawn_values[-1])
                time.sleep(.1)
