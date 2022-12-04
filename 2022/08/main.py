#!/bin/env python3


filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


grid = []


def reconstruct_grid():
    for row in content:
        clean_row = row.replace('\n', '')
        grid.append([int(c) for c in clean_row])


def count_visible_trees():
    visible_trees = 0
    for j in range(len(grid[0])):
        column = [grid[i][j] for i in range(len(grid))]
        for i in range(len(column)):
            row = grid[i]
            tree = grid[i][j]
            visible_trees += (
                all(t < tree for t in row[:j])
                or all(t < tree for t in row[j+1:])
                or all(t < tree for t in column[:i])
                or all(t < tree for t in column[i+1:])
            )
    return visible_trees


def max_viewing_score():
    max_viewing_score = 0
    for j in range(len(grid[0])):
        column = [grid[i][j] for i in range(len(grid))]
        for i in range(len(column)):
            row = grid[i]
            tree = grid[i][j]
            vs_left = next((d for d in range(1, j) if row[j - d] >= tree), j)
            vs_right = next((d for d in range(1, len(grid[0]) - j) if row[j + d] >= tree), len(grid[0]) - j - 1)
            vs_up = next((d for d in range(1, i) if column[i - d] >= tree), i)
            vs_down = next((d for d in range(1, len(column) - i) if column[i + d] >= tree), len(column) - i - 1)
            max_viewing_score = max(max_viewing_score, vs_left * vs_down * vs_right * vs_up )
    return max_viewing_score


reconstruct_grid()

print("Total visible trees: " + str(count_visible_trees()))
print("Max viewing score: " + str(max_viewing_score()))
