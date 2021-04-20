from collections import Counter

from homework2.hw.task02 import major_and_minor_elem


def test_one():
    """Testing [3,2,3]"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_two():
    """Testing [2,2,1,1,1,2,2]"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_three():
    """Testing [1,1,1,1,1,3,3,3,4,4,4,4,4,5]"""
    assert major_and_minor_elem([1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5]) == (1, 5)


def test_four():
    """Testing [-5,-5,-5,-5,-1,0,0]"""
    assert major_and_minor_elem([-5, -5, -5, -5, -1, 0, 0]) == (-5, -1)


def test_five():
    """Testing [4,5,3,2,3,5,4,5]"""
    assert major_and_minor_elem([4, 5, 3, 2, 3, 5, 4, 5]) == (5, 2)


def test_one_lib():
    """Testing [3,2,3]"""
    assert major_and_minor_elem([3, 2, 3]) == (
        Counter([3, 2, 3]).most_common()[0][0],
        Counter([3, 2, 3]).most_common()[-1][0],
    )


def test_two_lib():
    """Testing [2,2,1,1,1,2,2]"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (
        Counter([2, 2, 1, 1, 1, 2, 2]).most_common()[0][0],
        Counter([2, 2, 1, 1, 1, 2, 2]).most_common()[-1][0],
    )


def test_three_lib():
    """Testing [1,1,1,1,1,3,3,3,4,4,4,4,4,5]"""
    assert major_and_minor_elem([1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5]) == (
        Counter([1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5]).most_common()[0][0],
        Counter([1, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5]).most_common()[-1][0],
    )


def test_four_lib():
    """Testing [-5,-5,-5,-5,-1,0,0]"""
    assert major_and_minor_elem([-5, -5, -5, -5, -1, 0, 0]) == (
        Counter([-5, -5, -5, -5, -1, 0, 0]).most_common()[0][0],
        Counter([-5, -5, -5, -5, -1, 0, 0]).most_common()[-1][0],
    )


def test_five_lib():
    """Testing [4,5,3,2,3,5,4,5]"""
    assert major_and_minor_elem([4, 5, 3, 2, 3, 5, 4, 5]) == (
        Counter([4, 5, 3, 2, 3, 5, 4, 5]).most_common()[0][0],
        Counter([4, 5, 3, 2, 3, 5, 4, 5]).most_common()[-1][0],
    )
