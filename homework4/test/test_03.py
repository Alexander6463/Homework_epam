from homework4.hw.task03 import my_precious_logger


def test_std_err_positive(capsys):
    my_precious_logger("error: file not found\n")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found\n"


def test_std_out_positive(capsys):
    my_precious_logger("OK\n")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"


def test_std_err_negative(capsys):
    my_precious_logger("There is no errors")
    captured = capsys.readouterr()
    assert captured.err != "There is no errors"


def test_std_out_negative(capsys):
    my_precious_logger("error: ValueError Exception")
    captured = capsys.readouterr()
    assert captured.out != "error: ValueError Exception"
