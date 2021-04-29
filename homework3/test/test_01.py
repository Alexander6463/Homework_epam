import sys

from homework3.hw.task01 import cache

path = 'homework3/test/data.txt'


def test_working_cache_decorator_with_times_2():
    @cache(times=2)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(2):
            assert f() == str(i)
    sys.stdin.close()


def test_working_cache_decorator_with_times_4():
    @cache(times=4)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(4):
            assert f() == str(i)
    sys.stdin.close()


def test_working_cache_decorator_with_times_1():
    @cache(times=1)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(1):
            assert f() == str(i)
    sys.stdin.close()
