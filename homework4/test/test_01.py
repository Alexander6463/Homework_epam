import os

import pytest

from homework4.hw.task01 import read_magic_number


@pytest.fixture()
def create_and_del_file(tmp_path):
    def file_factory(body):
        file_path = os.path.join(tmp_path, 'test')
        with open(file_path, 'w') as f:
            f.write(body)
        return file_path
    return file_factory


def test_number_2_is_positive(create_and_del_file):
    assert read_magic_number(create_and_del_file('2'))


def test_number_5_is_negative(create_and_del_file):
    assert not read_magic_number(create_and_del_file('5'))


def test_number_3_is_negative(create_and_del_file):
    assert not read_magic_number(create_and_del_file('3'))


def test_exception_case(create_and_del_file):
    try:
        read_magic_number(create_and_del_file('a'))
    except ValueError:
        assert ValueError


def test_file_is_not_exist():
    try:
        read_magic_number('lalal')
    except FileExistsError:
        assert FileExistsError
