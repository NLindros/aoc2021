import unittest
from time import time
import aoc
from pathlib import Path

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        dots, instructions = aoc.read_input(curr_dir / "input.txt")
        self.assertEqual(len(dots), 820)
        self.assertEqual(len(instructions), 12)


class TestPart1(unittest.TestCase):
    def test_fold_once(self):
        dots, instructions = aoc.read_input(curr_dir / "example_input.txt")
        direction, fold = instructions[0]
        dots = aoc.fold_once(dots, direction, fold)
        self.assertEqual(len(dots), 17)

    def test_fold_once_on_input(self):
        dots, instructions = aoc.read_input(curr_dir / "input.txt")
        direction, fold = instructions[0]
        dots = aoc.fold_once(dots, direction, fold)
        self.assertEqual(len(dots), 682)


class TestPart2(unittest.TestCase):
    def test_fold_example(self):
        dots, instructions = aoc.read_input(curr_dir / "example_input.txt")
        dots = aoc.fold_dots(dots, instructions)
        aoc.print_dots(dots)

    def test_fold_input(self):
        dots, instructions = aoc.read_input(curr_dir / "input.txt")
        dots = aoc.fold_dots(dots, instructions)
        aoc.print_dots(dots)
