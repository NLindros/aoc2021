import os
from collections import Counter


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        polymer = fid.readline().strip()
        next(fid)
        insertions = {}
        for line in fid:
            a, b = line.strip().split(" -> ")
            insertions[tuple(a)] = b

        return polymer, insertions


def grow_polymer(pairs: Counter, insertions):
    new_pairs = Counter()
    for pair in pairs:
        num_of_pairs = pairs[pair]
        char = insertions[pair]
        new_pairs[(pair[0], char)] += num_of_pairs
        new_pairs[(char, pair[1])] += num_of_pairs
    return new_pairs


def run(polymer, insertions, steps):
    pairs = Counter(zip(polymer[:-1], polymer[1:]))
    for _ in range(steps):
        pairs = grow_polymer(pairs, insertions)
    return diff_most_common_to_least_common(pairs, last_element=polymer[-1])


def diff_most_common_to_least_common(pairs, last_element):
    elements = set()
    for a, b in pairs:
        elements.add(a)
        elements.add(b)

    element_count = Counter()
    for e in elements:
        for e_pair in [pair for pair in pairs if e is pair[0]]:
            element_count[e] += pairs[e_pair]
    element_count[last_element] += 1

    sorted_count = element_count.most_common()
    return sorted_count[0][1] - sorted_count[-1][1]


if __name__ == "__main__":
    part = os.environ.get("part")
    steps = {"part1": 10, "part2": 40}[part]
    polymer, insertions = read_input()
    print(run(polymer, insertions, steps))
