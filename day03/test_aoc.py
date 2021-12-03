from datetime import date
import unittest
import aoc
from day03.aoc import most_common_in_rows


class TestInput(unittest.TestCase):
    def _test_read_input(self):
        result = aoc.read_input()
        self.assertTrue(all(isinstance(val, int) for val in result))


class TestPart1(unittest.TestCase):
    def test_most_common(self):
        data = [
            "011",
            "101",
            "101",
        ]
        self.assertEqual(aoc.most_common_in_rows(data), "101")

    def test_invert_binary(self):
        self.assertEqual(aoc.invert_binary("101"), "010")

    def test_example(self):
        readout = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        self.assertEqual(aoc.power_consumption(readout), 198)

    def test_most_common_of_input_data(self):
        data = aoc.read_input()
        top = aoc.most_common_in_rows(data)
        self.assertEqual(top, "001101001100")

    def test_real_input(self):
        data = aoc.read_input()
        self.assertEqual(aoc.power_consumption(data), 2743844)


class TestPart2(unittest.TestCase):
    def test_example(self):
        data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        oxygen = aoc.life_support_decode(
            data, to_keep=lambda count: "1" if count["1"] >= count["0"] else "0"
        )
        co2 = aoc.life_support_decode(
            data, to_keep=lambda count: "1" if count["1"] < count["0"] else "0"
        )
        self.assertEqual(oxygen, "10111")
        self.assertEqual(co2, "01010")
        self.assertEqual(aoc.life_support_rating(data), 230)

    def test_with_input(self):
        data = aoc.read_input()
        self.assertEqual(aoc.life_support_rating(data), 6677951)
