from homework7.hw.task03 import tic_tac_toe_checker


def test_x_win():
    assert tic_tac_toe_checker(([['-', '-', 'o'],
                                 ['-', 'o', 'o'],
                                 ['x', 'x', 'x']])) == 'x wins!'


def test_o_win():
    assert tic_tac_toe_checker([['-', '-', 'o'],
                                ['-', 'x', 'o'],
                                ['x', 'x', 'o']]) == 'o wins!'


def test_draw():
    assert tic_tac_toe_checker([['o', 'x', 'o'],
                                ['o', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'draw!'


def test_unfinished():
    assert tic_tac_toe_checker([['-', '-', 'o'],
                                ['-', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'unfinished'


def test_unfinished_with_empty_board():
    assert tic_tac_toe_checker([['-', '-', '-'],
                                ['-', '-', '-'],
                                ['-', '-', '-']]) == 'unfinished'
