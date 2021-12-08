import os


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return fid.readlines()


def solution_part_1(data):
    target_lengths = [2, 3, 4, 7]
    segment_lengths = [
        len([seg for seg in collect_sets(line.split("|")[-1]) if len(seg) in target_lengths])
        for line in data
    ]
    return sum(segment_lengths)


def collect_sets(signals):
    return map(set, signals.strip().split(" "))


def decode_line(line):
    segments, output = map(collect_sets, line.split("|"))
    coding_of = [None] * 10
    coding_of[1], coding_of[7], coding_of[4], *multi_groups, coding_of[8] = sorted(
        segments, key=len
    )
    seg_of_size_5, seg_of_size_6 = multi_groups[:3], multi_groups[3:]

    top_left_and_mid = coding_of[4] - coding_of[1]
    coding_of[5] = pop_seg_with_diff_of_length(3, seg_of_size_5, top_left_and_mid)
    coding_of[0] = pop_seg_with_diff_of_length(5, seg_of_size_6, top_left_and_mid)

    coding_of[3], coding_of[2] = sort_on_diff_size(seg_of_size_5, coding_of[5])
    coding_of[9], coding_of[6] = sort_on_diff_size(seg_of_size_6, coding_of[3])

    return decode_output(output, coding_of)


def pop_seg_with_diff_of_length(target_length, segments, diff_reference_segment):
    for segment in segments:
        rem = segment - diff_reference_segment
        if len(rem) == target_length:
            segments.remove(segment)
            return segment


def sort_on_diff_size(segments, diff_reference_segment):
    return sorted(segments, key=lambda seg: seg - diff_reference_segment)


def decode_output(outputs, coding):
    result = [
        str(num)
        for output in outputs
        for num, segment in enumerate(coding)
        if output == segment
    ]
    return int("".join(result))


def solution_part_2(data):
    return sum(map(decode_line, data))


if __name__ == "__main__":
    part = os.environ.get("part")
    solver = {"part1": solution_part_1, "part2": solution_part_2}
    print(solver[part](read_input()))
