#!/bin/python3


def parse(path: str) -> list:
    pair_list = []
    with open(path, "r") as pairs:
        for pair in pairs:
            pair_list.append(
                (
                    parse_pair(pair.strip().split(",")[0]),
                    parse_pair(pair.strip().split(",")[1]),
                )
            )
    return pair_list


def parse_pair(pair: str) -> dict:
    start, end = pair.split("-")
    return {"start": int(start), "end": int(end)}


def is_fullt_contained(pair_1: dict, pair_2: dict) -> bool:
    if (pair_1["start"] <= pair_2["start"] and pair_1["end"] >= pair_2["end"]) or (
        pair_2["start"] <= pair_1["start"] and pair_2["end"] >= pair_1["end"]
    ):
        return True
    else:
        return False


def is_overlapping(pair_1: dict, pair_2: dict) -> bool:
    if pair_1["end"] < pair_2["start"] or pair_2["end"] < pair_1["start"]:
        return False
    else:
        return True


if __name__ == "__main__":
    list_of_pairs = parse(path="./input.txt")

    # Section one:
    sum_of_pairs = sum(
        is_fullt_contained(pair_1=pair[0], pair_2=pair[1]) for pair in list_of_pairs
    )
    print(f"Section one: {sum_of_pairs}")

    # Section two:
    sum_of_pairs = sum(
        is_overlapping(pair_1=pair[0], pair_2=pair[1]) for pair in list_of_pairs
    )
    print(f"Section two: {sum_of_pairs}")
