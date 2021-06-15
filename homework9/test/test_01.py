import pytest

from homework9.hw.task01 import merge_sorted_files


@pytest.fixture()
def create_and_del_files(tmpdir):

    def file_factory(*body):
        for element in body:
            file = tmpdir.join('my_file'+str(len(tmpdir.listdir())))
            file.write(element)
        return tmpdir.listdir()

    return file_factory


@pytest.fixture()
def data_test_number_one(create_and_del_files):
    return create_and_del_files('1\n3\n5', '2\n4\n6')


@pytest.fixture()
def data_test_number_two(create_and_del_files):
    return create_and_del_files('1\n1\n6\n8\n10', '2\n3\n5\n7\n11')


@pytest.fixture()
def data_test_numbers_with_symbols(create_and_del_files):
    return create_and_del_files('1\na\n3\nb\n5', '2\nc\n4\nd\n6')


def test_text_with_numbers_one(data_test_number_one):
    assert list(merge_sorted_files(data_test_number_one)) == \
           [1, 2, 3, 4, 5, 6]


def test_text_with_number_two(data_test_number_two):
    assert list(merge_sorted_files(data_test_number_two)) == \
           [1, 1, 2, 3, 5, 6, 7, 8, 10, 11]


def test_text_with_numbers_and_symbols(data_test_numbers_with_symbols):
    assert list(merge_sorted_files(data_test_numbers_with_symbols)) == \
           [1, 2, 3, 4, 5, 6]
