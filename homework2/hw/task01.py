"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    dict_words = dict()
    result_list = list()
    with open(file_path, "r", encoding="unicode-escape") as f:
        text = f.read().split("\n")
    new_text = str()
    set_words = set()
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
    list_words = new_text.split()
    set_words = set(list_words)
    for word in set_words:
        set_chars = set()
        for char in word:
            if char not in set_chars:
                set_chars.add(char)
        dict_words[word] = (len(word), len(set_chars))
    list_words = list(dict_words.items())
    list_words.sort(key=lambda i: (i[1][0], i[1][1]), reverse=True)
    return [word[0] for word in list_words[:10]]


def get_rarest_char(file_path: str) -> str:
    dict_chars = dict()
    with open(file_path, "r", encoding="unicode-escape") as f:
        text = f.read().split("\n")
    for line in text:
        for char in line:
            if char in dict_chars:
                dict_chars[char] += 1
            else:
                dict_chars[char] = 1
    list_chars = list(dict_chars.items())
    list_chars.sort(key=lambda i: i[1], reverse=True)
    return list_chars[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path, "r", encoding="unicode-escape") as f:
        text = f.read().split("\n")
    for line in text:
        for char in line:
            if char in punctuation:
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path, "r", encoding="unicode-escape") as f:
        text = f.read().split("\n")
    for line in text:
        for char in line:
            if not char.isascii():
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    dict_non_ascii_chars = dict()
    with open(file_path, "r", encoding="unicode-escape") as f:
        text = f.read().split("\n")
    for line in text:
        for char in line:
            if not char.isascii():
                if char in dict_non_ascii_chars:
                    dict_non_ascii_chars[char] += 1
                else:
                    dict_non_ascii_chars[char] = 1
    list_chars = list(dict_non_ascii_chars.items())
    list_chars.sort(key=lambda i: i[1], reverse=True)
    return list_chars[0][0]
