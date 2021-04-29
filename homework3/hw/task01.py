""" In previous homework task 4, you wrote a cache function
that remembers other function output value. Modify it to be a
parametrized decorator, so that the following code:
@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2,
     use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2' """


from functools import wraps
from typing import Callable


def cache(times: int) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: int) -> int:
            key_cache = tuple(args)
            if cache.times == 0:
                cache.dict = dict()
                cache.times = times
            if key_cache not in cache.dict:
                cache.dict[key_cache] = func(*key_cache)
            else:
                cache.times -= 1
            return cache.dict[key_cache]

        return wrapper

    cache.dict = dict()
    cache.times = times
    return outer
