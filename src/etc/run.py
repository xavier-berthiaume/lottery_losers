class Run():

    all_runs = []

    def __init__(self, name, draws, matches, total_cost, winnings, winning_combination, winning_bonus):
        self.name = name
        self.draws = draws
        self.matches = matches
        self.total_cost = total_cost
        self.winnings = winnings
        self.winning_combination = winning_combination
        self.winning_bonus = winning_bonus


    @staticmethod
    def generateRuns(runs_list):
        for run_point in runs_list:
            all_runs.append(Run(run_point))
