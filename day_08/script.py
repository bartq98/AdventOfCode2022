#!/bin/python3

def parse_map(path: str) -> list:
    map_rows = []
    with open(path, "r") as pairs:
        for pair in pairs:
            raw_line = pair.strip()
            row = [int(elem) for elem in raw_line]
            map_rows.append(row)
    return map_rows


def count_boundary_trees(map: list) -> int:
    rows = len(map)
    cols = len(map[0])
    return cols * 2 + (rows - 2) * 2


def get_column(map, col) -> int:
    column = []
    for i in range(len(map)):
        column.append(map[i][col])
    return column


def get_from_left(map, row, col):
    return map[row][:col]


def get_to_right(map, row, col):
    return map[row][col + 1 :]


def get_from_above(map, row, col):
    column = get_column(map, col)
    return column[:row]


def get_to_bottom(map, row, col):
    column = get_column(map, col)
    return column[row + 1 :]


def is_visible(map, column, row) -> bool:
    current_row  = map[row]
    current_col  = get_column(map, column)
    current_elem = map[row][column]

    print(f"Current elem on [{row}][{column}] is {current_elem}")

    if (
        max(get_from_left(map, row=row, col=column))     < current_elem
        or max(get_to_right(map, row=row, col=column))   < current_elem
        or max(get_from_above(map, row=row, col=column)) < current_elem
        or max(get_to_bottom(map, row=row, col=column))  < current_elem
    ):

        print(f"For [{row}][{column}] is visible")
        return True
    else:
        print(f"For [{row}][{column}] is not visible")
        return False


def iterate_throught_internal_trees(map):
    map_rows = len(map)
    map_cols = len(map[0])
    for row in range(1, map_rows - 1):
        for col in range(1, map_cols - 1):
            yield map[row][col]


def calculate_trees(map):
    map_rows = len(map)
    map_cols = len(map[0])
    sum_of_trees = count_boundary_trees(map)
    for row in range(1, map_rows - 1):
        for col in range(1, map_cols - 1):
            sum_of_trees += is_visible(map, col, row)
    return sum_of_trees


def sum_scenic_score(elem: int, tree_list: list, reverse=False) -> int:
    scenic_sum = 0
    if reverse:
        tree_list = tree_list[::-1]
    for i, list_elem in enumerate(tree_list):
        if list_elem >= elem:
            scenic_sum += 1
            break
        scenic_sum += 1
    return scenic_sum


def calculate_scenic_score(map, row, col):

    from_left  = get_from_left( map, row=row, col=col)
    to_right   = get_to_right(  map, row=row, col=col)
    from_above = get_from_above(map, row=row, col=col)
    to_bottom  = get_to_bottom( map, row=row, col=col)

    points_from_left = sum_scenic_score(
        elem=map[row][col], tree_list=from_left,  reverse=True
    )
    points_to_right = sum_scenic_score(
        elem=map[row][col], tree_list=to_right,   reverse=False
    )
    points_from_above = sum_scenic_score(
        elem=map[row][col], tree_list=from_above, reverse=True
    )
    points_to_bottom = sum_scenic_score(
        elem=map[row][col], tree_list=to_bottom,  reverse=False
    )

    return points_from_left * points_to_right * points_from_above * points_to_bottom


if __name__ == "__main__":
    map = parse_map(path="./input.txt")
    highest = 0
    for row, full_row in enumerate(map):
        for col, elem in enumerate(full_row):
            if calculate_scenic_score(map, row, col) > highest:
                highest = calculate_scenic_score(map, row, col)
    print(highest)
