import itertools
import random

iter_bin = itertools.cycle([0, 1])
iter_compass = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
iter_days = itertools.cycle([day for day in range(7)])
iter_months = itertools.cycle([month for month in range(1, 13)])

# bonus iterators
iter_hours = itertools.cycle([hour for hour in range(24)])
iter_minutes = itertools.cycle([minute for minute in range(60)])
iter_seconds = itertools.cycle([second for second in range(60)])

for _ in range(15):
    print(f"{next(iter_bin)} | {next(iter_compass)} | {next(iter_days)}")
