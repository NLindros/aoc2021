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
    SIZE = (5, 5)

    def __init__(self, board):
        self._board = np.array(board)
        self._marked = np.full(self._board.shape, False)

    def __repr__(self) -> str:
        return f"Board({self._board}"

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


if __name__ == "__main__":

    part = os.environ.get("part")
    solver = {
        "part1": solve_part_1,
        "part2": solve_part_2,
    }

    file_input = read_input("input.txt")
    result = solver[part](file_input)

    print("Python")
    print(result)
