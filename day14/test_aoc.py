from collections import Counter
import unittest
from time import time
import aoc
from pathlib import Path

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        pair_count, insertions = aoc.read_input(curr_dir / "input.test.txt")
        self.assertEqual(pair_count, "NNCB")
        self.assertEqual(insertions[("C", "H")], "B")
        self.assertEqual(insertions[("C", "N")], "C")


class TestPart1(unittest.TestCase):
    def test_example_step_10_diff(self):
        polymer, insertions = aoc.read_input(curr_dir / "input.test.txt")
        end_diff = aoc.run(polymer, insertions, steps=10)
        self.assertEqual(end_diff, 1588)

    def test_input_step_10_diff(self):
        polymer, insertions = aoc.read_input(curr_dir / "input.txt")
        end_diff = aoc.run(polymer, insertions, steps=10)
        self.assertEqual(end_diff, 2435)


class TestPart2(unittest.TestCase):
    def test_example_step_10_diff(self):
        polymer, insertions = aoc.read_input(curr_dir / "input.test.txt")
        end_diff = aoc.run(polymer, insertions, steps=40)
        self.assertEqual(end_diff, 2188189693529)

    def test_input_step_10_diff(self):
        polymer, insertions = aoc.read_input(curr_dir / "input.txt")
        end_diff = aoc.run(polymer, insertions, steps=40)
        self.assertEqual(end_diff, 2587447599164)
