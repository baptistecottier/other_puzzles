"""Codyssi - Year 2025 - Day 07 - Siren Disruption"""

import re

def preprocessing(puzzle_input: str) -> list[str]:
    """
    Process the puzzle input into a list of strings, splitting by newlines.
    """
    return puzzle_input.splitlines()


def solver(lines):
    """
    Calculates sum of reduced string lengths based on different regex replacement patterns.
    """
    yield sum(reduced_length(line, r'[\d|-]'                 ) for line in lines)
    yield sum(reduced_length(line, r'(\d\D|\D\d)'            ) for line in lines)
    yield sum(reduced_length(line, r'(\d[a-zA-Z]|[a-zA-Z]\d)') for line in lines)


def reduced_length(string, pattern):
    """
    Returns the length of a string after repeated removal of a given pattern using regular
    expressions.
    """
    while re.search(pattern, string):
        string = re.sub(pattern, '', string)
    return len(string)
