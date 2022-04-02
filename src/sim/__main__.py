import sim_runner

from multiprocessing import Process

all_runners = []

for _ in range(10):
    r = sim_runner.LotteryRunner()
    p = Process(target = r.start)
    all_runners.append(p)


for r in all_runners:
    r.start()
