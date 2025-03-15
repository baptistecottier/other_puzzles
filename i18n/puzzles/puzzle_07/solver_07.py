"""Internationalization Puzzles - Day 07 - The audit trail fixer"""


from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def preprocessing(puzzle_input):
    """Preprocess puzzle input by extracting timestamps and calculating time deltas.
    
    Args:
        puzzle_input: A multi-line string with records formatted as "timestamp correct wrong"
    
    Returns:
        List of tuples containing (datetime timestamp, delta) where delta is 
        the difference between correct and wrong values
    """
    records = []
    for record in puzzle_input.splitlines():
        timestamp, correct, wrong = record.split()
        delta = int(correct) - int(wrong)
        dt_timestamp = datetime.fromisoformat(timestamp)
        records.append((dt_timestamp, delta))
    return records


def solver(records: list[tuple[datetime, int]]):
    """Calculates a result based on timestamps and time zone information.
    
    Args:
        records: List containing tuples of (timestamp, delta), where timestamp 
                is a datetime object and delta is the number of minutes to add.
    
    Returns:
        Sum of each record's index multiplied by the hour of the adjusted timestamp.
        
    Note: 
        Timestamp need to be located befored adjustment as it may switch from summer 
        time to winter time of reciprocally
    """
    result = 0
    for n, (timestamp, delta) in enumerate(records, 1):
        if ZoneInfo("America/Halifax").utcoffset(timestamp) == timestamp.utcoffset():
            zone = "America/Halifax"
        else:
            zone = "America/Santiago"


        timestamp = timestamp + timedelta(minutes = delta)
        timestamp = timestamp.astimezone(ZoneInfo(zone))
        result += n * timestamp.hour

    return result
