"""Codyssi - Year 2025 - Day 14 - Crucial Crafting"""

import dataclasses
import knapsack


@dataclasses.dataclass(unsafe_hash = True)
class Item:
    """
    Represents an item with quality, cost, and material attributes.
    """
    qlty: int
    cost: int
    mtrl: int


def preprocessing(puzzle_input: str) -> list[Item]:
    """
    Parses the puzzle input into a list of Item objects with extracted attributes.
    """
    items = []
    for item in puzzle_input.replace(',', '').splitlines():
        data = item.split()
        items.append(Item(
            int(data[5]),
            int(data[8]),
            int(data[12]),
        ))
    return sorted(items, key = lambda x: (x.qlty, x.cost))


def solver(items: list[Item]):
    """
    Solves a multi-stage optimization problem for items with varying quality, cost, and material
    values using sorting and knapsack algorithms.
    """
    yield sum(c.mtrl for c in items[-5:])

    costs = [c.cost for c in items]
    qltys = [c.qlty for c in items]

    for budget in [30, 150 if len(items) < 50 else 300]:
        qlty, indexes = knapsack.knapsack(costs, qltys).solve(budget)
        _, rv_indexes = knapsack.knapsack(costs[::-1], qltys[::-1]).solve(budget)
        min_mtrl = min(sum(items[i].mtrl for i in indexes),
                       sum(items[-(i + 1)].mtrl for i in rv_indexes))
        yield qlty * min_mtrl
