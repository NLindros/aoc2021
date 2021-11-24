import unittest
import aoc

class TestInput(unittest.TestCase):

    def test_read_input(self):
        result = aoc.read_input('input.txt')
        self.assertTrue(all(isinstance(val, int) for val in result))

class TestPart1(unittest.TestCase):

    def test_prime_index_product(self):
        input = [0, 3, 4, 42, 106, 107, 267, 269]
        expected = 3*1 + 107*5 + 269*7
        self.assertEqual(aoc.solve_part_1(input), expected)
    
    def test_prime_check(self):
        values = range(10)
        primes = [val for val in values if aoc.is_prime(val)]
        self.assertEquals(primes, [3,5,7])

    def test_real_input(self):
        values = aoc.read_input('input.txt')
        result_part_1 = aoc.solve_part_1(values)
        self.assertEqual(result_part_1, 3590905)
  
class TestPart2(unittest.TestCase):

    def test_example_input(self):
        values = [0, 3, 4, 42, 106, 107, 267, 269]
        result_part_2 = aoc.solve_part_2(values)
        self.assertEqual(result_part_2, 335)

    def test_real_input(self):
        values = aoc.read_input('input.txt')
        result_part_2 = aoc.solve_part_2(values)
        self.assertEqual(result_part_2, 1047)