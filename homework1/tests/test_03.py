import os

from homework1.hw.task03 import find_maximum_and_minimum

print(os.getcwd())


def test_min_max():
    """Testing list of numbers [-5, -3, 0, 5, 10]"""
    assert find_maximum_and_minimum("homework1/"
                                    "tests/"
                                    "files_for_test/"
                                    "example1.txt") == (-5, 10)


def test_equal_numbers():
    assert find_maximum_and_minimum("homework1/"
                                    "tests/"
                                    "files_for_test/"
                                    "example2.txt") == (5, 5)
