from itertools import groupby
from typing import List
from pathlib import Path
import os
import numpy as np


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        numbers = list(map(int, fid.readline().split(",")))
        boards = read_boards(fid)
    return numbers, boards


class Board:
    def __init__(self, board):
        self._board = np.array(board)
        self._marked = np.full(self._board.shape, False)

    def __eq__(self, other) -> bool:
        if isinstance(other, Board):
            return np.array_equal(self._board, other._board)
        return False

    def mark_number(self, num):
        self._marked |= self._board == num

    def sum_of_unmarked(self):
        return self._board.sum() - sum(self._board[self._marked])

    def has_bingo(self):
        return any(
            (
                *self._marked.all(axis=0),
                *self._marked.all(axis=1),
            )
        )


def read_boards(stream):
    return [
        Board([[int(x) for x in row.split()] for row in board_rows])
        for content, board_rows in groupby(stream, lambda x: x.strip() != "")
        if content
    ]


def get_winner_board(boards: List[Board], numbers):
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.has_bingo():
                return board, number


def last_board_to_win(playing_boards: List[Board], numbers):
    for number in numbers:
        for board in playing_boards[:]:
            board.mark_number(number)
            if board.has_bingo():
                playing_boards.remove(board)
            if len(playing_boards) == 0:
                return board, number


def part1_solution(numbers, boards):
    winner, final_number = get_winner_board(boards, numbers)
    return winner.sum_of_unmarked() * final_number


def part2_solution(numbers, boards):
    last_board, final_number = last_board_to_win(boards, numbers)
    return last_board.sum_of_unmarked() * final_number


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1_solution, "part2": part2_solution}
    print(solver[part](*read_input()))
