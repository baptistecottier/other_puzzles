"""Codyssi - Year 2025 - Day 12 - Challenging the Whirlpool"""

from collections import defaultdict, deque


def preprocessing(puzzle_input: str) -> dict[str, list[tuple[str, int]]]:
    """
    Convert a string of paths into a graph structure of routes with distances.
    """
    routes = defaultdict(list)
    for path in puzzle_input.splitlines():
        places, dist = path.split(' | ')
        dist = int(dist)
        src, dst = places.split(' -> ')
        routes[src].append((dst, dist))
        if dst not in routes:
            routes[dst] = []
    return routes

def solver(routes: dict[str, list[tuple[str, int]]]):
    """
    Computes optimal route metrics, yielding products of top three fewest steps, shortest
    distances, and the longest cycle.
    """
    distances = []
    for dst in routes:
        distances.append(shortest_path(routes, dst))

    fewest_steps = [p for p, _ in sorted(distances)]
    yield fewest_steps[-3] * fewest_steps[-2] * fewest_steps[-1]

    shortest_dist = sorted([d for _, d in distances])
    yield shortest_dist[-3] * shortest_dist[-2] * shortest_dist[-1]

    yield longest_cycle(routes)


def shortest_path(routes: dict[str, list[tuple[str, int]]], dst: str) -> tuple[int, int]:
    """
    Find the shortest path from 'STT' to the destination using BFS.
    """
    start = 'STT'
    min_steps = len(routes)
    min_dist = 10_000
    queue = deque([([start], 0)])
    seen = set([start])
    while queue:
        (path, dist) = queue.popleft()
        if len(path) >= min_steps and dist >= min_dist:
            continue
        location = path[-1]
        if location == dst:
            min_steps = min(len(path) - 1, min_steps)
            min_dist = min(dist, min_dist)
        for nxt_loc, nxt_dist in routes[location]:
            if nxt_loc not in seen:
                queue.append((path + [nxt_loc], dist + nxt_dist))
                seen.add(nxt_loc)
    return (min_steps, min_dist)


def longest_cycle(routes: dict[str, list[tuple[str, int]]]) -> int:
    """
    Find the length of the longest cycle in the graph represented by the routes dictionary.
    """
    max_dist = 0
    for start in routes:
        queue = deque([([start], 0)])
        seen = set()
        while queue:
            (path, dist) = queue.popleft()
            location = path[-1]
            if len(path) > 2 and location == start:
                max_dist = max(dist, max_dist)
            else:
                for nxt_loc, nxt_dist in routes[location]:
                    if nxt_loc not in seen:
                        queue.append((path + [nxt_loc], dist + nxt_dist))
                        seen.add(nxt_loc)
    return max_dist
