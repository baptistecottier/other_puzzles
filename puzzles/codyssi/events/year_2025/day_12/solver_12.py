"""Codyssi - Year 2025 - Day 12 - Challenging the Whirlpool"""

from operator import add, sub, mul
from copy import deepcopy


def preprocessing(puzzle_input: str):
    """
    Parse puzzle input into grid of integers, instruction list, and flow control statements.
    """
    grid, instructions, flow_control = [block.splitlines() for block in puzzle_input.split('\n\n')]
    grid = [[int(n) for n in line.split()] for line in grid]
    instructions = [instruction.split(' ', 1) for instruction in instructions]
    flow_control = flow_control[1::2]
    return grid, instructions, flow_control


def solver(grid, instructions, flow_control):
    """
    Generator that yields the maximum sum after applying instructions to grid with different flow
    control configurations.
    """
    n = 1 + len(instructions) // flow_control.count('ACT')
    for fc in [['ACT'] * len(instructions), flow_control, n * flow_control]:
        yield max_sum_after_instructions(
                deepcopy(grid),
                deepcopy(instructions),
                fc)


def max_sum_after_instructions(grid, instructions, flow_control):
    """
    Apply a series of SHIFT and arithmetic operations to the grid based on given instructions.
    """
    str_to_op = {
        'ADD': add, 
        'SUB': sub,
        'MULTIPLY': mul,
    }

    while instructions and flow_control:
        op, args = instructions.pop(0)
        action = flow_control. pop(0)
        if action == 'CYCLE':
            instructions.append((op, args))
            continue
        args = args.split(' ')
        if op == 'SHIFT':
            grid = shift(grid, args[0], int(args[1]) - 1, int(args[3]))
        else:
            axis_number = int(args[-1]) - 1 if len(args) > 2 else -1
            grid = arithmetic(grid, str_to_op[op], args[1], axis_number, int(args[0]))

    return max(sum(g) for g in grid + list(zip(*grid)))


def shift(grid, axis, axis_number, amount):
    """
    Shifts elements in a row or column of a 2D grid by a specified amount, with elements that move
    off the edge wrapping around to the other side.
    """
    dim = len(grid[0])
    if axis == 'COL':
        temp = [grid[y][axis_number] for y in range(dim)]
        for y in range(dim):
            grid[y][axis_number] = temp[y - amount]
    else:
        grid[axis_number] = grid[axis_number][-amount:] + grid[axis_number][:-amount]
    return grid


def arithmetic(grid, op, axis, axis_number, amount):
    """
    Applies an arithmetic operation to specified elements in a grid and returns the modified grid
    with values modulo 2^30.
    """
    dim = len(grid[0])
    mod = 1 << 30
    match axis:
        case 'ALL':
            grid = [[op(n, amount) % mod for n in line] for line in grid]
        case 'ROW':
            grid[axis_number] = [op(n, amount) % mod for n in grid[axis_number]]
        case 'COL':
            for y in range(dim):
                grid[y][axis_number] = op(grid[y][axis_number], amount) % mod
        case _:
            raise ValueError("Axis has to be 'ALL', 'ROW', or 'COL'")
    return grid
