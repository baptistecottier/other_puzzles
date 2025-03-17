"""Coding Quest - Challenge 2022 - Day 02 - Lottery tickets"""


def preprocessing(puzzle_input):
    """
    Converts each line of the input into a list of integers, creating a list of tickets.
    """
    tickets = []
    for ticket in puzzle_input.splitlines():
        tickets.append(list(map(int, ticket.split())))
    return tickets


def solver(tickets):
    """
    Calculate winnings based on matches between tickets and a fixed draw.
    """
    draw = {12, 48, 30, 95, 15, 55, 97}
    winnings = 0
    for ticket in tickets:
        match len([num for num in ticket if num in draw]):
            case 3:
                winnings += 1
            case 4:
                winnings += 10
            case 5:
                winnings += 100
            case 6:
                winnings += 1000
            case _:
                continue
    yield winnings
