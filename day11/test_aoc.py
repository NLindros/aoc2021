import unittest
from time import time
import aoc
from pathlib import Path

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        self.assertTrue(isinstance(val, int) for val in data)


class TestPart1(unittest.TestCase):
    def test_small_example(self):
        data = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        expected = [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ]
        result, flashes = aoc.dumbo_simulate(data, steps=1)
        self.assertEqual(result, expected)
        self.assertEqual(flashes, 9)

    def test_larger_example(self):
        data = [
            [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
        ]
        expected = [
            [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
            [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
            [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
            [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
            [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
            [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
            [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
            [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
            [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
            [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
        ]
        result, flashes = aoc.dumbo_simulate(data, steps=1)
        self.assertEqual(result, expected)
        self.assertEqual(flashes, 0)

    def test_get_adjacent(self):
        size = aoc.Size(3, 4)
        self.assertEqual(
            len(set(aoc.get_adjacent_points(row_idx=1, col_idx=1, size=size))), 8
        )
        self.assertEqual(
            len(set(aoc.get_adjacent_points(row_idx=0, col_idx=1, size=size))), 5
        )
        self.assertEqual(
            len(set(aoc.get_adjacent_points(row_idx=0, col_idx=0, size=size))), 3
        )
        self.assertEqual(
            len(set(aoc.get_adjacent_points(row_idx=1, col_idx=0, size=size))), 5
        )
        self.assertEqual(
            len(set(aoc.get_adjacent_points(row_idx=4, col_idx=1, size=size))), 5
        )

    def test_with_example_input(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        expected = [
            [0, 4, 8, 1, 1, 1, 2, 9, 7, 6],
            [0, 0, 3, 1, 1, 1, 2, 0, 0, 9],
            [0, 0, 4, 1, 1, 1, 2, 5, 0, 4],
            [0, 0, 8, 1, 1, 1, 1, 4, 0, 6],
            [0, 0, 9, 9, 1, 1, 1, 3, 0, 6],
            [0, 0, 9, 3, 5, 1, 1, 2, 3, 3],
            [0, 4, 4, 2, 3, 6, 1, 1, 3, 0],
            [5, 5, 3, 2, 2, 5, 2, 3, 5, 0],
            [0, 5, 3, 2, 2, 5, 0, 6, 0, 0],
            [0, 0, 3, 2, 2, 4, 0, 0, 0, 0],
        ]
        result, flashes = aoc.dumbo_simulate(data, steps=10)
        self.assertEqual(result, expected)
        self.assertEqual(flashes, 204)

    def test_with_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        result, flashes = aoc.dumbo_simulate(data, steps=100)
        self.assertEqual(flashes, 1686)


class TestPart2(unittest.TestCase):
    def test_with_example(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        step = aoc.run_to_flash(data)
        self.assertEqual(step, 195)

    def test_with_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        step = aoc.run_to_flash(data)
        self.assertEqual(step, 360)
