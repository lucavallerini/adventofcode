#!/bin/env python3

import os

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


max_calories = []
current_calories = 0

for line in content:
    if line == '\n':
        max_calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line.replace('\n', ''))

max_calories.sort(reverse = True)

print("Top calories total: " + str(max_calories[0]))
print("Top three calories total: " + str(max_calories[0] + max_calories[1] + max_calories[2]))
