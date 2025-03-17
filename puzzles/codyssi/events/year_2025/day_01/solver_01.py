"""Codyssi - Year 2025 - Day 01 - Compass Calibration"""


def preprocessing(puzzle_input: str) -> tuple[list[int], list[str]]:
    """
    Converts the puzzle input string into a list of integers representing costs.
    """
    values = list(map(int, puzzle_input.split()[:-1]))
    signs = puzzle_input.splitlines()[-1]
    return values, signs


def solver(values: list[int], signs: list[str]):
    """
    Solves a problem by computing different offsets based on input values and signs.

    Args:
        values (list[int]): A list of integers to process.
        signs (list[str]): A list of operation signs to apply.

    Yields:
        int: The computed offset for the original values and signs.
        int: The computed offset for the original values and reversed signs.
        int: The computed offset for corrected values (where pairs of adjacent values are combined)
             and reversed signs.
    """
    yield compute_offset(values, signs)
    yield compute_offset(values, signs[::-1])
    corrected_values = []
    while values:
        corrected_values.append(values.pop(0) * 10 + values.pop(0))
    yield compute_offset(corrected_values, signs[::-1])


def compute_offset(values, signs):
    """
    Calculate the offset by applying a series of additions and subtractions.
    """
    delta = values[0]
    for s, v in zip(signs, values[1:]):
        if s == '-':
            delta -= v
        else:
            delta += v
    return delta
