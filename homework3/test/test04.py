from homework3.hw.task04 import is_armstrong


def test_armstrong_number_153():
    assert is_armstrong(153) == True


def test_non_armstrong_number_10():
    assert is_armstrong(10) == False


def test_armstrong_number_9():
    assert is_armstrong(9) == True


def test_non_armstrong_number_11():
    assert is_armstrong(11) == False
