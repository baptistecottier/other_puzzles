"""Codyssi - Year 2024 - Day 01 - Handling the Budget"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts the puzzle input string into a list of integers representing costs.
    """
    costs = list(map(int, puzzle_input.splitlines()))
    return costs


def solver(costs: list[int]):
    """
    Solve the budget handling puzzle.
    
    Args:
        costs: List of integers representing costs
        
    Returns:
        Generator yielding three different budget calculations
    """
    yield sum(costs)
    discount = 2 if len(costs) < 10 else 20
    yield sum(sorted(costs)[:-discount])
    yield sum(costs[::2]) - sum(costs[1::2])
