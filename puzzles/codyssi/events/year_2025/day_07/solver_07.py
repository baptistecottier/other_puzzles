"""Codyssi - Year 2025 - Day 07 - Siren Disruption"""

from itertools import pairwise


def preprocessing(puzzle_input: str):
    """
    Preprocesses the puzzle input by parsing frequencies, swaps, and test index.
    """
    puzzle_input = puzzle_input.replace('-', '\n')
    frequencies, swaps, test_index = puzzle_input.split('\n\n')
    frequencies = list(map(int, frequencies.splitlines()))
    swaps = list(map(lambda x: int(x) - 1, swaps.splitlines()))
    test_index = int(test_index) - 1
    return frequencies, swaps + [swaps[0]], test_index


def solver(frequencies: list[int], swaps: list[int], test_index: int):
    """
    Generates the frequency at the test index after performing swaps of different sizes on the
    given frequencies.
    """
    for size in [2, 3]:
        yield swap_frequencies(frequencies.copy(), swaps, size)[test_index]
    yield swap_block_frequencies(frequencies, swaps)[test_index]


def swap_frequencies(frequencies, swaps, size):
    """
    Swaps the values in the frequencies list according to the given swaps list in chunks of the
    specified size.
    """
    for i in [swaps[k: k + size] for k in range(0, len(swaps), 2)]:
        temp = frequencies[i[-1]]
        for src, dst in pairwise(i[::-1]):
            frequencies[src] = frequencies[dst]
        frequencies[i[0]] = temp
    return frequencies


def swap_block_frequencies(frequencies, swaps):
    """
    Swaps two block from given frequencies and swaps starting positions. Swaps stop when the first
    block overlaps the second one or if the second one reaches the end of the list of the 
    frequencies
    """
    l = len(frequencies)
    for a, b in [swaps[k: k + 2] for k in range(0, len(swaps) - 1, 2)]:
        a, b = min(a, b), max(a, b)
        ta, tb = a, b
        while ta < b and tb < l:
            frequencies[tb], frequencies[ta] = frequencies[ta], frequencies[tb]
            ta += 1
            tb += 1
    return frequencies
