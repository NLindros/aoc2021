import os
from itertools import chain
from math import prod, inf
from typing import List


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [[int(x) for x in row.strip()] for row in fid]


def solve_part1(data):

    flashes = 0
    height, width = len(data), len(data[0])

    data = [x + 1 for x in line for line in data]

    for i, line in enumerate(data):
        for j, x in enumerate(line):
            if x > 9:
                flashes += 1


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solve_part1, "part2": get_basins}
    print(solver[part](read_input()))
