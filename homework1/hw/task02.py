"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if not data:
        return False
    if data == [0] or data == [0, 1]:
        return True
    else:
        for index in range(2, len(data)):
            if data[index] == data[index - 1] + data[index - 2]:
                continue
            else:
                return False
        return True
