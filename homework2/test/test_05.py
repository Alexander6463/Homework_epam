import string

from homework2.hw.task05 import custom_range


def test_stop_str():
    """Testing string.ascii_lowercase and symbol stop = 'g' """
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c",
                                                         "d", "e", "f"]


def test_start_stop_str():
    """Testing string.ascii_lowercase with start = 'g' and stop = 'p' """
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_start_stop_step_str():
    """Testing string.ascii_lowercase
    with start = 'p', stop = 'g', step = -2 """
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_stop_list():
    """Testing [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and stop = 4"""
    assert custom_range([i for i in range(10)], 4) == [0, 1, 2, 3]


def test_start_stop_list():
    """Testing [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with start = 4 and stop = 7"""
    assert custom_range([i for i in range(10)], 4, 7) == [4, 5, 6]


def test_start_stop_step_list():
    """Testing [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with start = 8 and stop = 1, step = -2"""
    assert custom_range([i for i in range(10)], 8, 1, -2) == [8, 6, 4, 2]
