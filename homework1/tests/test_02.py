from homework1.hw.task02 import check_fibonacci


def test_positive_case():
    """Testing that sequence is fibonacci sequence"""
    assert check_fibonacci(
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    )


def test_negative_case():
    """Testing that sequence is not fibonacci sequence"""
    assert not check_fibonacci([2, 3, 5, 1, 34, 5, 6])


def test_boundary_conditions():
    """Testing boundary conditions"""
    assert check_fibonacci([0])


def test_null_sequence():
    """Testing null sequence"""
    assert not check_fibonacci([])
