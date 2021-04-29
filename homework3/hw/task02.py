"""Here's a not very efficient calculation function
that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):
    Some weird voodoo magic calculations
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))
Calculate total sum of slow_calculate() of all numbers
starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function."""
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Callable


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def multiprocessing_calculate(func: Callable) -> int:
    """Calculate sum of function value in range(500)"""
    list_numbers = [i for i in range(500)]
    with Pool(50) as p:
        result = p.map(func, list_numbers)
        p.close()
        p.join()
    return sum(result)
