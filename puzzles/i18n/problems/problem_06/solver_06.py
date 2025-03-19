"""Internationalization Puzzles - Day 06 - Mojibake puzzle dictionnary"""


def preprocessing(puzzle_input):
    """
    Preprocesses the puzzle input by splitting it into words and crossword keys.
    
    The function handles two parts of the puzzle input:
    1. Word list: Some words are encoded in latin1 and need to be decoded to utf8
       - Every 3rd word is decoded
       - Every 5th word is decoded (which means words that are both 3rd and 5th will be decoded
         twice)
    
    2. Crossword clues: Extracts key information from each line of the crossword
       - First alphabetic character of the clue
       - Position of the first alphabetic character
       - Total length of the clue
    
    Args:
        puzzle_input (str): Raw puzzle input containing words section and crossword section
                           separated by a double newline
    
    Returns:
        tuple: (list of processed words, set of crossword key tuples)
              Each key tuple contains (first_char, position, length)
    """
    raw_words, raw_crossword = puzzle_input.split('\n\n')
    words = []
    for n, word in enumerate(raw_words.splitlines(), 1):
        if n % 3 == 0:
            word = word.encode('latin1').decode('utf8')
        if n % 5 == 0:
            word = word.encode('latin1').decode('utf8')
        words.append((n, word))

    keys = set()
    for word in raw_crossword.splitlines():
        word = word.strip()
        i = word.find(next(filter(str.isalpha, word)))
        keys.add((word[i], i, len(word)))
    return words, keys


def solver(words, keys):
    """
    Calculates a score based on specific character matches in words.

    Args:
        words (list): List of words to check against.
        keys (list): List of tuples (c, i, l) where:
            - c (str): Character to match.
            - i (int): Index position to check.
            - l (int): Expected length of words.

    Returns:
        int: Sum of 1-based indices of words that meet all criteria.
    """
    result = 0
    for c, i, l in keys:
        for n, word in words:
            if len(word) != l:
                continue
            if word[i] == c:
                result += n
    return result
