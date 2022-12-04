#!/bin/env python3

import os

with open('input', 'r') as f:
    content = f.readlines()


CHAMBER_WIDTH = 7
LEFT_MARGIN = 2
BOTTOM_MARGIN = 3
ROCK_TYPES = [[['@'] * 4], [['.', '@', '.'], ['@', '@', '@'], ['.', '@', '.']], ['..@'.split(), '..@'.split(), '@@@'.split()], [('@' * 2).split()] * 2]
MOVING_ROCK = '@'
STOPPED_ROCK = '#'

def get_moves():
    return content[0].strip()


def draw_chamber(chamber):
    #os.system('clear')
    print('+-------+')
    for r in chamber:
        row = '|'
        for c in r:
            row += c 
        row += '|'
        print(row)


moves = get_moves()
chamber = [['.'] * 7] * 4
#print(chamber)

current_rock = -1
current_height = 0
for move in moves[0:1]:
    # Pick the rock
    current_rock = (current_rock + 1) % 4
    rock = ROCK_TYPES[current_rock]
    #print(rock)

    # Insert the rock
    if current_height + BOTTOM_MARGIN + len(rock) > len(chamber):
        chamber.append((['.'] * 7) * (len(chamber) - current_height - BOTTOM_MARGIN - len(rock)))

    for i in range(current_height + BOTTOM_MARGIN, current_height + BOTTOM_MARGIN + len(rock)):
        for j in range(LEFT_MARGIN, LEFT_MARGIN + len(rock[0])):
            #print(i,j)
            chamber[i][j] = rock[i - BOTTOM_MARGIN - current_height][j - LEFT_MARGIN]
            print(rock[i - BOTTOM_MARGIN - current_height][j - LEFT_MARGIN])
            draw_chamber(chamber)
    
    current_height =+ len(rock)

    #print(chamber)

    #draw_chamber(chamber)