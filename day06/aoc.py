import os
import collections

with open("input.txt", "r") as fid:
    amount = collections.Counter(map(int, fid.readline().split(",")))

population_map = collections.deque(amount[idx] for idx in range(9))

for day in range({"part1": 80, "part2": 256}[os.environ.get("part")]):
    population_map.rotate(-1)
    population_map[6] += population_map[8]

print(sum(population_map))
