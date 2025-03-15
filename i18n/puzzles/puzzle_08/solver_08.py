"""Internationalization Puzzles - Day 08 - Unicode passwords redux"""

from unidecode import unidecode


def preprocessing(puzzle_input):
    """Preprocess puzzle input by lowercasing and removing accents from each line."""
    passwords = []
    for pw in puzzle_input.splitlines():
        passwords.append(unidecode(pw).lower())
    return passwords


def solver(passwords):
    """
    Count valid passwords based on criteria: 
        4-12 chars length, has digit, vowel, consonant, and no repeated characters.
    Args:
        passwords (list): Passwords to validate
    Returns:
        int: Valid password count
    """
    cnt = 0
    vowels = (
        'a', 'e', 'i', 'o', 'u',
        )
    consonants = (
        'b', 'c', 'd', 'f', 'g', 'h', 'j',
        'k', 'l', 'm', 'n', 'p', 'q', 'r',
        's', 't', 'v', 'w', 'x', 'y', 'z',
        )

    for pw in passwords:
        if all((
            4 <= len(pw) <= 12,
            any(c.isdigit() for c in pw),
            any(c in vowels for c in pw),
            any(c in consonants for c in pw),
            all(pw.count(c) == 1 for c in pw),
        )):
            cnt += 1
    return cnt
