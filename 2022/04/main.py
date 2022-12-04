#!/bin/env python3

import os

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


def total_overlap(range_1, range_2):
    return True if (range_1[0] >= range_2[0] and range_1[1] <= range_2[1]) \
        or (range_2[0] >= range_1[0] and range_2[1] <= range_1[1]) else False


def partial_overlap(range_1, range_2):
    return True if (range_1[0] >= range_2[0] and range_1[0] <= range_2[1]) \
        or (range_1[1] >= range_2[0] and range_1[1] <= range_2[1]) \
        or (range_2[0] >= range_1[0] and range_2[0] <= range_1[1]) \
        or (range_2[1] >= range_1[0] and range_2[1] <= range_1[1]) else False


total_overlaps = 0
partial_overlaps = 0
for pair in content:
    pairs = pair.replace('\n', '').split(',')
    range_1 = list(map(lambda id: int(id), pairs[0].split('-')))
    range_2 = list(map(lambda id: int(id), pairs[1].split('-')))
    total_overlaps += 1 if total_overlap(range_1, range_2) else 0
    partial_overlaps += 1 if partial_overlap(range_1, range_2) else 0


print("Total overlaps: " + str(total_overlaps))
print("Partial overlaps: " + str(partial_overlaps))
