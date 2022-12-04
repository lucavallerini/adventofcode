#!/bin/env python3

import re

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


# Find first blanck line: this will separate the input cargo stacks and stacking procedure
separator_index = content.index('\n')

# Create the cargo stacks
number_of_cargos = len(re.findall("[0-9]", content[separator_index - 1]))
cargos = []

# Initialize stacks
def init_cargos():
    cargos.clear()
    for i in range(0, number_of_cargos):
        cargos.insert(i, [])

    for i in range(separator_index - 2, -1, -1):
        stacks = re.findall("(\[[A-Z]\][ \n])|([ ]{3}[\n]*)", content[i])
        for j in range(0, len(stacks)):
            box = stacks[j]
            if len(box[0]) > 0:
                cargos[j].append(box[0].replace('\n', '').replace(' ', ''))


# Perform procedure: read instructions and move boxes around
def crate_mover_9000():
    # move x (items) from y to z (1-indexed), ONE AT A TIME
    for i in range(separator_index + 1, len(content)):
        move = [ int(x) for x in re.findall("[0-9]+", content[i]) ]
        for o in range(0, move[0]):
            cargos[move[2] - 1].append(cargos[move[1] - 1].pop(len(cargos[move[1] - 1]) - 1))


def crate_mover_9001():
    # move x (items) from y to z (1-indexed), ALL AT ONCE
    for i in range(separator_index + 1, len(content)):
        move = [ int(x) for x in re.findall("[0-9]+", content[i]) ]
        cargos[move[1] - 1].reverse() # reverse the cargo
        boxes = cargos[move[1] - 1][0:move[0]] # keep elements to move
        boxes.reverse() # restore original order
        cargos[move[1] - 1] = cargos[move[1] - 1][move[0]:] # elements to keep
        cargos[move[1] - 1].reverse() # restore original order
        cargos[move[2] - 1].extend(boxes)


# Find the top of the stacks
def find_top_boxes():
    top = ""
    for i in range(0, len(cargos)):
        top += cargos[i][-1][1]
    return top


init_cargos()
crate_mover_9000()
print("Top of the stacks (CrateMover9000): " + find_top_boxes())

init_cargos()
crate_mover_9001()
print("Top of the stacks (CrateMover9001): " + find_top_boxes())
