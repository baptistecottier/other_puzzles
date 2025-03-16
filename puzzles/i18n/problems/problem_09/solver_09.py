"""Internationalization Puzzles - Day 09 - Nine Eleven"""

from collections import defaultdict
from datetime import datetime


def preprocessing(puzzle_input):
    """
    Processes raw puzzle input and organizes date entries by person, returning a defaultdict
    mapping person names to lists of date entries represented as three integers.
    """

    entries = defaultdict(list)
    for line in puzzle_input.splitlines():
        str_date, str_people = line.split(': ')
        people = str_people.split(', ')
        date = list(map(int, str_date.split('-')))
        for p in people:
            entries[p].append(date)
    return entries


def solver(entries):
    """
    Identifies writers who have specified dates matching September 11, 2001 in any valid date
    format.
    
    Args:
        entries (dict): Dictionary mapping writer names to lists of date entries. Each date entry 
                        is a list of three integers representing a date in an unknown format.
    
    Returns:
        str: Space-separated string of sorted writer names who have referenced September 11, 2001.
    """
    writers = []
    formats = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    target = datetime(2001, 9, 11)

    for name, dates in entries.items():
        for a, b, c in formats:
            writer = False
            try:
                for date in dates:
                    if date[a] < 20:
                        year = 2000 + date[a]
                    else:
                        year = 1900 + date[a]
                    writer |= (datetime(year, date[b], date[c]) == target)
            except ValueError:
                continue
            if writer is True:
                writers.append(name)
                break
    return " ".join(sorted(writers))
