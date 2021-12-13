from itertools import chain
import unittest
from time import time
import aoc
from pathlib import Path

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(curr_dir / "input.txt")
        self.assertTrue(isinstance(val, int) for val in data)

    def test_flat_to_transpose(self):
        s = aoc.Size(4, 3)
        idx = s.flat_to_transposed()
        self.assertEqual(list(idx), [0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8, 11])

        s = aoc.Size(2, 3)
        d = [1, 2, 3, 4, 5, 6]
        self.assertEqual([d[i] for i in s.flat_to_transposed()], [1, 4, 2, 5, 3, 6])

    def test_transpost_to_flat(self):
        s = aoc.Size(4, 3)
        idx = s.transposed_to_flat()
        self.assertEqual(list(idx), [0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11])

        s = aoc.Size(2, 3)
        d = [1, 4, 2, 5, 3, 6]
        self.assertEqual([d[i] for i in s.transposed_to_flat()], [1, 2, 3, 4, 5, 6])


class TestPart1(unittest.TestCase):
    def test_small_example(self):
        data = [[2, 3, 5, 4], [3, 1, 4, 5]]
        result = aoc.solve_part1(data)
        self.assertEqual(result, 10)

    def test_part1_example(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        result = aoc.solve_part1(data)
        self.assertEqual(result, 15)

    def test_min_points(self):
        data = [3, 4, 2, 3, 2, 1, 4, 3]
        min_point = aoc.min_point_in_stream(data, width=4, height=2)
        self.assertEqual(
            min_point, [True, False, True, False, False, True, False, True]
        )

    def test_compare_neighbors(self):
        data = [
            [1, 2, 1],
            [4, 3, 2],
            [4, 1, 2],
        ]
        stream = list(chain(*data))
        self.assertEqual(
            aoc.is_smallest_in_neighborhood(stream, aoc.Size(3, 3)),
            [True, False, True, False, False, False, False, True, False],
        )

    def test_part1_with_input(self):
        t0 = time()
        data = aoc.read_input(curr_dir / "input.txt")
        result = aoc.solve_part1(data)
        print(time() - t0)
        self.assertEqual(result, 580)


class TestPart2(unittest.TestCase):
    def test_part2_example(self):
        data = aoc.read_input(curr_dir / "example_input.txt")
        result = aoc.get_basins(data)
        self.assertEqual(result, 1134)

    def test_collect_adjacent_from_point(self):
        data = [
            [9, 9, 1, 2],
            [5, 4, 9, 9],
            [3, 2, 5, 9],
            [9, 6, 9, 8],
            [9, 9, 9, 7],
        ]
        stream = list(chain(*data))
        size = aoc.Size(5, 4)
        result = aoc.get_group_around_point(stream, size, start_idx=9)
        self.assertEqual(len(result), 6)

    def test_part2_with_input(self):
        t0 = time()
        data = aoc.read_input(curr_dir / "input.txt")
        result = aoc.get_basins(data)
        t1 = time()
        print(t1 - t0)
        self.assertEqual(result, 856716)
