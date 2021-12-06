from pathlib import Path
import os


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return list(map(int, fid.readline().split(",")))


def run_life_simulation(ages, days):
    population_map = [0] * 9
    for age in ages:
        population_map[age] += 1
    for day in range(days):
        spawns = population_map[0]
        population_map = [*population_map[1:], spawns]
        population_map[6] += spawns
    return sum(population_map)


if __name__ == "__main__":
    part = os.environ.get("part")
    days = {"part1": 80, "part2": 256}
    print(run_life_simulation(read_input(), days[part]))
