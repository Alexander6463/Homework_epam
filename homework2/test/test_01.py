from collections import Counter
from string import punctuation

from homework2.hw.task01 import (count_non_ascii_chars,
                                 count_punctuation_chars,
                                 get_longest_diverse_words,
                                 get_most_common_non_ascii_char,
                                 get_rarest_char)

path = 'homework2/test/test_files/test01.txt'


def test_one_example1():
    """Testing function get_longest_diverse_words"""

    assert get_longest_diverse_words(path) == [
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


def test_one_library():
    with open(path, "r", encoding="unicode-escape") as f:
        new_text = str()
        text = f.read().replace("\n", " ").split()
        # print(Counter(text))
        for line in text:
            if line.endswith("-"):
                line = line.replace("-", "")
            new_text += (
                line.replace(",", " ")
                .replace(".", " ")
                .replace(":", " ")
                .replace(";", " ")
                .replace("?", " ")
                + " "
            )
    result = list()
    c2 = Counter(word for word in new_text.split() for char in set(word))
    c1 = Counter(word for word in new_text.split() for char in word)
    for word in new_text.split():
        result.append((word, (c1[word], c2[word])))
    result.sort(key=lambda i: (i[1][0], i[1][1]), reverse=True)
    assert get_longest_diverse_words(path) == [
        word[0] for word in result[:10]
    ]


def test_two():
    """Testing get_rarest_char"""
    with open(path, "r", encoding="unicode-escape") as f:
        text = f.read().replace(" ", "")
    assert (
        get_rarest_char(path) == Counter(text).most_common()[-1][0]
    )


def test_two_library():
    """Testing get_rarest_char"""
    assert get_rarest_char(path) == "??"


def test_three():
    """Testing count_punctuation_chars"""
    assert count_punctuation_chars(path) == 27


def test_three_library():
    with open(path, "r", encoding="unicode-escape") as f:
        text = f.read().replace(" ", "").replace("\n", "")
    assert count_punctuation_chars(path) == sum(
                Counter(c for c in text if c in punctuation).values())


def test_four():
    """Testing count_non_ascii_chars"""
    assert count_non_ascii_chars(path) == 7


def test_four_library():
    """Testing count_non_ascii_chars"""
    with open(path, "r", encoding="unicode-escape") as f:
        text = f.read().replace(" ", "").replace("\n", "")
    assert count_non_ascii_chars(path) == sum(
        Counter(c for c in text if not c.isascii()).values()
    )


def test_five():
    """Testing get_most_common_non_ascii_char"""
    assert get_most_common_non_ascii_char(path) == "??"


def test_five_library():
    """Testing get_most_common_non_ascii_char"""
    with open(path, "r", encoding="unicode-escape") as f:
        text = f.read().replace(" ", "").replace("\n", "")
    assert (
        get_most_common_non_ascii_char(path)
        == Counter(c for c in text if not c.isascii()).most_common()[0][0]
    )
