import os
from pathlib import Path
from itertools import pairwise, islice
from collections import deque

def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [int(val) for val in fid]

def depth_increases(depths):
    return sum((b > a) for a, b in pairwise(depths))

def sliding_window(iterable, win_size):
    it = iter(iterable)
    window = deque(islice(it, win_size), maxlen=win_size)
    if len(window) == win_size:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def sliding_mean_increases(dephts):
    sums = (sum(win) for win in sliding_window(dephts, win_size=3))
    return depth_increases(sums)


if __name__ == "__main__":

    part = os.environ.get("part")
    solver = {
        "part1": depth_increases,
        "part2": sliding_mean_increases,
    }

    file_input = read_input("input.txt")
    result = solver[part](file_input)

    print(result)
