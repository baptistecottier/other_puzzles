"""Codyssi - Year 2025 - Day 10 - Cyclops Chaos"""

from collections import deque


def preprocessing(puzzle_input):
    """
    Converts the puzzle input into a 2D grid of integers by parsing each line and splitting numbers
    by spaces.
    """
    grid = [[int(n) for n in line.split(' ')] for line in puzzle_input.splitlines()]
    return grid


def solver(grid):
    """
    Finds the minimum sum of grid lines and calculates the safest path to specified endpoints.
    """
    yield min(sum(line) for line in grid)

    size = len(grid[0]) - 1
    for end in [(14, 14), (size, size)]:
        yield safest_path((0, 0), end, grid)


def safest_path(start, end, grid):
    """
    Finds the path with the lowest danger level from start to end in a grid.
    """
    sx, sy = start
    size = max(end)

    lowest_danger = 18 * sum(end)
    queue = deque([(sx, sy, 0)])
    seen = {(sx, sy): 0}
    while queue:
        path = queue.pop()
        (x, y, danger_level) = path
        if (x, y) == end and danger_level < lowest_danger:
            lowest_danger = danger_level
        else:
            for (tx, ty) in [(x + 1, y), (x, y + 1)]:
                if (tx <= size and ty <= size):
                    if (tx, ty) not in seen or seen[(tx, ty)] > danger_level:
                        queue.appendleft((tx, ty, danger_level + grid[ty][tx]))
                        seen[(tx, ty)] = danger_level

    return lowest_danger + grid[sx][sy]
