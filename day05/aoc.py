from itertools import chain
from collections import Counter
from dataclasses import dataclass
import itertools
from typing import Tuple
from pathlib import Path
import os


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [PointPair.parse_str(line) for line in fid]


@dataclass
class PointPair:
    x0: int
    y0: int
    x1: int
    y1: int

    @classmethod
    def parse_str(cls, raw_str):
        point0, point1 = [
            [int(val) for val in point_str.split(",")]
            for point_str in raw_str.split(" -> ")
        ]
        return cls(*point0, *point1)

    def get_line_points(self):
        if self.x0 == self.x1:
            return [(self.x0, y) for y in in_range(self.y0, self.y1)]
        if self.y0 == self.y1:
            return [(x, self.y0) for x in in_range(self.x0, self.x1)]

    def get_diag_points(self):
        if abs(self.x0 - self.x1) == abs(self.y0 - self.y1):
            return [
                (x, y)
                for x, y in zip(
                    in_range(self.x0, self.x1),
                    in_range(self.y0, self.y1),
                )
            ]


def in_range(start, stop):
    step = 1 if start < stop else -1
    for i in range(start, stop, step):
        yield i
    yield stop


def count_multiple_points(*all_points):
    coord_count = Counter(chain(*all_points))
    multi_points = [point for point, amount in coord_count.items() if amount > 1]
    return len(multi_points)


def part1_solution(pairs):
    line_points = chain(filter(None, [pair.get_line_points() for pair in pairs]))
    return count_multiple_points(*line_points)


def part2_solution(pairs):
    line_points = chain(filter(None, [pair.get_line_points() for pair in pairs]))
    diag_points = chain(filter(None, [pair.get_diag_points() for pair in pairs]))
    return count_multiple_points(*line_points, *diag_points)


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1_solution, "part2": part2_solution}
    print(solver[part](read_input()))
