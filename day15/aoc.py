import os
from collections import namedtuple


def read_input(file_path="input.txt"):
    with open(file_path, "r") as fid:
        return [[int(val) for val in line.strip()] for line in fid]


def calculate_risk(cost_map):
    height, width = len(cost_map), len(cost_map[0])
    height_idx_lim = (height - 1) * width

    cost_map = [x for line in cost_map for x in line]
    node = namedtuple("Node", ["previous", "cost"])

    nodes = [node(None, float("inf"))] * len(cost_map)
    nodes[0] = node(None, cost_map[0])

    nodes_to_evaluate = set()
    search_idx = 0

    while True:
        for adj_idx in get_adjacent_points(search_idx, width, height_idx_lim):
            if adj_idx:
                this_cost = nodes[search_idx].cost + cost_map[adj_idx]
                if this_cost < nodes[adj_idx].cost:
                    nodes[adj_idx] = (search_idx, this_cost)
                    nodes_to_evaluate.add(adj_idx)
        if not nodes_to_evaluate:
            break
        search_idx = nodes_to_evaluate.pop()

    cost_of_path = nodes[-1].cost - nodes[0].cost
    return cost_of_path


def get_adjacent_points(idx, width, height_idx_lime):
    return [
        idx - 1 if idx % width else None,
        idx + 1 if (idx + 1) % width else None,
        idx - width if idx >= width else None,
        idx + width if idx < height_idx_lime else None,
    ]


def expand_board(board, expands=5):
    horizontal_expand = [
        [val + x for x in range(expands) for val in row] for row in board
    ]
    vertical_expand = [
        [val + x for val in row] for x in range(expands) for row in horizontal_expand
    ]
    full_wrap_around = [
        [val % 9 if val > 9 else val for val in row] for row in vertical_expand
    ]
    return full_wrap_around


if __name__ == "__main__":
    part = os.environ.get("part")
    risk_map = read_input()
    if part == "part2":
        risk_map = expand_board(risk_map, expands=5)
    result = calculate_risk(risk_map)
    print(result)
