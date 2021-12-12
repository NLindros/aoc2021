from itertools import chain
import os
from math import prod, inf
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


def is_smallest_in_neighborhood(matrix):
    height, width = len(matrix), len(matrix[0])
    stream = list(chain(*matrix))
    horizontal = min_point_in_stream(stream, width=width, height=height)
    transpose_data = list(chain(*zip(*matrix)))
    vertical = min_point_in_stream(transpose_data, width=height, height=width)
    return [h & v for v, h in zip(horizontal, vertical)]


def min_point_in_stream(stream, width, height):
    left = [True, *[a < b for a, b in zip(stream[1:], stream[:-1])]]
    left[slice(None, None, width)] = [True] * height
    right = [*[a > b for a, b in zip(stream[1:], stream[:-1])], True]
    right[slice(width - 1, None, width)] = [True] * height
    return [l & r for l, r in zip(left, right)]


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
    groups = [get_group_around_point(data, point) for point in min_points]
    group_size = sorted(map(len, groups))
    return prod(group_size[-3:])


def get_group_around_point(data, start):
    height, width = len(data), len(data[0])
    start_idx = width * start[0] + start[1]
    group = [start_idx]
    stream = list(chain(*data))
    last_row = width * (height - 1)
    for idx in group:
        for new_idx in get_adjacent_points(width, last_row, idx):
            if new_idx not in group:
                if stream[new_idx] < MAX:
                    group.append(new_idx)
    return group


def get_adjacent_points(width, last_row, idx):
    adjacent = filter(
        None,
        [
            idx - 1 if idx % width else None,
            idx + 1 if (idx + 1) % width else None,
            idx - width if idx >= width else None,
            idx + width if idx < last_row else None,
        ],
    )

    return adjacent


def basin_points(data: List[list]) -> List[tuple]:
    return [
        (i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val < MAX
    ]


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solve_part1, "part2": get_basins}
    print(solver[part](read_input()))
