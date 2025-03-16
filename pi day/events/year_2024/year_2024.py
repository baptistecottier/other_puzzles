"""
Solver for 2024 - Pi Day Coding Quest
"""

def preprocessing(puzzle_input: str) -> str:
    """
    Preprocess the puzzle input by converting it to lowercase.
    """
    return puzzle_input.lower()


def solver(message: str):
    """
    Solves a puzzle by processing a message using Pi digits.
    
    Shifts each character in the message backwards by corresponding Pi digits,
    then calculates a code based on occurrences of digit words in the message.
    
    Args:
        message (str): The input message to process
        
    Yields:
        int: The calculated code value
    """
    alphabet   = "abcdefghijklmnopqrstuvwxyz"
    pi_digits  = list(map(int, "3141592653589793"))
    digits_str = ["two", "three", "four",
                  "five", "six", "seven",
                  "eight", "nine", "ten"]

    for n, c in enumerate(message):
        if c not in " -!',.":
            message += alphabet[(alphabet.index(c) - pi_digits[n % 16]) % 26]

    code = 1
    for i, w in enumerate(digits_str, 2):
        if w in message:
            code *= pow(i, message.count(w))
    yield code
