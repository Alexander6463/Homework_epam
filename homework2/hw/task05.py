"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, List, Union


def custom_range(iter_sequence: Iterable, *args: Union) -> List[str]:
    list_sequence = list(iter_sequence)
    if len(args) == 1:
        stop = list_sequence.index(args[0])
        return list_sequence[:stop]
    elif len(args) == 2:
        start = list_sequence.index(args[0])
        stop = list_sequence.index(args[1])
        return list_sequence[start:stop]
    else:
        step = args[2]
        start = list_sequence.index(args[0])
        stop = list_sequence.index(args[1])
        if step >= 1:
            return list_sequence[start:stop:step]
        else:
            list_sequence = list_sequence[::-1]
            start = list_sequence.index(args[0])
            stop = list_sequence.index(args[1])
            return list_sequence[start:stop:step * (-1)]
