"""
Solver for 2025 - Pi Day Coding Quest
"""

from decimal import Decimal


def solver(puzzle_input):
    """
    Solves a puzzle that works with Pi digits, an alphabet cipher, and ticker data.

    The function processes a puzzle input with stock ticker data, applies a cipher based on Pi
    digits, and performs math operations on prices based on even/odd days. It returns a code 
    derived from mathematical operations and a phrase constructed from cipher mapping.

    Args:
        puzzle_input (str): A multi-line string with ticker data in format "day price ticker"

    Returns:
        tuple: A 2-element tuple containing:
            - str: 10-digit code derived from price calculations
            - str: Deciphered phrase from the sorted ticker data
    """
    pi_digits  = "31415926535897932384626433832795"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_map = ("X J P Z Q T M C A O W Y B G D A "
                  "N F R S H V K U E X J P Z Q T M "
                  "C L O W Y B G D A N F R S H V K "
                  "G E X J P Z Q T M P L O W Y B G "
                  "D A N F R S H V K U E X J P Z Q "
                  "T M A L O W Y B G D A O F I S H "
                  "A K U E X J P Z Q T M C L O W Y "
                  "O G D A N F R S H V K U E X J P "
                  "Y Q T M C L O W Y B G D A N F R "
                  "S H V K U E X Y G Z Q T M C L O "
                  "D Y B G D A N F R S H V K U D X "
                  "J P Z Q T M C L O W Y B G D A N "
                  "F R S H V K U E X J P Z Q T M C "
                  "D O W Y B G D A N F R S H V K U "
                  "E X J P Z Q T M C O O W Y B G D "
                  "A N F R S H V K U E X J P Z Q T ")
    cipher_map = cipher_map.split()

    code = None

    prices = {}
    tickers = {}
    phrase = []

    for line in puzzle_input.splitlines()[1:]:
        day, price, ticker = line.split()
        tickers[ticker] = int(day)
        prices[ticker] = int(price.replace('.',''))

    for line in puzzle_input.splitlines()[1:]:
        day, price, ticker = line.split()
        shift = price.replace('.', '')
        if shift in pi_digits:
            if code is None:
                code = Decimal(price)
            elif int(day) % 2 == 0:
                code *= Decimal(price)
            else:
                code /= Decimal(price)

            updated_ticker = ""
            for letter in ticker:
                updated_ticker += alphabet[(alphabet.index(letter) + int(shift)) % 26]
            phrase.append((
                tickers[updated_ticker],
                prices[updated_ticker],)
                )
    return (
        str(code).strip('0').replace('.', '')[:10],
        "".join(cipher_map[price % 256] for _, price in sorted(phrase)),
    )
