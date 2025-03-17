"""Coding Quest - Practice 2022 - Day 04 - Lost in transmission"""


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """Converts hexadecimal strings from the puzzle input into a list of lists of integers."""
    received_bytes = []
    for line in puzzle_input.splitlines():
        received_bytes.append([int(item, 16) for item in line.split()])
    return received_bytes


def solver(received_bytes: list[list[int]]) -> int:
    """
    Verifies the integrity of a 2D list of bytes using row and column checksums.

    Args:
        received_bytes (list of list of int): 
            A 2D list where each sublist represents a row of 
            bytes. The last element of each row is the row checksum, and the last row 
            contains the column checksums.

    Returns:
        int: 
            The product of the incorrect byte and the difference needed to correct it.
    """
    for y, row in enumerate(received_bytes[:-1]):
        if sum(row[:-1]) % 256 != row[-1]:
            for x, col_cs in enumerate(received_bytes[-1]):
                col_sum = sum(received_bytes[dy][x] for dy in range(len(received_bytes) - 1))
                cs_verif = col_sum - col_cs
                cs_verif %= 256
                if cs_verif != 0:
                    return (received_bytes[y][x] - cs_verif) * received_bytes[y][x]
    return 0
