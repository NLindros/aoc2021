from collections import Counter
import os
from pathlib import Path
from statistics import mode


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return [val.strip() for val in fid]


def most_common_in_rows(data):
    return "".join(mode(row) for row in zip(*data))


def invert_binary(bin_str):
    return "".join("1" if val == "0" else "0" for val in bin_str)


def bin2dec(bin_str):
    return int(bin_str, 2)


def power_consumption(data):
    most_common_bin_str = most_common_in_rows(data)
    gamma = bin2dec(most_common_bin_str)
    epsilon = bin2dec(invert_binary(most_common_bin_str))
    return gamma * epsilon


def life_support_decode(data, to_keep):
    n = len(data[0])
    for i in range(n):
        count = Counter(x[i] for x in data)
        keeper = to_keep(count)
        data = [row for row in data if row[i] == keeper]
        if len(data) == 1:
            break
    return data[0]


def life_support_rating(data):
    oxygen = life_support_decode(data, to_keep=lambda count: "1" if count["1"] >= count["0"] else "0")
    co2 = life_support_decode(data, to_keep=lambda count: "1" if count["1"] < count["0"] else "0")
    return bin2dec(oxygen) * bin2dec(co2)


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": power_consumption, "part2": life_support_rating}
    print(solver[part](read_input()))
