"""Internationalization Puzzles - Day 03 - Unicode passwords"""


def solver(passwords: str):
    """
    Counts the number of valid passwords in a given string of passwords.

    Args:
        passwords (str): Multi-line string containing passwords to validate

    Returns:
        int: Number of valid passwords
    """
    good_passwords = 0
    for password in passwords.splitlines():
        if is_password_good(password):
            good_passwords += 1
    return good_passwords


def is_password_good(password: str) -> bool:
    """
    Check if a password meets the security requirements:
        - Length is between 4 and 12 characters (inclusive)
        - Contains at least one digit
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one character with ASCII value greater than 128

    Args:
        password (str): The password to check

    Returns:
        bool: True if the password meets all requirements, False otherwise
    """
    return (4 <= len(password) <= 12
            and any(c.isdigit() for c in password)
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(ord(c) > 128 for c in password))
