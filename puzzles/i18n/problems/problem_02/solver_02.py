"""Internationalization Puzzles - Day 02 - Detecting gravitational waves"""

import datetime
from collections import defaultdict
import pytz

def solver(records):
    """
    Finds the UTC time of a record that appears exactly 4 times in different timezones.

    Args:
        records (str): String containing datetime records in format YYYY-MM-DDTHH:MM±HH:MM

    Returns:
        str: UTC time in ISO format where record appears 4 times
    """
    local_times = defaultdict(int)
    for record in records.splitlines():
        local_time = datetime.datetime.fromisoformat(record)
        if local_times[local_time] == 3:
            return local_time.astimezone(pytz.utc).isoformat()
        local_times[local_time] += 1
    return None
