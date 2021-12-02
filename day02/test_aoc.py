import unittest
import aoc
from day02.aoc import Submarine


class TestInput_Day2(unittest.TestCase):
    def test_read_input(self):
        result = aoc.read_input()
        for item in result:
            a, b = item
            self.assertTrue(isinstance(a, str))
            self.assertTrue(isinstance(b, int))


class TestPart1_Day2(unittest.TestCase):
    def test_example(self):
        commands = [
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ]
        submarine = aoc.Submarine()
        submarine.run(commands)
        self.assertEqual(submarine.get_pos(), {"horizontal": 15, "depth": 10})
        self.assertEqual(submarine.get_measurement(), 150)

    def test_real_data(self):
        commands = aoc.read_input()
        submarine = aoc.Submarine()
        submarine.run(commands)
        self.assertEqual(submarine.get_pos(), {"horizontal": 1998, "depth": 741})
        self.assertEqual(submarine.get_measurement(), 1480518)


class TestPart2_Day2(unittest.TestCase):
    def test_example(self):
        commands = [
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ]
        submarine = aoc.Submarine_with_updated_navigation()
        submarine.run(commands)
        self.assertEqual(submarine.get_pos(), {"horizontal": 15, "depth": 60})
        self.assertEqual(submarine.get_measurement(), 900)

    def test_real_data(self):
        commands = aoc.read_input()
        submarine = aoc.Submarine_with_updated_navigation()
        submarine.run(commands)
        self.assertEqual(submarine.get_pos(), {"horizontal": 1998, "depth": 642047})
        self.assertEqual(submarine.get_measurement(), 1282809906)
