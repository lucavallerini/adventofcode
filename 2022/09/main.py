#!/bin/env python3


filename = 'input'
with open(filename, 'r') as f:
    content = f.readlines()


sign = lambda x: 0 if x == 0 else 1 if x > 0 else - 1


def move_head(head, direction, amount):
    if direction == 'R':
        head = (head[0] + amount, head[1])
    elif direction == 'L':
        head = (head[0] - amount, head[1])
    elif direction == 'U':
        head = (head[0], head[1] - amount)
    elif direction == 'D':
        head = (head[0], head[1] + amount)
    return head


def move_tail(tail, head):
    x_delta = tail[0] - head[0]
    y_delta = tail[1] - head[1]
    if abs(x_delta) > 1 or abs(y_delta) > 1:
        tail = (tail[0] - sign(x_delta), tail[1] - sign(y_delta))
    return tail


def process(number_of_knots):
    knots = [(0, 0)] * number_of_knots
    visited = set()

    # Starting position is visited
    visited.add(knots[-1])

    # Now cycle all moves
    for move in content:
        for s in range(int(move[1:])):
            knots[0] = move_head(knots[0], move[0], 1)
            for k in range(1, len(knots)):
                knots[k] = move_tail(knots[k], knots[k-1])
            visited.add(knots[-1])

    return len(visited)


print("Visited cells (2 knots):", process(2))
print("Visited cells (10 knots):", process(10))
