"""Codyssi - Year 2025 - Day 06 - Lotus Scramble"""


def preprocessing(puzzle_input):
    """
    Convert the puzzle input into a list of characters.
    """
    return list(puzzle_input)


def solver(log_sheet):
    """
    Processes log_sheet by identifying uncorrupted and corrupted entries, then yields the count of
    uncorrupted entries, sum of uncorrupted values, and total sum of all values after applying 
    uncorrupting process.
    """
    values = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    list_uncorrupted = []
    list_corrupted = []
    for i, c in enumerate(log_sheet):
        if c.isalpha():
            list_uncorrupted.append(values.index(c))
        else:
            ind = (2 * values.index(log_sheet[i - 1]) - 5) % 52
            list_corrupted.append(ind)
            log_sheet[i] = values[ind]

    yield len(list_uncorrupted)
    yield sum(list_uncorrupted)
    yield sum(list_uncorrupted) + sum(list_corrupted)
