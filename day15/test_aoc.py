from collections import Counter
import unittest
from time import time
import aoc
from pathlib import Path

current_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(current_dir / "input.test.txt")
        print(data)
        self.assertTrue(all([isinstance(val, int) for line in data for val in line]))


class TestPart1(unittest.TestCase):
    def test_check_adjacent_nodes(self):
        data = [
            [1, 5],
            [2, 1],
        ]
        final_node = aoc.calculate_risk(data)
        self.assertEqual(final_node, 3)

    def test_calculate_lowest_cost_for_all_nodes(self):
        risk = [
            [2, 4, 1],
            [1, 6, 2],
        ]
        final_node = aoc.calculate_risk(risk)
        self.assertEqual(final_node, 7)

    def test_lowest_risk_of_example_input(self):
        risk = aoc.read_input(current_dir / "input.test.txt")
        full_cost = aoc.calculate_risk(risk)
        self.assertEqual(full_cost, 40)

    def test_lowest_risk_of_input(self):
        risk = aoc.read_input()
        full_cost = aoc.calculate_risk(risk)
        self.assertEqual(full_cost, 361)


class TestPart2(unittest.TestCase):
    def test_expand_board(self):
        board = [[4, 8], [9, 1]]
        expected = [
            [4, 8, 5, 9],
            [9, 1, 1, 2],
            [5, 9, 6, 1],
            [1, 2, 2, 3],
        ]
        actual = aoc.expand_board(board, expands=2)
        self.assertEqual(expected, actual)

    def test_example_expanded(self):
        board = aoc.read_input(current_dir / "input.test.txt")
        expanded_board = aoc.expand_board(board, 5)
        full_cost = aoc.calculate_risk(expanded_board)
        self.assertEqual(full_cost, 315)

    def test_input_expanded(self):
        board = aoc.read_input()
        expanded_board = aoc.expand_board(board, 5)
        full_cost = aoc.calculate_risk(expanded_board)
        self.assertEqual(full_cost, 2838)
