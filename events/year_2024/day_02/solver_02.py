"""Codyssi - Year 2024 - Day 02 - Sensors and circuits"""


def preprocessing(puzzle_input):
    """
    Preprocess the puzzle input by converting each sensor reading to a binary value.

    Args:
        puzzle_input (str): A string containing sensor readings, one per line.
            Each reading is either 'TRUE' or something else.
            
    Returns:
        list[int]: A list of binary values where 1 represents 'TRUE' and 0 represents 
        any other value.
    """
    sensors = []
    for sensor in puzzle_input.splitlines():
        if sensor == "TRUE":
            sensors.append(1)
        else:
            sensors.append(0)
    return sensors


def solver(sensors):
    """
    Process a list of sensors through logical operations and aggregation.

    This function processes a list of sensor values (0s and 1s) in three phases:
    1. Returns the sum of indices (1-based) of sensors that have a value of 1
    2. Iteratively processes sensors in groups of 4, applying AND operation to first pair
        and OR operation to second pair, then returns the sum of active sensors after first 
        iteration
    3. Returns the sum of all sensor counts from all iterations

    Args:
         sensors: List of integers (0s and 1s) representing sensor values

    Yields:
         int: Sum of 1-based indices where sensor value is 1
         int: Sum of active sensors after first iteration
         int: Total sum of active sensors across all iterations
    """
    yield sum(n for n, s in enumerate(sensors, 1) if s == 1)
    cnts = [sum(sensors)]
    new_sensors = []
    while len(sensors) != 1:
        for i in range(0, len(sensors), 4):
            new_sensors.append(sensors[i] & sensors[i + 1])
            try:
                new_sensors.append(sensors[i + 2] | sensors[i + 3])
            except IndexError:
                pass
        cnts.append(sum(new_sensors))
        sensors = new_sensors.copy()
        new_sensors = []
    yield cnts[1]
    yield sum(cnts)
