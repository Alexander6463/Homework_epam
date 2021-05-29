import pytest

from homework9.hw.task03 import universal_file_counter


@pytest.fixture()
def create_and_del_files(tmpdir):

    def file_factory(*body):
        for element in body:
            file = tmpdir.join('my_file'+str(len(tmpdir.listdir()))+'.txt')
            file.write(element)
        return tmpdir.strpath

    return file_factory


@pytest.fixture()
def data_test_1(create_and_del_files):
    return create_and_del_files('1\n3 5\n5 6 7', '2\n4\n6\n8')


@pytest.fixture()
def data_test_2(create_and_del_files):
    return create_and_del_files('1 3 a e\n3 5\n5 6 \n7',
                                '2 5 g\n4 3cde\n6eq\n8 2')


def test_with_no_tokenizer_with_numbers(data_test_1):
    assert universal_file_counter(data_test_1, 'txt') == 7


def test_with_tokenizer_with_numbers(data_test_1):
    assert universal_file_counter(data_test_1, 'txt', str.split) == 10


def test_with_no_tokenizer_with_numbers_and_symbols(data_test_2):
    assert universal_file_counter(data_test_2, 'txt') == 8


def test_with_tokenizer_with_numbers_and_symbols(data_test_2):
    assert universal_file_counter(data_test_2, 'txt', str.split) == 17
