"""Codyssi - Year 2025 - Day 16 - Artifacts at Atlantis"""

from itertools import product
import math

class Dice:
    """
    A 6-sided dice simulator with grid-based faces that can be twisted and scored in various ways.
    """
    front: int
    below: int
    right: int
    size: int
    faces: list
    wrapped: list

    def __init__(self, size):
        self.front = 2
        self.below = 0
        self.right = 1
        self.size = size
        self.faces = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(6)]
        self.wrapped = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(6)]

    def twist(self, direction):
        """
        Returns new coordinates after twisting the cube in the specified direction.
        """
        match direction:
            case 'L':
                self.front, self.right = self.right, 5 - self.front
            case 'R':
                self.front, self.right = 5 - self.right, self.front
            case 'U':
                self.front, self.below = self.below, 5 - self.front
            case 'D':
                self.front, self.below = 5 - self.below, self.front

    def apply_modulo(self):
        """
        Apply modulo 100 to all values in faces and wrapped lists.
        """
        self.faces = [[[d % 100 for d in row] for row in face] for face in self.faces]
        self.wrapped = [[[d % 100 for d in row] for row in face] for face in self.wrapped]

    def adjust_instruction(self, axis, index):
        """
        Adjust an instruction based on current dice face orientation.
        """
        if self.orientation in 'LR':
            axis = 1 - axis

        if self.orientation == 'D' or axis == 'RLDU'.index(self.orientation):
            index = self.size - 1 - index

        return (axis, index)

    @property
    def unwrapped_dominance_score(self):
        """
        Calculate the dominance score as the product of the maximum row or column sum for each
        face.
        """
        return math.prod(self.size + max(sum(f) for f in face + list(zip(*face)))
                    for face in self.faces)

    @property
    def wrapped_dominance_score(self):
        """
        Calculate the dominance score as the product of the maximum row or column sum for each
        face.
        """
        faces = [[[(ff + ww) % 100
                    for ff, ww in zip(f, w)]
                        for f, w in zip(face, wrap)]
                            for face, wrap in zip(self.faces, self.wrapped)]

        return math.prod(self.size + max(sum(f) for f in face + list(zip(*face)))
                        for face in faces)

    @property
    def orientation(self):
        """
        Determines the dice orientation ('U', 'D', 'L', 'R') based on the current below and front
        face values.
        """
        if self.below == 3 or ((self.front, self.below) in [(2, 0), (3, 5)]):
            return 'U'
        if self.below == 2 or ((self.front, self.below) in [(2, 5), (3, 0)]):
            return 'D'
        if (self.front, self.below) in [(0, 1), (1, 5), (2, 1), (3, 1), (4, 0), (5, 4)]:
            return 'L'
        return 'R'


def preprocessing(puzzle_input):
    """
    Parse puzzle input into structured instructions and twists.
    """
    instructions = []
    raw_instructions, twists = puzzle_input.split('\n\n')

    for instruction in raw_instructions.splitlines():
        data = instruction.rsplit(' ', 3)
        target = data[0]
        number = int(data[-1])
        if target == 'FACE':
            instructions.append((-1, None, number))
        elif 'COL' in target:
            instructions.append((0, int(target[4:]) - 1, number))
        else:
            instructions.append((1, int(target[4:]) - 1, number))

    return instructions, list(twists)


def solver(instructions: list[tuple[int, int | None, int]], twists: str):
    """
    Processes dice instructions and twists, yielding applied instruction results and dominance
    scores.
    """
    size = 3 if len(twists) < 10 else 80
    dice = Dice(size)

    yield apply_instructions(dice, instructions, twists)
    yield dice.unwrapped_dominance_score
    yield dice.wrapped_dominance_score


def apply_instructions(dice, instructions, twists):
    """
    Applies a sequence of instructions to a dice and returns absorption score.
    """
    absorption_score = [0 for _ in range(6)]

    while instructions:
        axis, index, number = instructions.pop(0)
        absorption_score[dice.front] += number * dice.size * (dice.size if index is None else 1)

        if axis == -1:
            for x, y in product(range(dice.size), repeat = 2):
                dice.faces[dice.front][y][x] += number

        else:
            faces = dice.faces
            for _ in range(4):
                t_axis, t_index = dice.adjust_instruction(axis, index)

                if t_axis == 1:
                    faces[dice.front][t_index] = [d + number for d in faces[dice.front][t_index]]

                else:
                    for y in range(dice.size):
                        faces[dice.front][y][t_index] += number

                dice.twist('L' if axis == 1 else 'D')
                faces = dice.wrapped

        if twists:
            dice.twist(twists.pop(0))

    absorption_score.sort()
    dice.apply_modulo()

    return absorption_score[-1] * absorption_score[-2]
