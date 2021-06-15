import pytest

from homework9.hw.task02 import Supressor, supressor_gen


def test_supressor_class_positive():
    with Supressor(ValueError):
        raise ValueError


def test_supressor_class_raise_error():
    with Supressor(ValueError):
        with pytest.raises(AttributeError):
            raise AttributeError


def test_supressor_gen_positive():
    with supressor_gen(ValueError):
        raise ValueError


def test_supressor_gen_raise_error():
    with supressor_gen(ValueError):
        with pytest.raises(AttributeError):
            raise AttributeError
