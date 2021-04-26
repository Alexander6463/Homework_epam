import os
import tempfile

import pytest

from homework4.hw.task01 import read_magic_number


@pytest.fixture()
def create_and_del_file():
    f = open("test.txt", "w")
    yield f
    os.remove("test.txt")


def test_number_2_is_positive(create_and_del_file):
    file = create_and_del_file
    file.write("2")
    file.close()
    assert read_magic_number(file.name)


def test_number_5_is_negative(create_and_del_file):
    file = create_and_del_file
    file.write("5")
    file.close()
    assert not read_magic_number(file.name)


def test_number_3_is_negative(create_and_del_file):
    file = create_and_del_file
    file.write("3")
    file.close()
    assert not read_magic_number(file.name)


def test_exception_case(create_and_del_file):
    file = create_and_del_file
    file.write("a")
    file.close()
    assert read_magic_number(file.name) is ValueError
