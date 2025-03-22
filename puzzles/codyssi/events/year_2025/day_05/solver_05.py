"""Codyssi - Year 2025 - Day 05 - Patron Islands"""


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Convert string input to a list of (x, y) integer coordinate tuples.
    """
    coordinates = []
    puzzle_input = puzzle_input.replace('(', '').replace(')', '')
    for coordinate in puzzle_input.splitlines():
        x, y = coordinate.split(', ')
        coordinates.append((int(x), int(y)))
    return coordinates


def solver(coordinates: list[tuple[int, int]]):
    """
    Solves a multi-part problem involving Manhattan distances between coordinates, yielding the
    difference between max and min distances, and calculating optimal paths.
    """
    max_distance = max(abs(x) + abs(y) for x, y in coordinates)
    min_distance = min(abs(x) + abs(y) for x, y in coordinates)
    yield max_distance - min_distance

    ax, ay = min(coordinates, key = manhattan_distance)
    coordinates.remove((ax, ay))

    bx, by = min(coordinates, key = lambda x : manhattan_distance(x, (ax, ay)))
    coordinates.remove((bx, by))

    total_distance = manhattan_distance((ax, ay), (bx, by))
    yield total_distance

    while coordinates:
        ax, ay = bx, by
        bx, by = min(coordinates, key = lambda x : manhattan_distance(x, (ax, ay)))
        coordinates.remove((bx, by))
        total_distance += manhattan_distance((ax, ay), (bx, by))
    yield min_distance + total_distance


def manhattan_distance(a, b = (0, 0)):
    """
    Calculate the Manhattan distance between two 2D points, with default b as the origin (0, 0).
    """
    xa, ya = a
    xb, yb = b
    return abs(xb - xa) + abs(yb - ya)
