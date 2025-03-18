"""Codyssi - Year 2025 - Day 02 - Absurd arithmetic"""


def preprocessing(puzzle_input: str) -> tuple[callable, list[int]]:
    """
    Converts the puzzle input string into a list of integers representing costs.
    """
    functions, values = puzzle_input.split('\n\n')
    a, m, p = [int(line.split()[-1]) for line in functions.splitlines()]
    def pricing(x):
        return (x ** p) * m + a
    return pricing, sorted(list(map(int, values.split())), reverse = True)


def solver(pricing: callable, room_qualities: list[int]):
    """
    Calculates room prices based on quality, finding median price, price for sum of
    even qualities, and first affordable room.
    """
    prices = []
    affordable_rq = None
    even_sum = 0
    for rq in room_qualities:
        price = pricing(rq)
        prices.append(price)
        if rq % 2 == 0:
            even_sum += rq
        if price <= 15_000_000_000_000 and affordable_rq is None:
            affordable_rq = rq

    yield prices[len(prices) // 2]
    yield pricing(even_sum)
    yield affordable_rq
