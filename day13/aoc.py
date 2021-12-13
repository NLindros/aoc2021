import os
import re


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        dots = []
        for line in fid:
            if line == "\n":
                break
            dots.append(map(int, line.strip().split(",")))

        instructions = []
        pattern = re.compile("fold along (\w)=(\d+)")
        for line in fid:
            xy, fold = pattern.match(line).groups()
            instructions.append((xy, int(fold)))

    return dots, instructions


def fold_once(dots, direction, fold):
    if direction == "y":
        return set((x, y if y < fold else 2 * fold - y) for x, y in dots)
    if direction == "x":
        return set((x if x < fold else 2 * fold - x, y) for x, y in dots)


def fold_dots(dots, instructions):
    for direction, fold in instructions:
        dots = fold_once(dots, direction, fold)
    return dots


def print_dots(dots):
    width = max(x for x, y in dots) + 1
    height = max(y for x, y in dots) + 1
    for y in range(height):
        print("".join(["#" if (x, y) in dots else " " for x in range(width)]))


if __name__ == "__main__":
    part = os.environ.get("part")
    dots, instructions = read_input()
    if part == "part1":
        print(len(fold_once(dots, instructions)))
    else:
        print(print_dots(fold_dots(dots, instructions)))
