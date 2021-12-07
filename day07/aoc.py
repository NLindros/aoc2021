from itertools import count
from pathlib import Path
from statistics import median
import os


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [int(val) for val in fid.readline().split(",")]


def cost_part2(data, pos):
    return sum([sum(range(abs(x - pos) + 1)) for x in data])


def find_min_cost(data):
    init_guess = int(sum(data) / len(data))
    current_cost = cost_part2(data, init_guess)

    for step in [-1, 1]:
        result = run_to_min(data, current_cost, count(init_guess, step=step))
        if result < current_cost:
            return result

    return current_cost


def run_to_min(data, current_cost, guess):
    next(guess)
    while True:
        next_cost = cost_part2(data, next(guess))
        if current_cost < next_cost:
            return current_cost
        current_cost = next_cost


def part1(data):
    pos = median(data)
    return sum([abs(x - pos) for x in data])


def part2(data):
    return find_min_cost(data)


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1, "part2": part2}
    print(solver[part](read_input()))
