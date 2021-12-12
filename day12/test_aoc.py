import unittest
from time import time
import aoc
from pathlib import Path

curr_dir = Path(__file__).parent


class TestInput(unittest.TestCase):
    def test_read_input(self):
        pass

    def test_parse_to_connection(self):
        raw = [
            "start-a",
            "start-b",
            "b-a",
            "a-end",
        ]
        expected = {
            "start": {"a", "b"},
            "b": {"a"},
            "a": {"b", "end"},
        }
        result = aoc.build(raw)
        self.assertEqual(result["b"], expected["b"])
        self.assertEqual(result["a"], expected["a"])


class TestPart1(unittest.TestCase):
    def test_find_paths_in_cave_1(self):
        cave = aoc.build(
            [
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ]
        )
        paths = aoc.find_paths_part_1(cave)
        self.assertEqual(
            set(map(",".join, paths)),
            set(
                [
                    "start,A,b,A,c,A,end",
                    "start,A,b,A,end",
                    "start,A,b,end",
                    "start,A,c,A,b,A,end",
                    "start,A,c,A,b,end",
                    "start,A,c,A,end",
                    "start,A,end",
                    "start,b,A,c,A,end",
                    "start,b,A,end",
                    "start,b,end",
                ]
            ),
        )

    def test_slightly_larger_example(self):
        cave = aoc.build(
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ]
        )
        result = aoc.find_paths_part_1(cave)
        self.assertEqual(len(result), 19)

    def test_largest_example(self):
        cave = aoc.build(
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ]
        )
        result = aoc.find_paths_part_1(cave)
        self.assertEqual(len(result), 226)

    def test_with_input(self):
        cave = aoc.read_input(curr_dir / "input.txt")
        result = aoc.find_paths_part_1(cave)
        self.assertEqual(len(result), 3497)


class TestPart2(unittest.TestCase):
    def test_find_paths_in_cave_1(self):
        cave = aoc.build(
            [
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ]
        )
        expected = set(
            [
                "start,A,b,A,b,A,c,A,end",
                "start,A,b,A,b,A,end",
                "start,A,b,A,b,end",
                "start,A,b,A,c,A,b,A,end",
                "start,A,b,A,c,A,b,end",
                "start,A,b,A,c,A,c,A,end",
                "start,A,b,A,c,A,end",
                "start,A,b,A,end",
                "start,A,b,d,b,A,c,A,end",
                "start,A,b,d,b,A,end",
                "start,A,b,d,b,end",
                "start,A,b,end",
                "start,A,c,A,b,A,b,A,end",
                "start,A,c,A,b,A,b,end",
                "start,A,c,A,b,A,c,A,end",
                "start,A,c,A,b,A,end",
                "start,A,c,A,b,d,b,A,end",
                "start,A,c,A,b,d,b,end",
                "start,A,c,A,b,end",
                "start,A,c,A,c,A,b,A,end",
                "start,A,c,A,c,A,b,end",
                "start,A,c,A,c,A,end",
                "start,A,c,A,end",
                "start,A,end",
                "start,b,A,b,A,c,A,end",
                "start,b,A,b,A,end",
                "start,b,A,b,end",
                "start,b,A,c,A,b,A,end",
                "start,b,A,c,A,b,end",
                "start,b,A,c,A,c,A,end",
                "start,b,A,c,A,end",
                "start,b,A,end",
                "start,b,d,b,A,c,A,end",
                "start,b,d,b,A,end",
                "start,b,d,b,end",
                "start,b,end",
            ]
        )
        result = aoc.find_paths_part_2(cave)
        self.assertEqual(set(map(",".join, result)), expected)

    def test_slightly_larger_example(self):
        cave = aoc.build(
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ]
        )
        result = aoc.find_paths_part_2(cave)
        self.assertEqual(len(result), 103)

    def test_largest_example(self):
        cave = aoc.build(
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ]
        )
        result = aoc.find_paths_part_2(cave)
        self.assertEqual(len(result), 3509)

    def test_with_input(self):
        cave = aoc.read_input(curr_dir / "input.txt")
        result = aoc.find_paths_part_2(cave)
        self.assertEqual(len(result), 93686)
