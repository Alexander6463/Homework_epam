from homework5.hw.task02 import print_result


@print_result
def some_function(*args):
    """This function sum numbers"""
    return sum(args)


def test_result_some_function():
    assert some_function(1, 2, 3, 4) == 10


def test_doc_string_some_function():
    assert some_function.__doc__ == "This function sum numbers"


def test_name_some_function():
    assert some_function.__name__ == "some_function"


def test_atr_original_func():
    assert some_function.__original_func(1, 2, 3, 4) \
           == some_function(1, 2, 3, 4)


def test_std_out(capsys):
    some_function(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out == "10\n"
