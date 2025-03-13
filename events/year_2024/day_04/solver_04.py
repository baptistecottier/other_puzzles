"""Codyssi - Year 2024 - Day 04 - Traversing the country"""

from collections import defaultdict, deque


def preprocessing(puzzle_input):
    """
    Creates a bidirectional graph from the input, where each node is 
    connected to the nodes specified in the puzzle input.
    """
    routes = defaultdict(set)
    for pair in puzzle_input.splitlines():
        l, r = pair.split(" <-> ")
        routes[l].add(r)
        routes[r].add(l)
    return routes


def solver(routes):
    """
    Analyzes routes by counting destinations, paths with ≤3 steps, and summing
    all shortest paths.
    """
    destinations = routes.keys()
    yield len(destinations)

    distances = []
    for dst in destinations:
        distances.append(shortest_path(routes, dst))

    yield len([d for d in distances if d <= 3])
    yield sum(distances)


def shortest_path(routes, dst):
    """
    Find the shortest path from 'STT' to the destination using BFS.
    
    Args:
        routes (dict): A dictionary mapping locations to lists of adjacent locations.
        dst (str): The destination location.
        
    Returns:
        int or None: The minimum number of steps required to reach the destination,
                    or None if no path exists.
    """
    start = 'STT'
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        location = path[-1]
        if location == dst:
            return len(path) - 1
        for nxt_loc in routes[location]:
            if nxt_loc not in seen:
                queue.append(path + [nxt_loc])
    return None
