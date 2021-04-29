from homework1.hw.task03 import find_max_and_min

path = "homework1/tests/files_for_test/"


def test_min_max():
    """Testing list of numbers [-5, -3, 0, 5, 10]"""
    assert find_max_and_min(path+'example1.txt') == (-5, 10)


def test_equal_numbers():
    """Testing list of numbers [5, 5, 5, 5, 5]"""
    assert find_max_and_min(path+'example2.txt') == (5, 5)
