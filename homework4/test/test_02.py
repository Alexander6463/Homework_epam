from unittest.mock import patch

from homework4.hw.task02 import count_dots_on_i


def test_with_three_i():
    with patch("requests.get") as fake_get:
        fake_get.return_value.text = 'iaiaia'
        assert count_dots_on_i('asdf') == 3


def test_with_five_i():
    with patch("requests.get") as fake_get:
        fake_get.return_value.text = 'iiiii'
        assert count_dots_on_i("zzz") == 5


def test_with_null_i():
    with patch("requests.get") as fake_get:
        fake_get.return_value.text = 'ggggg'
        assert count_dots_on_i("zasdf") == 0


def test_negative_case():
    with patch("requests.get") as fake_get:
        fake_get.return_value.text = 'gig'
        assert count_dots_on_i("gggg") != 5


def test_exception_case():
    with patch("requests.get") as fake_get:
        fake_get.return_value.text = ValueError
        try:
            count_dots_on_i("https://example.com")
        except Exception:
            assert ValueError
