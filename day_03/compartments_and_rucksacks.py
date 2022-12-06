#!/bin/python3

POINTS_FOR_ITEM = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_compartments_of_rucksacks(rucksack: list):
    half = len(rucksack)//2
    first_half, second_half = rucksack[:half], rucksack[half:]
    return first_half, second_half

def get_common_item(compartment_1, compartment_2):
    item_set_1, item_set_2 = set(compartment_1), set(compartment_2)
    common_item = item_set_1.intersection(item_set_2)
    return common_item.pop()

def get_points_of_item(item: str):
    print(item, POINTS_FOR_ITEM.index(item))
    return POINTS_FOR_ITEM.index(item)

def parse_rucksacks_file(path: str) -> list:
    rucksacks_list = []
    with open(path, 'r') as rucksacks_table:
        for rucksack in rucksacks_table:
            rucksacks_list.append(tuple(rucksack.strip()))
    return rucksacks_list

def calculate_priorities(path: str) -> int:
    rucksacks = parse_rucksacks_file(path=path)
    priorities_sum = 0
    for rucksack in rucksacks:
        first_compartment, second_compartment = get_compartments_of_rucksacks(rucksack)
        common_item = get_common_item(first_compartment, second_compartment)
        priorities_sum += get_points_of_item(common_item)
    return priorities_sum

def find_badges(path: str) -> int:
    rucksacks = parse_rucksacks_file(path=path)
    badges_sum = 0
    for i in range(0, len(rucksacks), 3):
        badge_letter = set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])).pop()
        badges_sum += get_points_of_item(badge_letter)
    return badges_sum


if __name__ == "__main__":
    sum_of_priorities = calculate_priorities(path="./rucksacks.txt")
    print(sum_of_priorities)
    badges = find_badges(path="./rucksacks.txt")
    print(badges)