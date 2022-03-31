class Run():

    def __init__(self, runner):
        self.setRunValues(runner)


    def setRunValues(self, runner):
        self.name = runner.name
        self.draws = runner.draw_engine.draws
        self.matches = runner.draw_engine.matches.copy()
        self.total_cost = runner.draw_engine.total_cost
        self.winnings = runner.draw_engine.winnings
        self.winning_combination = runner.draw_engine.winningCombination
        self.winning_bonus = runner.draw_engine.bonus


    def winningCombinationToString(self):
        return str(self.winning_combination)
