from itertools import chain
import os
from math import prod
from dataclasses import dataclass

MAX_VALUE = 9


@dataclass
class Size:
    height: int
    width: int

    def number_of_samples(self):
        return self.height * self.width

    def transposed_to_flat(self):
        for i in range(self.height):
            for j in range(0, self.number_of_samples(), self.height):
                yield i + j

    def flat_to_transposed(self):
        for i in range(self.width):
            for j in range(0, self.number_of_samples(), self.width):
                yield i + j


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [[int(x) for x in row.strip()] for row in fid]


def solve_part1(data):
    size = Size(len(data), len(data[0]))
    stream = list(chain(*data))
    is_min_point = is_smallest_in_neighborhood(stream, size)
    return sum(val + 1 for val, min_point in zip(stream, is_min_point) if min_point)


def is_smallest_in_neighborhood(stream, size: Size):
    horizontal = min_point_in_stream(stream, width=size.width, height=size.height)
    transpose_data = [stream[i] for i in size.flat_to_transposed()]
    vertical = min_point_in_stream(transpose_data, width=size.height, height=size.width)
    reflipped = (vertical[i] for i in size.transposed_to_flat())
    return [h & v for v, h in zip(horizontal, reflipped)]


def min_point_in_stream(stream, width, height):
    left = [True, *[a < b for a, b in zip(stream[1:], stream[:-1])]]
    left[slice(None, None, width)] = [True] * height
    right = [*[a > b for a, b in zip(stream[1:], stream[:-1])], True]
    right[slice(width - 1, None, width)] = [True] * height
    return [l & r for l, r in zip(left, right)]


def get_basins(data):
    size = Size(len(data), len(data[0]))
    stream = list(chain(*data))
    is_min_points = is_smallest_in_neighborhood(stream, size)
    min_points = (idx for idx, is_min_point in enumerate(is_min_points) if is_min_point)
    groups = (
        get_group_around_point(stream, size, min_point_idx)
        for min_point_idx in min_points
    )
    group_size = sorted(map(len, groups))
    return prod(group_size[-3:])


def get_group_around_point(stream, size, start_idx):
    group = [start_idx]
    last_row = size.width * (size.height - 1)
    for idx in group:
        for new_idx in get_adjacent_points(size.width, last_row, idx):
            if new_idx not in group:
                if stream[new_idx] < MAX_VALUE:
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


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solve_part1, "part2": get_basins}
    print(solver[part](read_input()))
