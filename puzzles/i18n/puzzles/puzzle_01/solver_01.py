"""Internationalization Puzzles - Day 01 - Length limits on messaging platforms"""


def solver(messages):
    """
    Calculates message cost based on character and byte length.
    
    Args:
        messages (str): Multi-line string containing messages.
        
    Returns:
        int: Total cost for all messages.
    """
    cost = 0
    for message in messages.splitlines():
        match len(message) <= 140, len(message.encode('utf-8')) <= 160:
            case True, True:
                cost += 13
            case False, True:
                cost += 11
            case True, False:
                cost += 7
            case False, False:
                pass
    return cost
