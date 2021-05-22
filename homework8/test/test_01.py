import os

import pytest

from homework8.hw.task01 import KeyValueStorage


@pytest.fixture()
def create_and_del_file(tmp_path):
    def file_factory(body):
        file_path = os.path.join(tmp_path, 'test')
        with open(file_path, 'w') as f:
            f.write(body)
        return file_path
    return file_factory


def test_setattr_key_value_storage(create_and_del_file):
    storage = KeyValueStorage(create_and_del_file('name=kek'))
    assert storage.name == 'kek'


def test_setitem_key_value_storage(create_and_del_file):
    storage = KeyValueStorage(create_and_del_file('asdf=lalala'))
    assert storage['asdf'] == 'lalala'


def test_integer_value_key_value_storage(create_and_del_file):
    storage = KeyValueStorage(create_and_del_file('last_name=1'))
    assert type(storage.last_name) is int


def test_key_error(create_and_del_file):
    with pytest.raises(ValueError):
        KeyValueStorage(create_and_del_file('1=last_name'))
