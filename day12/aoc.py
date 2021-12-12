from itertools import permutations
import os
from math import prod, inf
from typing import List
from collections import defaultdict, Counter


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return build([line.strip() for line in fid.readlines()])


def build(raw_str):
    connections = defaultdict(set)
    for line in raw_str:
        for (start, end) in permutations(line.split("-")):
            if end != "start" and start != "end":
                connections[start].add(end)
    return connections


def find_paths_part_1(cave):
    def rec_find_path(current_path):
        for node in cave[current_path[-1]]:
            if node == "end":
                paths.append([*current_path, node])
            elif node.isupper() or node not in current_path:
                rec_find_path([*current_path, node])

    paths = []
    for node in cave["start"]:
        rec_find_path(["start", node])

    return paths


def find_paths_part_2(cave):
    def rec_find_path(current_path):
        for node in cave[current_path[-1]]:
            if node == "end":
                paths.append([*current_path, node])
                continue
            if node.isupper():
                rec_find_path([*current_path, node])
                continue
            lowers = [node for node in current_path if node.islower()]
            if node not in lowers or len(lowers) == len(set(lowers)):
                rec_find_path([*current_path, node])

    paths = []
    for node in cave["start"]:
        rec_find_path(["start", node])

    return paths


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": find_paths_part_1, "part2": find_paths_part_2}
    print(solver[part](read_input()))
