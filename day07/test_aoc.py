import unittest
import aoc
from pathlib import Path


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        self.assertTrue(isinstance(val, int) for val in data)


class TestPart1(unittest.TestCase):
    def test_part1_example(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = aoc.part1(data)
        self.assertEqual(result, 37)

    def test_median(self):
        self.assertEqual(aoc.find_median([1, 3, 4]), 3)
        self.assertEqual(aoc.find_median([1, 3, 4, 6]), 3.5)

    def test_part1_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        result = aoc.part1(data)
        self.assertEqual(result, 349357)


class TestPart2(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(next(aoc.count(5, step=1)), 5)
        neg_count = aoc.count(5, step=-1)
        self.assertEqual(next(neg_count), 5)
        self.assertEqual(next(neg_count), 4)

    def test_cost_function(self):
        data = [1, 6]
        self.assertEqual(aoc.cost_part2(data, 2), 1 + (1 + 2 + 3 + 4))
        self.assertEqual(aoc.cost_part2(data, 3), (1 + 2) + (1 + 2 + 3))

    def test_part1_example(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = aoc.part2(data)
        self.assertEqual(result, 168)

    def test_part2_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        result = aoc.part2(data)
        self.assertEqual(result, 96708205)
