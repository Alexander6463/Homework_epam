"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    values = list()
    with open(file_name, "r") as f:
        for line in f:
            if len(values) == 0:
                min_value = int(line)
                max_value = int(line)
            values.append(int(line))
            if min_value > int(line):
                min_value = int(line)
            if max_value < int(line):
                max_value = int(line)
    return min_value, max_value
