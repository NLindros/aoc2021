import os
from collections import deque

# from functools import reduce


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [x.strip() for x in fid]


corrupt_scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

incomplete_scoring = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

char_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def find_incorrect_closing(line):
    expected_closing = deque()
    for char in line:
        if char in char_pairs:
            expected_closing.append(char_pairs[char])
            continue
        if expected_closing.pop() != char:
            return char


def find_incomplete_closing(line):
    expected_closing = deque()
    for char in line:
        if char in char_pairs:
            expected_closing.append(char_pairs[char])
            continue
        if expected_closing.pop() != char:
            return None
    return reversed(expected_closing)


def solution_part_1(data):
    bad_closing = filter(None, [find_incorrect_closing(line) for line in data])
    return sum([corrupt_scoring[char] for char in bad_closing])


def solution_part_2(data):
    incomplete = filter(None, [find_incomplete_closing(line) for line in data])
    all_score = [line_score(line) for line in incomplete]
    mid_idx = len(all_score) // 2
    return sorted(all_score)[mid_idx]


def line_score(line):
    # return reduce(
    #     lambda result, char_val: result * 5 + char_val,
    #     [incomplete_scoring[char] for char in line],
    # )
    result = 0
    for char in line:
        result = result * 5 + incomplete_scoring[char]
    return result


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solution_part_1, "part2": solution_part_2}
    print(solver[part](read_input()))
