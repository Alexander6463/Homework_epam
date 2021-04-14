"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_max_and_min(file_name: str) -> Tuple[int, int]:
    max_value = int()
    min_value = int()
    with open(file_name, "r") as f:
        for line in f:
            if max_value <= int(line) or not max_value:
                max_value = int(line)
            if min_value >= int(line) or not min_value:
                min_value = int(line)
    return min_value, max_value
