"""Codyssi - Year 2024 - Day 03 - Unformatted Readings!"""

def preprocessing(puzzle_input):
    """
    Process the puzzle input by parsing each line into a reading with string 
    number and integer base.
    """
    readings = []
    for reading in puzzle_input.splitlines():
        n, base = reading.split()
        readings.append([n, int(base)])
    return readings

def solver(readings):
    """
    Solves a problem involving number readings with different bases.

    Args:
        readings: A list of tuples where each tuple contains a number (as a string) 
        and its base (as an integer).

    Yields:
        1. Sum of all the bases
        2. Sum of all the numbers converted to decimal
        3. The sum converted to base-65 representation using a custom character set
    """
    yield sum(base for _, base in readings)
    sum_readings = sum(int(n, base) for n, base in readings)
    yield sum_readings
    converter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#"
    base65_sum = []
    while sum_readings != 0:
        base65_sum.insert(0, converter[sum_readings % 65])
        sum_readings //= 65
    yield "".join(base65_sum)
