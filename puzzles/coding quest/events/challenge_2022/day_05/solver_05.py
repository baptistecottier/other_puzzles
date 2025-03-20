"""Coding Quest - Challenge 2022 - Day 05 - Spot the forgery"""

from hashlib import sha256


def preprocessing(puzzle_input: str) -> list[list[str, int, str]]:
    """
    Process raw input by splitting records into description, mined number, 
    and hash components.
    """
    records = []
    for record in puzzle_input.splitlines():
        desc, mined_n, _, record_hash = record.split('|')
        records.append([desc, int(mined_n), record_hash])
    return records


def solver(records: list[list[str, int, str]]):
    """
    Computes a final hash by verifying and processing a chain of blockchain-like records.
    
    For each record, validates the hash against the description, mined number, and previous hash.
    If invalid, finds a new mining number that produces a hash starting with six zeros.
    Returns the final hash after processing all records in sequence.
    """
    final_hash = '0' * 64
    for d, n, h in records:
        if sha256(f"{d}|{n}|{final_hash}".encode('utf-8')).hexdigest() != h:
            k = 0
            while True:
                h = sha256(f"{d}|{k}|{final_hash}".encode('utf-8')).hexdigest()
                if h.startswith("000000"):
                    final_hash = h
                    break
                k += 1
        else:
            final_hash = sha256(f"{d}|{n}|{final_hash}".encode('utf-8')).hexdigest()
    yield final_hash
