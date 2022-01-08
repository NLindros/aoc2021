import unittest
import aoc
from pathlib import Path

import binascii

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        transmission = aoc.read_input()
        self.assertTrue(isinstance(transmission, str))


class TestPart1(unittest.TestCase):
    def test_parse_literal_package(self):

        t = aoc.Transmission("D2FE28")
        result = aoc.parse_package(t)
        self.assertEqual(result.version, 6)
        self.assertEqual(result.type_ID, 4)
        self.assertEqual(result.value, 2021)

    def test_parse_transmission_with_fixed_length_subpackages(self):

        t = aoc.Transmission("38006F45291200")
        result = aoc.parse_package(t)
        self.assertEqual(result.version, 1)
        self.assertEqual(result.type_ID, 6)
        self.assertEqual(result.subpackages[0].value, 10)
        self.assertEqual(result.subpackages[1].value, 20)

    def test_parse_transmission_with_fixed_number_of_packages(self):

        t = aoc.Transmission("EE00D40C823060")
        result = aoc.parse_package(t)
        self.assertEqual(result.version, 7)
        self.assertEqual(result.type_ID, 3)
        self.assertEqual(result.subpackages[0].value, 1)
        self.assertEqual(result.subpackages[1].value, 2)
        self.assertEqual(result.subpackages[2].value, 3)

    def test_sum_versions_1(self):
        hex_str = "8A004A801A8002F478"
        result = aoc.part1(hex_str)
        self.assertEqual(result, 16)

    def test_sum_versions_2(self):
        hex_str = "620080001611562C8802118E34"
        result = aoc.part1(hex_str)
        self.assertEqual(result, 12)

    def test_sum_versions_3(self):
        hex_str = "C0015000016115A2E0802F182340"
        result = aoc.part1(hex_str)
        self.assertEqual(result, 23)

    def test_sum_versions_4(self):
        hex_str = "A0016C880162017C3686B18A3D4780"
        result = aoc.part1(hex_str)
        self.assertEqual(result, 31)

    def test_sum_versions_of_input(self):
        hex_str = aoc.read_input()
        result = aoc.part1(hex_str)
        self.assertEqual(result, 934)


class TestPart2(unittest.TestCase):
    def test_short_examples(self):
        examples = [
            ("C200B40A82", 3),
            ("04005AC33890", 54),
            ("880086C3E88112", 7),
            ("CE00C43D881120", 9),
            ("D8005AC2A8F0", 1),
            ("F600BC2D8F", 0),
            ("9C005AC2F8F0", 0),
            ("9C0141080250320F1802104A08", 1),
        ]
        for hex_str, expected in examples:
            result = aoc.part2(hex_str)
            self.assertEqual(result, expected)

    def test_example(self):
        hex_str = aoc.read_input()
        result = aoc.part2(hex_str)
        self.assertEqual(result, 912901337844)
