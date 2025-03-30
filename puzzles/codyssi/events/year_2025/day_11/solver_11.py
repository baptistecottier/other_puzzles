"""Codyssi - Year 2025 - Day 11 - Games in a Storm!"""

from math import ceil

ALPHABET = (
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "!@#$%^"
        )


def preprocessing(puzzle_input):
    """
    Convert a list of custom base-encoded strings to their integer values.
    """
    integers = []

    for number in puzzle_input.splitlines():
        value, base = number.split()
        base = int(base)
        integer = 0
        for digit in list(value):
            integer = base * integer + ALPHABET.index(digit)
        integers.append(integer)

    return integers


def solver(integers):
    """
    Processes a collection of integers to yield the maximum value, base-68 representation of their
    sum, and smallest base for a 4 digits representation.
    """
    yield max(integers)

    integer = sum(integers)
    smallest_base = ceil(integer ** (1/4))
    base68_representation = ""

    while integer != 0:
        digit = integer % 68
        base68_representation += ALPHABET[digit]
        integer //= 68
    yield base68_representation[::-1]

    yield smallest_base
