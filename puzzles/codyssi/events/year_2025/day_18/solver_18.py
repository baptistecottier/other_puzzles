"""Codyssi - Year 2025 - Day 18 - Cataclysmic Escape"""

from collections import deque
from dataclasses import dataclass
from itertools   import product


@dataclass(unsafe_hash = True)
class Coord:
    """
    Represents a position in 4D space (x, y, z, a) with boundary validation.
    """
    x: int
    y: int
    z: int
    a: int

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.a])


@dataclass(unsafe_hash = True)
class Eq:
    """
    A class representing a modular linear equation in four variables.
    The equation has the form: (x*self.x + y*self.y + z*self.z + a*self.a) % self.p == self.r
    """
    coeffs: Coord
    p: int
    r: int
    v: tuple[int, int, int, int]

    def evaluate(self, coord):
        """
        Evaluates if the given parameters satisfy the linear congruence relation.
        """
        return sum(p * c for p, c in zip(self.coeffs, coord)) % self.p == self.r


@dataclass
class Debri:
    """
    A class representing a debris particle in a 3D grid with an additional attribute.
    """
    pos: Coord
    vel: Coord
    def __init__(self, pos, vel):
        self.pos = Coord(*pos)
        self.vel = Coord(*vel)

    def move(self, n = 1):
        """
        Calculates new position after n seconds, applying modular bounds.
        """
        return (
            (self.pos.x + n * self.vel.x) % 10,
            (self.pos.y + n * self.vel.y) % 15,
            (self.pos.z + n * self.vel.z) % 60,
            (self.pos.a + n * self.vel.a + 1) % 3 - 1)


def preprocessing(puzzle_input):
    """
    Parses puzzle input into a list of equation objects.
    """
    equations = []
    for line in puzzle_input.splitlines():
        data = line.split(' ', 11)
        equation = data[2]
        coeffs = [int(item[:-1]) for item in equation.split('+')]
        quotient = int(data[4])
        remainder = int(data[7])
        velocity = tuple(int(item) for item in data[-1][1:-1].split(', '))
        equations.append(Eq(Coord(*coeffs), quotient, remainder, velocity))
    return equations


def solver(equations):
    """
    Navigates a submarine through 3D space with moving debris.

    Args:
        equations: List of equations defining debris movements.

    Yields:
        int: First the total number of debris pieces.
        int: Then the shortest time to reach destination (9,14,59) avoiding debris.
    """
    debris = []
    space = product(range(9 + 1), range(14 + 1), range(59 + 1), [-1, 0, 1])
    for dot, eq in product(space, equations):
        if eq.evaluate(dot):
            debris.append(Debri(dot, eq.v))
    yield len(debris)

    obstacles = {0: {d.pos for d in debris}}
    queue = deque([(0, 0, 0, 0, 0, 0)])
    seen = {(0, 0, 0, 0, 0, 0)}
    neighbours = [(0, 0, 0),
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)]

    lowest_duration = None
    while queue:
        submarine = queue.popleft()
        (x, y, z, a, seconds, hits) = submarine
        if seconds not in obstacles:
            obstacles[seconds] = {d.move(seconds) for d in debris}

        if (x, y, z, a) != (0, 0, 0, 0) and (x, y, z, a) in obstacles[seconds]:
            if lowest_duration is not None or hits >= 3:
                continue
            hits += 1

        if (x, y, z, a) == (9, 14, 59, 0):
            if lowest_duration is None:
                lowest_duration = seconds
                queue = deque(
                    {(x, y, z, a, s, h) for (x, y, z, a, s, h) in queue if h == 0}
                              )
            if hits == 0:
                yield seconds
                break

        for (dx, dy, dz) in neighbours:
            tx, ty, tz = x + dx, y + dy, z + dz
            if (in_space(tx, ty, tz, a) and
                        (tx, ty, tz, a, seconds + 1, hits) not in seen):
                queue.append((tx, ty, tz, a, seconds + 1, hits))
                seen.add(((tx, ty, tz, a, seconds + 1, hits)))
    yield lowest_duration


def in_space(x, y, z, a):
    """
    Check if point (x, y, z, a) is within defined space boundaries.
    """
    return all((
        0 <= x <= 9,
        0 <= y <= 14,
        0 <= z <= 59,
        -1 <= a <= 1))
