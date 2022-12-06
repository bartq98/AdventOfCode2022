#!/bin/python3

elve_calories_intake = []

with open("./example_data_from_aoc_webpage.txt", 'r') as food_calories_data:
    totall_intake_of_current_elve = 0
    for single_food_calories in food_calories_data:
        if single_food_calories == "\n":
            elve_calories_intake.append(totall_intake_of_current_elve)
            totall_intake_of_current_elve = 0
            continue
        totall_intake_of_current_elve += int(single_food_calories.strip())

# Part #01
print(sorted(elve_calories_intake, reverse=True)[0])

# Part #02
print(sum(sorted(elve_calories_intake, reverse=True)[0:3]))