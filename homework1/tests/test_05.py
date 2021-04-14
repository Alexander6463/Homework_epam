from homework1.hw.task05 import find_maximal_subarray_sum


def test_number_one():
    """Testing lists of numbers [1, 3, -1, -3, 5, 3, 6, 7] and k = 3"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_number_two():
    """Testing list of numbers [0, 0, 0, 0, 0, 1], k = 2"""
    assert find_maximal_subarray_sum([0, 0, 0, 0, 0, 1], 2) == 1


def test_number_three():
    """Testing list of numbers [-3, 5, 7, 1, 4, -10], k = 5"""
    assert find_maximal_subarray_sum([-3, 5, 7, 1, 4, -10], 5) == 14


def test_number_four():
    """Testing list of numbers [-4, 1, 3, 4, 6, 1, 5], k = 7"""
    assert find_maximal_subarray_sum([-4, 1, 3, 4, 6, 1, 5], 7) == 16


def test_number_five():
    """Testing list of numbers [-4, 1, 3, 4, 6, 1, 5], k = 1"""
    assert find_maximal_subarray_sum([-4, 1, 3, 4, 6, 1, 5], 1) == 6


def test_number_six():
    """Testing list of numbers [-4, 1, 3, 4, 6, 1, 5], k = 0"""
    assert find_maximal_subarray_sum([-4, 1, 3, 4, 6, 1, 5], 0) == 0


def test_number_seven():
    """Testing list of numbers [1000, 1, 5, 999, 333, 0, -200], k = 1"""
    assert find_maximal_subarray_sum([100, 1, 5, 99, 33, 0, -200], 1) == 100
