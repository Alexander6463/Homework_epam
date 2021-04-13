from homework1.hw.task04 import check_sum_of_four


def test_number_one():
    """Testing lists of numbers [1,2], [-2,-1], [-1,2], [0,2]"""
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_number_two():
    """Testing list of numbers [0], [0], [0], [0]"""
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_number_three():
    """Testing list of numbers [1], [2], [3], [4]"""
    assert check_sum_of_four([1], [2], [3], [4]) == 0
