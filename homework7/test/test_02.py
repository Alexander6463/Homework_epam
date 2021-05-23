from homework7.hw.task02 import backspace_compare


def test_strings_with_one_backspace():
    assert backspace_compare("ab#c", "ad#c") is True


def test_string_startwith_backspace():
    assert backspace_compare("a##c", "#a#c") is True


def test_string_without_backspace():
    assert backspace_compare("a#c", "b") is False
