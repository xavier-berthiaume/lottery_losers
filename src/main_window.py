from tkinter import *
import drawloop

class Root():
    def __init__(self):
        #initialize some default values that you use to build the frame
        self.generic_pad_x = 2
        self.generic_pad_y = 3
        self.draw_engine = drawloop.DrawEngine(self)
        #design the root window
        self.window = Tk()
        self.window.title("Lottery Losers")
        #self.window.geometry("200x200")
        self.createWinningFrame()
        self.createDrawFrame()
        self.createInfoFrame()
        self.window.mainloop()


    #create a frame that displays the winning combination of numbers right from the start
    def createWinningFrame(self):
        winning_frame = LabelFrame(self.window, text = "Winning Combination")
        winning_frame.grid(row = 0, column = 0, columnspan = 2, padx = self.generic_pad_x, pady = self.generic_pad_y, ipady = 5,  sticky = E+W)

        combination_label = Label(winning_frame, text = f"The winning combination: {self.draw_engine.winningCombination}")
        combination_label.grid(row = 0, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y)


    #create the frame that contains information related to the lottery numbers that are being currently drawn
    #later on it will be necessary to access the entry fields to update the number values. The Root object's draw_entries list will contain all entry fields.
    def createDrawFrame(self):
        button_height_generic = 3

        draw_frame = LabelFrame(self.window, text = "Lottery Draw Information")
        draw_frame.grid(row = 1, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = N+S)
        count = 1
        for x in range(0,12,2):
            draw_label = Label(draw_frame, text = f"Number {count}: ")
            draw_label.grid(row = x, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y)
            count += 1

        self.draw_entries = []
        for x in range(1, 13, 2):
            self.draw_entries.append(Entry(draw_frame, width = 5, justify = CENTER))
            self.draw_entries[-1].grid(row = x-1, column = 1, padx = self.generic_pad_x, pady = self.generic_pad_y)

        draw_button = Button(draw_frame, text = "Start Drawing", command = self.draw_engine.draw_thread.start, height = button_height_generic)
        draw_button.grid(row = 100, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)

        stop_drawing_button = Button(draw_frame, text = 'Stop Drawing', command = lambda: self.draw_engine.stopDrawing(), height = button_height_generic)
        stop_drawing_button.grid(row = 100, column = 1, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)


    #create a frame tha contains all the information that relates to lottery wins and losses (1 match all the way to 6 match)
    #accessing these labels can be done through the match_labels list of the root object
    #accessing the label that displays the 'cost' of the lottery tickets is cost_label of the root object, winnings is the winnings_label
    def createInfoFrame(self):
        info_frame = LabelFrame(self.window, text = "Wins and Losses")
        info_frame.grid(row = 1, column = 1, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W+N+S)

        self.match_labels = []
        for x in range(0, 6):
            self.match_labels.append(Label(info_frame, text = f"{x+1} match: 0"))
            self.match_labels[-1].grid(row = x, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = W)

        self.draws_label = Label(info_frame, text = "Total draws: 0")
        self.draws_label.grid(row = 7, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)

        self.cost_label = Label(info_frame, text = "Total ticket cost: $0")
        self.cost_label.grid(row = 8, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)

        self.winnings_label = Label(info_frame, text = "Winnings: $0")
        self.winnings_label.grid(row = 9, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)


    def updateWinningsLabel(self, total_winnings):
        self.winnings_label.config(text = f"Winnings: ${total_winnings}")
        #self.winnings_label.grid(row = 8, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)


    def updateCostLabel(self, total_cost):
        self.cost_label.config(text = f"Total ticket cost: ${total_cost}")
        #self.cost_label.grid(row = 8, column = 0, padx = self.generic_pad_x, pady = self.generic_pad_y, sticky = E+W)


    def updateDrawLabel(self, total_draws):
        self.draws_label.config(text = f"Total draws: {total_draws}")
