import os
from pathlib import Path
from itertools import pairwise, islice
from collections import deque


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [int(val) for val in fid]


def increases_of_depth(depths):
    return sum((b > a) for a, b in pairwise(depths))


def sliding_window(values, win_size):
    window = deque(islice(values, win_size), maxlen=win_size)
    for x in values:
        yield tuple(window)
        window.append(x)
    yield tuple(window)


def increases_of_depth_with_sliding_mean(dephts):
    win_sums = (sum(win) for win in sliding_window(dephts, win_size=3))
    return increases_of_depth(win_sums)


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {
        "part1": increases_of_depth,
        "part2": increases_of_depth_with_sliding_mean,
    }

    file_input = read_input("input.txt")
    result = solver[part](file_input)
    print(result)
