import unittest

from numpy.lib.function_base import bartlett
import aoc
from pathlib import Path
import numpy as np


class TestInput(unittest.TestCase):
    def test_read_input(self):
        point_pairs = aoc.read_input(Path(__file__).parent / "example_input.txt")
        self.assertEqual(point_pairs[0], aoc.PointPair(0, 9, 5, 9))
        self.assertEqual(point_pairs[2], aoc.PointPair(9, 4, 3, 4))


class TestPart1(unittest.TestCase):
    def test_get_horz_intermidiate_line(self):
        pair = aoc.PointPair(1, 2, 1, 4)
        self.assertEqual(pair.get_line_points(), [(1, 2), (1, 3), (1, 4)])

    def test_get_vert_intermidiate_line(self):
        pair = aoc.PointPair(4, 2, 7, 2)
        self.assertEqual(pair.get_line_points(), [(4, 2), (5, 2), (6, 2), (7, 2)])

    def test_with_example_data(self):
        pairs = aoc.read_input(Path(__file__).parent / "example_input.txt")
        n_multiple_points = aoc.part1_solution(pairs)
        self.assertEqual(n_multiple_points, 5)

    def test_with_input_data(self):
        pairs = aoc.read_input(Path(__file__).parent / "input.txt")
        n_multiple_points = aoc.part1_solution(pairs)
        self.assertEqual(n_multiple_points, 6283)

    def test_inrange(self):
        self.assertEqual(list(aoc.in_range(1, 3)), [1, 2, 3])
        self.assertEqual(list(aoc.in_range(5, 2)), [5, 4, 3, 2])


class TestPart2(unittest.TestCase):
    def test_get_diag_intermidiate_line(self):
        pair = aoc.PointPair(2, 2, 5, 5)
        self.assertEqual(pair.get_diag_points(), [(2, 2), (3, 3), (4, 4), (5, 5)])

    def test_get_diag_intermidiate_line_2(self):
        pair = aoc.PointPair(9, 7, 7, 9)
        self.assertEqual(pair.get_diag_points(), [(9, 7), (8, 8), (7, 9)])

    def test_get_diag_intermidiate_line_3(self):
        pair = aoc.PointPair(5, 5, 8, 2)
        self.assertEqual(pair.get_diag_points(), [(5, 5), (6, 4), (7, 3), (8, 2)])

    def test_with_example_data(self):
        pairs = aoc.read_input(Path(__file__).parent / "example_input.txt")
        n_multiple_points = aoc.part2_solution(pairs)
        self.assertEqual(n_multiple_points, 12)

    def test_with_input_data(self):
        pairs = aoc.read_input(Path(__file__).parent / "input.txt")
        multi_points = aoc.part2_solution(pairs)
        self.assertEqual(multi_points, 18864)
