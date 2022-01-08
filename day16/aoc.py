import os
from math import prod


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return fid.readline().strip()


LITERAL_VALUE_TYPE = 4
type_ID_operators = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}


class Package:
    def __init__(self, version: int, type_ID: int):
        self.version = version
        self.type_ID = type_ID
        self._value = None
        self.subpackages = []

    @property
    def value(self):
        if self._value:
            return self._value
        sub_values = [package.value for package in self.subpackages]
        result = type_ID_operators[self.type_ID](sub_values)
        return int(result)

    @value.setter
    def value(self, value):
        self._value = value


class Transmission:
    def __init__(self, hex_str):
        self._bin_str = self._convert_hex(hex_str)
        self.current = 0

    def _convert_hex(self, hex_str):
        return "".join(format(int(char, base=16), "0>4b") for char in hex_str)

    def read(self, bits=1):
        start, stop = self.current, self.current + bits
        self.current = stop
        return self._bin_str[start:stop]


def parse_package(transmission: Transmission):
    version = int(transmission.read(3), base=2)
    type_ID = int(transmission.read(3), base=2)

    package = Package(version, type_ID)

    if type_ID == LITERAL_VALUE_TYPE:
        package.value = get_literal_value(transmission)
    else:
        length_ID = transmission.read()
        if length_ID == "0":
            sub_package_length = int(transmission.read(15), base=2)
            parse_limit = transmission.current + sub_package_length
            while transmission.current < parse_limit:
                package.subpackages.append(parse_package(transmission))
        else:
            number_of_sub_packages = int(transmission.read(11), base=2)
            package.subpackages = [
                parse_package(transmission) for _ in range(number_of_sub_packages)
            ]

    return package


def get_literal_value(transmission):
    bin_str = ""
    final_group = False
    while not final_group:
        final_group = transmission.read() == "0"
        bin_str += transmission.read(4)
    return int(bin_str, base=2)


def get_version_sum(package):
    process_stack = [package]
    version_sum = 0
    while process_stack:
        current = process_stack.pop()
        process_stack.extend(current.subpackages)
        version_sum += current.version
    return version_sum


def part1(hex_str):
    transmission = Transmission(hex_str)
    package = parse_package(transmission)
    return get_version_sum(package)


def part2(hex_str):
    transmission = Transmission(hex_str)
    package = parse_package(transmission)
    return package.value


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": part1, "part2": part2}[part]
    print(solver(read_input()))
