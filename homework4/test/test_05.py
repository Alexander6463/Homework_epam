from homework4.hw.task05 import fizzbuzz


def test_5_fizz_buzz():
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]


def test_10_fizz_buzz():
    assert list(fizzbuzz(10)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
    ]


def test_20_fizz_buzz():
    assert list(fizzbuzz(20)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizz buzz",
        "16",
        "17",
        "fizz",
        "19",
        "buzz",
    ]
