from itertools import chain
import os
from math import inf, prod
from typing import List


MAX = 9


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [[int(x) for x in row.strip()] for row in fid]


def solve_part1(data):
    is_min_point = is_smallest_in_neighborhood(data)
    return sum(
        [
            val + 1
            for line, cond_line in zip(data, is_min_point)
            for val, cond in zip(line, cond_line)
            if cond
        ]
    )


def is_smallest_in_neighborhood(data):
    horizontal = map(left_to_right, data)
    transpose_data = zip(*data)
    vertical = map(left_to_right, transpose_data)
    vertical = zip(*vertical)
    is_min_point = [
        [all(cond) for cond in zip(row, col)] for row, col in zip(horizontal, vertical)
    ]
    return is_min_point


def left_to_right(line):
    left = (True, *[a > b for a, b in zip(line[:-1], line[1:])])
    right = (*[a < b for a, b in zip(line[:-1], line[1:])], True)
    is_min_point = (l & r for l, r in zip(left, right))
    return is_min_point


def get_basins(data):
    is_min_point = is_smallest_in_neighborhood(data)
    min_points = [
        (i, j)
        for (i, row), cond_line in zip(enumerate(data), is_min_point)
        for (j, val), cond in zip(enumerate(row), cond_line)
        if cond
    ]
    coordinates = basin_points(data)
    groups = [get_group(coordinates, point) for point in min_points]
    group_size = sorted(map(len, groups))
    return prod(group_size[-3:])


def get_group(coordinates, start):
    coordinates.remove(start)
    group = [start]
    for a in group:
        for b in coordinates[:]:
            if (a[0] == b[0] and a[1] - b[1] in [-1, 1]) or (
                a[1] == b[1] and a[0] - b[0] in [-1, 1]
            ):
                group.append(b)
                coordinates.remove(b)
    return group


def basin_points(data: List[list]) -> List[tuple]:
    return [
        (i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val < MAX
    ]


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solve_part1, "part2": get_basins}
    print(solver[part](read_input()))
