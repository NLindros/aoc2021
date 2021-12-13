import os
from dataclasses import dataclass


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [[int(x) for x in row.strip()] for row in fid]


@dataclass
class Size:
    height: int
    width: int


def dumbo_simulate(data, steps=100):

    flashes = 0
    size = Size(len(data), len(data[0]))

    for step in range(steps):
        data, flashed = step_simulation(data, size)
        flashes += len(flashed)

    return data, flashes


def run_to_flash(data):
    size = Size(len(data), len(data[0]))

    step = 0
    while True:
        step += 1
        data, flashed = step_simulation(data, size)

        if len(flashed) == size.height * size.width:
            return step


def step_simulation(data, size: Size):
    data = [[x + 1 for x in line] for line in data]
    flashed = []
    while True:
        all_affected = []
        for i, line in enumerate(data):
            for j, x in enumerate(line):
                if x > 9 and (i, j) not in flashed:
                    flashed.append((i, j))
                    adjacent = get_adjacent_points(i, j, size)
                    all_affected.extend(adjacent)

        if len(all_affected) == 0:
            break

        for i, j in all_affected:
            data[i][j] += 1

    for i, j in flashed:
        data[i][j] = 0

    return data, flashed


def get_adjacent_points(row_idx, col_idx, size: Size):
    adjacent = []
    if row_idx > 0:
        adjacent.append((row_idx - 1, col_idx))
    if row_idx < size.width - 1:
        adjacent.append((row_idx + 1, col_idx))
    mid_line = [(row_idx, col_idx), *adjacent]
    if col_idx > 0:
        adjacent = [*adjacent, *[(i, j - 1) for i, j in mid_line]]
    if col_idx < size.height - 1:
        adjacent = [*adjacent, *[(i, j + 1) for i, j in mid_line]]
    return adjacent


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": dumbo_simulate, "part2": run_to_flash}
    print(solver[part](read_input()))
