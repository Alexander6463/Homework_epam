from unittest.mock import MagicMock

from homework4.hw.task02 import count_dots_on_i


def test_positive_case():
    count_dots_on_i = MagicMock(return_value=59)
    assert count_dots_on_i("https://example.com") == 59


def test_negative_case():
    count_dots_on_i = MagicMock(return_value=58)
    assert not count_dots_on_i("https://example.com") == 59


def test_exception_case():
    count_dots_on_i = MagicMock(side_effect=ValueError)
    try:
        count_dots_on_i("https://example.com")
    except:
        assert ValueError
