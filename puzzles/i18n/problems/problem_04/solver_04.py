"""Internationalization Puzzles - Day 03 - Unicode passwords"""

from zoneinfo import ZoneInfo
import datetime as dt


def preprocessing(puzzle_input: str):
    """
    Processes a puzzle input string containing flight information and converts it into datetime 
    objects.
    """
    times = []
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for flight in puzzle_input.splitlines():
        if flight == '':
            continue

        place = flight[11:42].strip()

        year = int(flight[50:54])
        month = months.index(flight[42:45]) + 1
        day = int(flight[46:48])

        h = int(flight[56:58])
        m = int(flight[59:61])

        time = dt.datetime(year, month, day, h, m, tzinfo=ZoneInfo(place))
        times.append(time)
    return times


def solver(times: list):
    """Calculate total time difference in minutes from a list of timestamps.

    This function processes a list of timestamps in pairs, calculating the difference
    between consecutive pairs and summing up the total time difference. The timestamps
    are processed from the end of the list toward the beginning.
    """
    total = times.pop() - times.pop()
    while times:
        total += times.pop() - times.pop()
    return int(total.total_seconds() / 60)
