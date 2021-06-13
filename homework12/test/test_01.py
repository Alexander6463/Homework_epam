import pytest

from homework12.hw.task01 import ColorsEnum, SizesEnum


def test_colors_enum_positive():
    assert ColorsEnum().RED == 'RED'
    assert ColorsEnum().BLACK == 'BLACK'


def test_colors_enum_negative():
    with pytest.raises(AttributeError):
        ColorsEnum().BROWN


def test_sizes_enum_positive():
    assert SizesEnum().S == 'S'
    assert SizesEnum().XL == 'XL'


def test_sizes_enum_negative():
    with pytest.raises(AttributeError):
        SizesEnum().XXL
