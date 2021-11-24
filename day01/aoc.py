from math import sqrt
from itertools import cycle
import os

def read_input(file_path):
    with open(file_path, 'r') as fid:
        return [int(val) for val in fid]

def solve_part_1(values):
    return sum(idx*val for idx, val in enumerate(values) if is_prime(val))
    
def solve_part_2(values):
    signs = cycle([1, -1])
    return sum([
        sign * val for val, sign in zip(values, signs) if not is_prime(val)
    ])

def is_prime(value):
    if value <= 2:
        return False
    for div in range(2, int(sqrt(value)+1)):
        if value % div == 0:
            return False
    return True


if __name__ == '__main__':

    part = os.environ.get('part')
    solver = {
        'part1': solve_part_1,
        'part2': solve_part_2,
        }

    file_input = read_input('input.txt')
    result = solver[part](file_input)

    print('Python')
    print(result)
