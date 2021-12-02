import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Submarine:
    horizontal: int = 0
    depth: int = 0

    def run(self, commands):
        for direction, amount in commands:
            self.navigate(direction, amount)

    def navigate(self, direction, amount):
        if direction == "forward":
            self.horizontal += amount
        else:
            self.depth += amount if direction == "down" else -amount

    def get_pos(self):
        return {"horizontal": self.horizontal, "depth": self.depth}

    def get_measurement(self):
        return self.horizontal * self.depth


class Submarine_with_updated_navigation(Submarine):
    aim: int = 0

    def navigate(self, direction, amount):
        if direction == "forward":
            self.horizontal += amount
            self.depth += self.aim * amount
        else:
            self.aim += amount if direction == "down" else -amount


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        for row in fid:
            direction, amount = row.split()
            yield (direction, int(amount))


def part1(instructions):
    submarine = Submarine()
    submarine.run(instructions)
    return submarine.get_measurement()


def part2(instructions):
    submarine = Submarine_with_updated_navigation()
    submarine.run(instructions)
    return submarine.get_measurement()


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1, "part2": part2}
    print(solver[part](read_input()))
