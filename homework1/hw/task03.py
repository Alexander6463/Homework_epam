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
