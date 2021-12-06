import unittest

from numpy.lib.function_base import bartlett
import aoc
from pathlib import Path
import numpy as np

local_dir = file_path = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        life_times = aoc.read_input(local_dir / "input.txt")
        self.assertTrue(all(isinstance(val, int) for val in life_times))


class TestPart1(unittest.TestCase):
    def test_example(self):
        self.assertEqual(aoc.run_life_simulation([3, 4, 3, 1, 2], days=18), 26)
        self.assertEqual(aoc.run_life_simulation([3, 4, 3, 1, 2], days=80), 5934)

    def test_with_input(self):
        self.assertEqual(
            aoc.run_life_simulation(aoc.read_input(local_dir / "input.txt"), days=80),
            362740,
        )


class TestPart2(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            aoc.run_life_simulation([3, 4, 3, 1, 2], days=256), 26984457539
        )

    def test_with_input(self):
        self.assertEqual(
            aoc.run_life_simulation(aoc.read_input(local_dir / "input.txt"), days=256),
            1644874076764,
        )
