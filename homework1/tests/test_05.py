from homework1.hw.task05 import find_maximal_subarray_sum


def test_number_one():
    """Testing lists of numbers [1, 3, -1, -3, 5, 3, 6, 7] and k = 3"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_number_two():
    """Testing list of numbers [0, 0, 0, 0, 0, 0], k = 2"""
    assert find_maximal_subarray_sum([0, 0, 0, 0, 0, 0], 2) == 0
