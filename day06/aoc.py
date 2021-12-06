import os
from collections import deque, Counter

with open("input.txt", "r") as fid:
    ages = map(int, fid.readline().split(","))

days = {"part1": 80, "part2": 256}[os.environ.get("part")]

amount = Counter(ages)
population_map = deque(amount[idx] for idx in range(9))

for day in range(days):
    population_map.rotate(-1)
    population_map[6] += population_map[8]

print(sum(population_map))
