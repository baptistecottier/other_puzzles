"""Codyssi - Year 2025 - Day 04 - Aeolian Transmissions"""

from itertools import groupby


def solver(lines):
    """
    Solves puzzles by processing lines of text, generating three values: a sum of alphabet indices, 
    a weighted sum of indices with length calculations, and a sum based on character groupings.
    """
    mem = 0
    mem2 = 0
    mem3 = 0
    alpha = '_abcdefghijklmnopqrstuvwxyz'.upper()
    for line in lines.splitlines():
        for k, v in groupby(line):
            mem3 += alpha.index(k) + sum(int(n) for n in str(len(list(v))))
        mem += sum(alpha.index(c) for c in line)
        k = len(line) // 10
        mem2 += sum(alpha.index(c) for c in line[:k] + line[-k:])
        mem2 += sum(int(n) for n in str(len(line) - 2 * k))

    yield mem
    yield mem2
    yield mem3
