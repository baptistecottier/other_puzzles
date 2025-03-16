"""Internationalization Puzzles - Day 10 - Unicode passwords strike back!"""

from unicodedata import normalize
from itertools import product
from bcrypt import checkpw


def preprocessing(puzzle_input: str) -> tuple[dict, list]:
    """
    Pre-processes the puzzle input by separating the database and attempts information.

    Args:
        puzzle_input (str): The raw puzzle input consisting of a database section 
                            and a attempts section separated by a blank line.

    Returns:
        tuple: A tuple containing:
            - hashes (dict): A dictionary mapping attemptss to emails.
            - attempts (list): A list of attempts attempts, where each attempt is a list of strings.
    """
    hashes = {}
    db, attempts = puzzle_input.split('\n\n')
    for d in db.splitlines():
        user, digest = d.split(' ')
        hashes[user] = digest
    attempts = [attempt.split(' ') for attempt in attempts.splitlines()]
    return hashes, attempts


def solver(hashes: dict[str, str], attempts: list[list[str]]):
    """
    Evaluates login attempts and returns the number of successful attempts.

    This function compares login attempts against stored password hashes using bcrypt.
    It keeps track of successfully authenticated users to avoid rehashing for repeat attempts.

    Args:
        hashes (dict): Mapping of usernames to their password hashes.
        attempts (list): List of tuples containing (username, password_attempt).

    Returns:
        int: The number of successful login attempts.
    """
    score = 0
    passwords = {}
    for user, attempt in attempts:
        if user in passwords:
            if normalize('NFC', attempt) == passwords[user]:
                score += 1
                continue
        for pw in possible_passwords(normalize('NFC', attempt)):
            if checkpw(pw.encode('utf-8'), hashes[user].encode('utf-8')) is True:
                passwords[user] = normalize('NFC',pw)
                score += 1
                break
    return score


def possible_passwords(normalized_pw: str) -> list[str]:
    """
    Generate all possible password combinations by considering normalized and unnormalized
    versions of non-ASCII characters.
    """
    candidates = [{normalize('NFD', c), c} if not c.isascii() else {c} for c in normalized_pw]
    return [''.join(letters) for letters in product(*candidates)]
