#!/bin/env python3

import os

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3

LOST_ROUND_POINTS = 0
DRAW_ROUND_POINTS = 3
WON_ROUND_POINTS = 6

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

MOVE_ROCK = MOVE_LOOSE = 'X'
MOVE_PAPER = MOVE_DRAW = 'Y'
MOVE_SCISSORS = MOVE_WIN = 'Z'

def decrypt1(round):
    return round.replace('\n', '').replace(MOVE_ROCK, ROCK).replace(MOVE_PAPER, PAPER).replace(MOVE_SCISSORS, SCISSORS).split(' ')


def decrypt2(round):
    strategy = round.replace('\n', '').split(' ')

    our_move = None
    if strategy[1] == MOVE_LOOSE:
        our_move = SCISSORS if strategy[0] == ROCK else ROCK if strategy[0] == PAPER else PAPER
    elif strategy[1] == MOVE_DRAW:
        our_move = strategy[0]
    else:
        our_move = PAPER if strategy[0] == ROCK else SCISSORS if strategy[0] == PAPER else ROCK

    return [strategy[0], our_move]


def round_points(opponent, we):
    points = ROCK_POINTS if we == ROCK else PAPER_POINTS if we == PAPER else SCISSORS_POINTS

    if opponent == we:
        points += DRAW_ROUND_POINTS
    elif (opponent == ROCK and we == PAPER) or (opponent == PAPER and we == SCISSORS) or (opponent == SCISSORS and we == ROCK):
        points += WON_ROUND_POINTS

    return points


total_points_strategy_1 = 0
total_points_strategy_2 = 0

for round in content:
    strategy_1 = decrypt1(round)
    strategy_2 = decrypt2(round)
    total_points_strategy_1 += round_points(strategy_1[0], strategy_1[1])
    total_points_strategy_2 += round_points(strategy_2[0], strategy_2[1])


print("Total points strategy 1: " + str(total_points_strategy_1))
print("Total points strategy 2: " + str(total_points_strategy_2))
