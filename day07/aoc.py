from itertools import count
from pathlib import Path
import os


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [int(val) for val in fid.readline().split(",")]


def find_median(data):
    n = len(data)
    mid_idx = n // 2
    if n % 2:
        return sorted(data)[mid_idx]
    return sum(sorted(data)[mid_idx - 1 : mid_idx + 1]) / 2


def cost_part1(data, target):
    return sum([abs(x - target) for x in data])


def cost_part2(data, target):
    return sum([sum(range(abs(x - target) + 1)) for x in data])


def find_min_cost(data, cost_func):
    init_guess = int(sum(data) / len(data))
    current_cost = cost_func(data, init_guess)

    result = run_to_min(data, cost_func, current_cost, count(init_guess, step=1))
    if result < current_cost:
        return result

    result = run_to_min(data, cost_func, current_cost, count(init_guess, step=-1))
    if result < current_cost:
        return result

    return current_cost


def run_to_min(data, cost_func, current_cost, guess):
    next(guess)
    while True:
        next_cost = cost_func(data, next(guess))
        if current_cost < next_cost:
            return current_cost
        current_cost = next_cost


def part1(data):
    return cost_part1(data, find_median(data))


def part2(data):
    return find_min_cost(data, cost_part2)


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1, "part2": part2}
    print(solver[part](read_input()))
