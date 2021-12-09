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
        data = [[2, 3, 5, 4], [3, 1, 4, 5]]
        result = aoc.solve_part1(data)
        self.assertEqual(result, 10)

    def test_part1_example(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        result = aoc.solve_part1(data)
        self.assertEqual(result, 15)

    def test_compare_neighbors(self):
        data = [
            [1, 2, 1],
            [4, 3, 2],
            [4, 1, 2],
        ]

        self.assertEqual(
            aoc.is_smallest_in_neighborhood(data),
            [[True, False, True], [False, False, False], [False, True, False]],
        )

    def test_part1_with_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        t0 = time()
        result = aoc.solve_part1(data)
        print(time() - t0)
        self.assertEqual(result, 580)


class TestPart2(unittest.TestCase):
    def test_part2_example(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        t0 = time()
        result = aoc.get_basins(data)
        t1 = time()
        print(t1 - t0)
        self.assertEqual(result, 1134)

    def test_get_low_coord(self):
        data = [
            [9, 3, 2],
            [2, 9, 2],
        ]
        self.assertEqual(aoc.basin_points(data), [(0, 1), (0, 2), (1, 0), (1, 2)])

    def test_collect_adjacent(self):
        data = [
            [9, 9, 1, 2],
            [5, 4, 9, 9],
            [3, 2, 5, 9],
            [9, 6, 9, 8],
        ]
        coordinates = aoc.basin_points(data)
        result = aoc.get_group(coordinates, start=(2, 1))
        self.assertEqual(set(result), {(1, 0), (2, 0), (1, 1), (2, 1), (3, 1), (2, 2)})

    def test_part2_with_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        result = aoc.get_basins(data)
        self.assertEqual(result, 856716)
