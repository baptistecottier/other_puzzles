"""Internationalization Puzzles - Day 12 - Sorting it out"""

from math import prod
from unidecode import unidecode


def preprocessing(puzzle_input: str) -> dict[str, int]:
    """
    Parse the puzzle input into a dictionary of contacts, mapping names to phone numbers.
    """
    contacts = {}
    for contact in puzzle_input.splitlines():
        name, number = contact.split(': ')
        contacts[name.replace("'", '')] = int(number)
    return contacts


def solver(contacts: dict[str, int]):
    """
    Calculate the product of middle numbers for each rule type applied to 
    contacts.
    """
    rules = [trainee_rules, vp_rules, ceo_rules]
    return prod(get_middle_number(contacts, rule) for rule in rules)


def get_middle_number(contacts: dict[str, int], rules: callable):
    """
    Return the value associated with the middle name when the names are sorted 
    by the given rules.
    """
    names = contacts.keys()
    return contacts[sorted(names, key = rules)[len(names) // 2]]


def trainee_rules(name: str) -> str:
    """
    Applying the trainee rules.
    """
    return unidecode(name).lower()


def vp_rules(name: str) -> str:
    """
    Apply Vice President rules. 
    The latin alphabet is extended using 'a', 'b', 'c' as they follow the uppercase
    alphabet in the ASCII table.
    """
    name = name.replace(" ", '')
    name = name.upper()
    name = name.replace('Å', 'a')
    name = name.replace('Æ', 'b')
    name = name.replace('Ä', 'b')
    name = name.replace('Ø', 'c')
    name = name.replace('Ö', 'c')
    return unidecode(name)


def ceo_rules(name: str) -> str:
    """
    Apply the CEO rules.
    """
    for prefix in ["de ", "den ", "der ", "van "]:
        name = name.replace(prefix, '')
    return unidecode(name).lower()
