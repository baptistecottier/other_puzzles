"""Codyssi - Year 2025 - Day 09 - Windy Bargain"""

from copy import deepcopy


class Balance:
    """
    Class representing a financial balance with money and debts.
    """
    money: int
    debts: list[tuple[str, int]]

    def __init__(self, amount):
        self.money = amount
        self.debts = []


def preprocessing(puzzle_input: str):
    """
    Parses the puzzle input into balances and transactions.
    """
    balances = {}
    transactions = []
    raw_balances, raw_transactions = puzzle_input.split("\n\n")

    for balance in raw_balances.splitlines():
        name, amount = balance.split(' HAS ')
        balances[name] = Balance(int(amount))

    for transaction in raw_transactions.splitlines():
        words = transaction.split()
        transactions.append((words[1], words[3], int(words[5])))

    return balances, transactions


def solver(balances, transactions):
    """
    Processes financial transactions at different debt levels, yielding results for each level.
    """
    for debt_level in range(3):
        yield proceed_transactions(transactions, deepcopy(balances), debt_level)


def proceed_transactions(transactions, balances, debt_level):
    """
    Process multiple financial transactions, handle debt based on debt level, and return the sum of
    the three highest balances.
    """
    for src, dst, qty in transactions:
        paid = qty

        if debt_level > 0 and qty > balances[src].money:
            paid = balances[src].money
            balances[src].debts.insert(0, (dst, qty - paid))
        balances[src].money -= paid
        balances[dst].money += paid

        if debt_level == 2:
            adjust_debts(dst, balances)

    return sum(sorted([b.money for b in balances.values()])[-3:])


def adjust_debts(dst, balances):
    """
    Recursively settles financial debts by adjusting balances and processing debt chains.
    """
    while balances[dst].money > 0 and balances[dst].debts != []:
        debt_dst, debt_qty = balances[dst].debts.pop()

        if debt_qty <= balances[dst].money:
            balances[debt_dst].money += debt_qty
            balances[dst].money -= debt_qty

        else:
            debt_qty -= balances[dst].money
            balances[debt_dst].money += balances[dst].money
            balances[dst].money = 0
            balances[dst].debts.append((debt_dst, debt_qty))

        adjust_debts(debt_dst, balances)
