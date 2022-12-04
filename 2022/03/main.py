#!/bin/env python3

import os

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


def find_common_item(compartment_1, compartment_2, compartment_3 = None):
    for item in compartment_1:
        if item in compartment_2 and (compartment_3 == None or item in compartment_3):
            return item
    return None


# ASCII
# A - Z [65, 90] -> [27, 52]
# a - z -> [97, 122] -> [1, 26]
def compute_priority(item):
    ascii = ord(item)
    return (ascii - 38) if ascii < 91 else (ascii - 96)


total_priorities = 0
for line in content:
    rucksack = line.replace('\n', '')
    middle_index = int(len(rucksack)/2)
    compartment_1 = rucksack[:middle_index]
    compartment_2 = rucksack[middle_index:]
    total_priorities += compute_priority(find_common_item(compartment_1, compartment_2))


print("Total priorities: " + str(total_priorities))


total_group_priorities = 0
for i in range(0, len(content), 3):
    rucksack_1 = content[i].replace('\n', '')
    rucksack_2 = content[i+1].replace('\n', '')
    rucksack_3 = content[i+2].replace('\n', '')
    total_group_priorities += compute_priority(find_common_item(rucksack_1, rucksack_2, rucksack_3))

print("Total priorities: " + str(total_group_priorities))