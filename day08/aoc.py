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
    segments, output = map(collect_sets, line.split(" | "))
    segment_group = {
        length: list(segment_group)
        for length, segment_group in groupby(sorted(segments, key=len), key=len)
    }
    coding_of = [set()] * 10
    coding_of[1] = segment_group[2][0]
    coding_of[7] = segment_group[3][0]
    coding_of[4] = segment_group[4][0]
    coding_of[8] = segment_group[7][0]

    top_left_and_mid = coding_of[4] - coding_of[1]
    coding_of[5] = pop_seg_diff_of_length(3, segment_group[5], top_left_and_mid)
    coding_of[0] = pop_seg_diff_of_length(5, segment_group[6], top_left_and_mid)

    coding_of[3], coding_of[2] = sort_on_diff_size(segment_group[5], coding_of[5])
    coding_of[9], coding_of[6] = sort_on_diff_size(segment_group[6], coding_of[3])

    return decode_output(output, coding_of)


def pop_seg_diff_of_length(target_length, segments, diff_reference_segment):
    for segment in segments:
        rem = segment - diff_reference_segment
        if len(rem) == target_length:
            segments.remove(segment)
            return segment


def sort_on_diff_size(segments, diff_reference_segment):
    return sorted(segments, key=lambda seg: seg - diff_reference_segment)


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
