import os
from collections import deque, Counter


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return map(int, fid.readline().split(","))


def run_life_simulation(ages, days):
    amount = Counter(ages)
    population_map = deque(amount[idx] for idx in range(9))
    for day in range(days):
        population_map.rotate(-1)
        population_map[6] += population_map[8]
    return sum(population_map)


if __name__ == "__main__":
    part = os.environ.get("part")
    days = {"part1": 80, "part2": 256}
    print(run_life_simulation(read_input(), days[part]))
