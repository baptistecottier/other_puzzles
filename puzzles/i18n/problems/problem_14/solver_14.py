"""Internationalization Puzzles - Day 14 - Metrification in Japan"""

from kanjize import kanji2number


def preprocessing(puzzle_input: str) -> list[tuple[int, ...]]:
    """
    Process the puzzle input to extract width, height, and unit information from land dimensions.
    """
    dimensions = []
    for land in puzzle_input.splitlines():
        width, height = land.split(' × ')
        w_value, w_unit = kanji2number(width[:-1]), width[-1]
        h_value, h_unit = kanji2number(height[:-1]), height[-1]
        dimensions.append(w_value, w_unit, h_value, h_unit)


def solver(dimensions: list[tuple[int, ...]]):
    """
    Calculates the total area by summing the area of each dimension in the input list.
    """
    area_size = sum(get_area(*area) for area in dimensions)
    return area_size


def get_area(w_value, w_unit, h_value, h_unit):
    """
    Calculate area given width and height values with Japanese traditional units.
    """
    unit_to_int = {
        '尺': 1      , '間': 6    , '丈': 10      ,
        '町': 360    , '里': 12960, '毛': 1/10_000,
        '厘': 1/1_000, '分': 1/100, '寸': 1/10    ,
        }
    return w_value * unit_to_int[w_unit] * h_value * unit_to_int[h_unit]
