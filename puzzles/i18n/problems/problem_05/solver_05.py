"""Internationalization Puzzles - Day 05 - Don't step in it"""


def solver(puzzle_input):
    """
    Count occurrences of poop emoji at specific coordinates based on line numbers.
    Returns total count of poop emojis found at x positions that match (2*y) % width.
    """
    cnt = 0
    width = len(puzzle_input.splitlines()[0])
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == "💩" and x == ((2 * y) % width):
                cnt += 1
    return cnt
