#!/bin/python3

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

CRATES_FILE_WIDTH = 36
SHIFT_INDEX = 4


def parse_moves(path: str) -> list:
    move_list = []
    with open(path, "r") as pairs:
        for pair in pairs:
            splitted_pair = pair.strip().split(" ")
            move_list.append(
                {
                    "how_many": int(splitted_pair[1]),
                    "from": int(splitted_pair[3]) - 1,
                    "to": int(splitted_pair[5]) - 1,
                }
            )
    return move_list


def parse_crates(path: str) -> list:
    crate_list = [[] for i in range(9)]
    with open(path, "r") as file:
        for line in file:
            for letter_index in range(1, CRATES_FILE_WIDTH, SHIFT_INDEX):
                if line[letter_index].isalpha():
                    crate_list[letter_index // SHIFT_INDEX].append(line[letter_index])

    return crate_list


if __name__ == "__main__":
    moves  = parse_moves("./moves.txt")
    crates = parse_crates("./initial_crates_configuration.txt")

    for move in moves:
        how_many, from_i, to = move["how_many"], move["from"], move["to"]
        fetched_crates = crates[from_i][:how_many]
        del crates[from_i][:how_many]
        crates[to] = fetched_crates + crates[to]


    for i, crate in enumerate(crates):
        print(f"{crate[0]}", end="")
