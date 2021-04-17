from homework2.hw.task01 import *


def test_one_example1():
    """Testing function get_longest_diverse_words"""
    assert get_longest_diverse_words("test_files/test01.txt") == [
        "swpkfperngsdergac",
        "aretgdswerpasdfgr",
        "dorjlwkrogkbmsex",
        "apsekfpemgflaeer",
        "abcdefghklemnbd",
        "asdlrpwermdckae",
        "ajwelrjwoeksla",
        "akepekgkaseprw",
        "akepwkfjroplf",
        "skepwladmede",
    ]


def test_two():
    """Testing get_rarest_char"""
    assert get_rarest_char("test_files/test01.txt") == "L"


def test_three():
    """Testing count_punctuation_chars"""
    assert count_punctuation_chars("test_files/test01.txt") == 27


def test_four():
    """Testing count_non_ascii_chars"""
    assert count_non_ascii_chars("test_files/test01.txt") == 7


def test_five():
    """Testing get_most_common_non_ascii_char"""
    assert get_most_common_non_ascii_char("test_files/test01.txt") == "ä"
