"""Codyssi - Year 2025 - Day 03 - Supplies in Surplus"""


def preprocessing(puzzle_input: str) -> list[set]:
    """
    Convert a string of number ranges into a list of sets.

    Each range in the input string is formatted as 'start-end', and is converted
    into a set of integers from start to end (inclusive).
    """
    ranges = []
    for str_range in puzzle_input.split():
        start, end = str_range.split('-')
        ranges.append(set(range(int(start), int(end) + 1)))
    return ranges


def solver(ranges: list[set]):
    """
    Solver function for event day 3.
    Processes ranges by merging them and yields the number of boxes at different stages:
    1. Total count of all boxes in the initial ranges.
    2. Total count after merging adjacent pairs of ranges.
    3. Maximum count in any single range after merging adjacent ranges again.
    """
    n_boxes = sum(len(r) for r in ranges)
    yield n_boxes

    ranges = [ranges[i].union(ranges[i + 1]) for i in range(0, len(ranges), 2)]
    n_boxes = sum(len(r) for r in ranges)
    yield n_boxes

    ranges = [ranges[i].union(ranges[i + 1]) for i in range(len(ranges) - 1)]
    n_boxes = max(len(r) for r in ranges)
    yield n_boxes
