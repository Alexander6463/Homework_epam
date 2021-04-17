from homework2.hw.task04 import cache


def test_positive():
    """Testing that val1 is val2 after cache function"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_negative():
    """Testing that val1 after cache function and val2 = func(*some) is not same"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = func(*some)
    assert val_1 is not val_2


def test_values():
    """Testing that value1 after cache function is same that value after func"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = func(*some)
    assert val_1 == val_2


def test_other_func():
    """Testing other function"""

    def func(a, b):
        return (a * b) ** 3

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
