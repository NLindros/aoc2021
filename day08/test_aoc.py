import unittest
import aoc
from pathlib import Path


example_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".splitlines()


class TestInput(unittest.TestCase):
    def test_read_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        self.assertTrue(isinstance(val, int) for val in data)


class TestPart1(unittest.TestCase):
    def test_count_unique_example_output(self):
        amount = aoc.solution_part_1(example_data)
        self.assertEqual(amount, 26)

    def test_count_unique_output(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        amount = aoc.solution_part_1(data)
        self.assertEqual(amount, 245)


class TestPart2(unittest.TestCase):
    def test_decode_segments(self):
        line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        result = aoc.decode_line(line)
        self.assertEqual(result, 5353)

    def test_decode_segments_2(self):
        line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
        result = aoc.decode_line(line)
        self.assertEqual(result, 8394)

    def test_sum_of_example(self):
        result = aoc.solution_part_2(example_data)
        self.assertEqual(result, 61229)

    def test_sum_of_input(self):
        data = aoc.read_input(Path(__file__).parent / "input.txt")
        result = aoc.solution_part_2(data)
        self.assertEqual(result, 983026)
