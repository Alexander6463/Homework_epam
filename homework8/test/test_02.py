import os
from collections.abc import Iterable

from homework8.hw.task02 import TableData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "example.sqlite")
presidents = TableData(db_path, 'presidents')


def test_get_item_table_data():
    assert presidents['Putin'] == ('Putin', 222, 'RUS')


def test_len_table_data():
    assert len(presidents) == 4


def test_contains_table_data():
    assert 'Trump' in presidents


def test_negative_contains_table_data():
    assert 'Medvedev' not in presidents


def test_iter_table_data():
    assert isinstance(presidents, Iterable)
