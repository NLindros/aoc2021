import unittest
import aoc


class TestInput(unittest.TestCase):
    def test_read_input(self):
        result = aoc.read_input()
        self.assertTrue(all(isinstance(val, int) for val in result))


class TestPart1(unittest.TestCase):
    def test_example(self):
        depth = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(aoc.increases_of_depth(depth), 7)

    def test_real_input(self):
        depth = aoc.read_input()
        self.assertEqual(aoc.increases_of_depth(depth), 1266)


class TestPart2(unittest.TestCase):
    def test_example(self):
        depth = [607, 618, 618, 617, 647, 716, 769, 792]
        self.assertEqual(aoc.increases_of_depth_with_sliding_mean(depth), 5)

    def test_real_input(self):
        depth = aoc.read_input()
        self.assertEqual(aoc.increases_of_depth_with_sliding_mean(depth), 1217)
