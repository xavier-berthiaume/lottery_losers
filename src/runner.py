import drawloop
import log
import main_window
import stats
import random, secrets


#main class that will centralize all the elements of the app and allow them to easily pass information from one module to the other
class LotteryRunner():
    num_runners = 0

    def __init__(self):
        LotteryRunner.num_runners += 1
        self.name = LotteryRunner.generateName()


    def start(self):
        self.initializeEngines()
        self.log.logInfoMessage('set up without issue')


    def initializeEngines(self):
        self.root_window = main_window.Root(self)
        self.draw_engine = drawloop.DrawEngine(self)
        self.stats_engine = stats.StatEngine(self)
        self.log = log.LogEngine(self)

        self.root_window.initializeFrames()


    @staticmethod
    def generateName():
        str_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rand_str = random.choices(str_list, k = 8)
        rand_int = random.randint(0,99)
        str_name = ''
        str_name = str_name.join([str(elem) for elem in rand_str])
        name = str(rand_int) + str(str_name) + str(LotteryRunner.num_runners)
        return name
