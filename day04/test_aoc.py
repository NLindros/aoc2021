import unittest

from numpy.lib.function_base import bartlett
import aoc
from pathlib import Path
import numpy as np


class TestInput(unittest.TestCase):
    def test_collect_boards(self):
        data = (x for x in ["1 2", "2 3", "", "5 6", "7 8", ""])
        boards = aoc.read_boards(data)
        self.assertEqual(len(boards), 2)
        self.assertEqual(boards[0], aoc.Board([[1, 2], [2, 3]]))

    def test_read_input(self):
        result = aoc.read_input()
        self.assertEqual(len(result), 2)
        numbers, boards = result
        self.assertTrue(all(isinstance(val, int) for val in numbers))
        self.assertTrue(all(isinstance(board, aoc.Board) for board in boards))


class TestPart1(unittest.TestCase):
    def test_with_example_data(self):
        numbers, boards = aoc.read_input(Path(__file__).parent / "example_input.txt")
        winner, final_num = aoc.get_winner_board(boards, numbers)
        expected_winner = aoc.Board(
            [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ]
        )
        self.assertEqual(winner, expected_winner)
        self.assertEqual(winner.sum_of_unmarked() * final_num, 4512)

    def test_get_unmarked(self):
        board = aoc.Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        board.mark_number(4)
        board.mark_number(5)
        self.assertEqual(board.sum_of_unmarked(), sum(range(10)) - 4 - 5)

    def test_check_bingo(self):
        board = aoc.Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        board.mark_number(4)
        board.mark_number(5)
        self.assertFalse(board.has_bingo())
        board.mark_number(6)
        self.assertTrue(board.has_bingo())

    def test_with_real_input(self):
        numbers, boards = aoc.read_input(Path(__file__).parent / "input.txt")
        winner, final_number = aoc.get_winner_board(boards, numbers)
        self.assertEqual(winner.sum_of_unmarked() * final_number, 82440)


class TestPart2(unittest.TestCase):
    def test_last_to_win_in_example(self):
        numbers, boards = aoc.read_input(Path(__file__).parent / "example_input.txt")
        last_board, final_number = aoc.last_board_to_win(boards, numbers)
        self.assertEqual(final_number, 13)
        self.assertEqual(last_board.sum_of_unmarked() * final_number, 1924)

    def test_last_to_win_with_input(self):
        numbers, boards = aoc.read_input(Path(__file__).parent / "input.txt")
        last_board, final_number = aoc.last_board_to_win(boards, numbers)
        self.assertEqual(last_board.sum_of_unmarked() * final_number, 20774)
