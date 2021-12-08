from itertools import count, groupby
from pathlib import Path
from statistics import median
import os


def read_input(file_path=Path(__file__).parent / "input.txt"):
    with open(file_path, "r") as fid:
        return fid.readlines()


def count_output(data):
    target_lengths = [2, 3, 4, 7]
    matching_segments = [
        [seg for seg in collect_sets(line.split("|")[-1]) if len(seg) in target_lengths]
        for line in data
    ]
    return sum(map(len, matching_segments))


def collect_sets(signals):
    return map(set, signals.strip().split(" "))


def decode_line(line):
    patterns, output = map(collect_sets, line.split(" | "))
    patterns_by_length = {
        length: list(pattern_group)
        for length, pattern_group in groupby(sorted(patterns, key=len), key=len)
    }
    coding = [set()] * 10
    coding[1] = patterns_by_length[2][0]
    coding[7] = patterns_by_length[3][0]
    coding[4] = patterns_by_length[4][0]
    coding[8] = patterns_by_length[7][0]
    top_side_and_middle_segments = coding[4] - coding[1]
    for pattern in patterns_by_length[5]:
        segments = pattern - top_side_and_middle_segments
        if len(segments) == 3:
            patterns_by_length[5].remove(pattern)
            coding[5] = pattern
            break
    for pattern in patterns_by_length[5]:
        segments = pattern - coding[5]
        if len(segments) == 1:
            coding[3] = pattern
        if len(segments) == 2:
            coding[2] = pattern

    for pattern in patterns_by_length[6]:
        segments = pattern - top_side_and_middle_segments
        if len(segments) == 5:
            patterns_by_length[6].remove(pattern)
            coding[0] = pattern
    for pattern in patterns_by_length[6]:
        segments = pattern - coding[3]
        if len(segments) == 1:
            coding[9] = pattern
        if len(segments) == 2:
            coding[6] = pattern

    return decode_output(output, coding)


def decode_output(output, coding):
    result = []
    for o in output:
        for num, segment in enumerate(coding):
            if o == segment:
                result.append(num)
                break
    return int("".join(map(str, result)))


def sum_result(data):
    return sum([decode_line(line) for line in data])


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": count_output, "part2": sum_result}
    print(solver[part](read_input()))
