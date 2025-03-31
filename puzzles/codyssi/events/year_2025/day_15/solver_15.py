"""Codyssi - Year 2025 - Day 15 - Artifacts at Atlantis"""

from collections import namedtuple

class Tree:
    """A binary tree implementation with value storage and child node expansion capabilities."""
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.value = None

    def expand(self, value):
        """
        Expand the tree by initializing a tree node with a value and create empty left and right
        child nodes.
        """
        self.value = value
        self.right = Tree()
        self.left = Tree()

Artefact = namedtuple('Artefact', ['af_id', 'code'])


def preprocessing(puzzle_input: str):
    """
    Parses the puzzle input into a list of Artefact objects.
    """
    artefacts = []
    for artefact in puzzle_input.replace('\n\n', '\n').splitlines():
        code, af_id = artefact.split(' | ')
        artefacts.append(Artefact(int(af_id), code))
    return artefacts


def solver(artefacts):
    """
    Construct a binary search tree from artefacts, calculating layer sums, and finding common codes
    in paths.
    """
    codes = dict(artefacts)
    tree = Tree()
    tree.expand(artefacts[0].af_id)
    layers = [[artefacts[0].af_id]]
    paths = {}
    for af_id, _ in artefacts[1:-2] + [Artefact(500_000, '_')]:
        if af_id == 500_000:
            yield len(layers) * max(sum(l) for l in layers)
        path = []
        t = tree
        while t.value is not None:
            path.append(codes[t.value])
            if af_id < t.value:
                t = t.right
            else:
                t = t.left
        t.expand(af_id)
        if len(layers) - 1 < len(path):
            layers.append([af_id])
        else:
            layers[len(path)].append(af_id)
        paths[af_id] = path

    yield '-'.join(path)

    path1 = paths[artefacts[-1][0]][::-1]
    path2 = paths[artefacts[-2][0]]
    for code in path1:
        if code in path2:
            yield code
            break
