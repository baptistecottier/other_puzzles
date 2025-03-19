"""Internationalization Puzzles - Day 13 - Gulliver's puzzle dictionary"""

from problems.problem_06 import solver_06


def preprocessing(puzzle_input):
    """
    Preprocess a puzzle by decoding hex-encoded words with various encodings and
    extracting crossword pattern information from the input.
    """
    real_words = []
    raw_words, raw_crossword = puzzle_input.split('\n\n')

    for n, word in enumerate(raw_words.splitlines(), 1):
        word = bytes.fromhex(word)
        for prefix in [b'\xff\xfe', b'\xef\xbb\xbf', b'\xfe\xff']:
            word = word.removeprefix(prefix)
        for encoding in ['utf8', 'latin1', 'utf_16_be', 'utf_16_le']:
            try:
                decoded_word = word.decode(encoding)
                if all(c.isalpha() for c in decoded_word):
                    real_words.append((n, decoded_word))
            except UnicodeDecodeError:
                continue

    keys = set()
    for word in raw_crossword.splitlines():
        word = word.strip()
        i = word.find(next(filter(str.isalpha, word)))
        keys.add((word[i], i, len(word)))
    return real_words, keys


solver = solver_06.solver
