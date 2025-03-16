"""Codyssi - Year 2024 - Day 02 - Sensors and circuits"""


def preprocessing(puzzle_input: str) -> list[bool]:
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
        sensors.append(sensor == "TRUE")
    return sensors


def solver(sensors: list[bool]):
    """
    Process sensors list through logical operations and yield statistical results.
    
    Args:
        sensors: List of boolean values representing sensor states (1/True or 0/False)
    
    Yields:
        int: Sum of indices of active sensors (1-indexed)
        int: Sum of active sensors after first transformation
        int: Sum of all active sensors across all transformations
    """
    yield sum(n for n, s in enumerate(sensors, 1) if s is True)
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
