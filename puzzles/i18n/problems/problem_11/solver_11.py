"""Internationalization Puzzles - Day 11 - Homer's cipher"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Preprocess puzzle input by replacing Greek final sigma (ς) with regular sigma (σ)
    and keeping only Greek letters (Unicode range 913-969).

    Args:
        puzzle_input: A string containing multiple lines of text with Greek characters.

    Returns:
        A list of strings, where each string is a line from the input with only Greek letters.
    """
    sentences = []
    for sentence in puzzle_input.splitlines():
        sentence = sentence.replace('ς', 'σ')
        sentence = ''.join(c for c in sentence if 913 <= ord(c) <= 969)
        sentences.append(sentence)
    return sentences


def solver(sentences: list[str]):
    """
    Finds the number of shifts needed to reveal Odysseus' name in Greek in given sentences.
    
    Applies Homer unshifting repeatedly until finding any Greek variant of Odysseus' name.
    Then sums all the shifts needed for each sentence.
    """
    variants = ['Οδυσσευσ', 'Οδυσσεα', 'Οδυσσει', 'Οδυσσεωσ', 'Οδυσσευ']

    sum_shifts = 0
    for sentence in sentences:
        for shift in range(1, 25):
            sentence = homer_unshift(sentence)
            if any(variant in sentence for variant in variants):
                sum_shifts += shift
                break
    return sum_shifts


def homer_unshift(sentence: str) -> str:
    """
    Performs a Caesar shift decryption (right shift by 1) on Greek letters in a sentence.

    This function converts each Greek letter to the next one in the alphabet, while
    keeping non-Greek characters unchanged. For example, Α becomes Β, Β becomes Γ, etc.
    ω wraps around to α.
    """
    lower = "αβγδεζηθικλμνξοπρστυφχψωα"
    unshift = dict(zip(lower[:-1], lower[1:]))

    upper = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΑ"
    unshift.update(dict(zip(upper[:-1], upper[1:])))

    return ''.join(unshift[c] for c in sentence)
