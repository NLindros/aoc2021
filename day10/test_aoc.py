import unittest
import aoc
from pathlib import Path


example_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".splitlines()


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        self.assertTrue(isinstance(val, int) for val in data)


class TestPart1(unittest.TestCase):
    def test_find_incorrect_closing(self):
        line = "{([(<{}[<>[]}>{[]{[(<()>"
        self.assertEqual(aoc.find_incorrect_closing(line), "}")

    def test_example_input(self):
        result = aoc.solution_part_1(example_data)
        self.assertEqual(result, 26397)

    def test_input_data(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        result = aoc.solution_part_1(data)
        self.assertEqual(result, 271245)


class TestPart2(unittest.TestCase):
    def test_find_incomplete_closing(self):
        line = "[({(<(())[]>[[{[]{<()<>>"
        result = aoc.find_incomplete_closing(line)
        self.assertEqual("".join(result), "}}]])})]")

    def test_find_incomplete_closing_score(self):
        data = ["[({(<(())[]>[[{[]{<()<>>"]
        result = aoc.solution_part_2(data)
        self.assertEqual(result, 288957)

    def test_example_input(self):
        result = aoc.solution_part_2(example_data)
        self.assertEqual(result, 288957)

    def test_input_data(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        result = aoc.solution_part_2(data)
        self.assertEqual(result, 1685293086)
