"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
 with Supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Supressor:
    def __init__(self, exc):
        self.exception = exc

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return isinstance(exc_val, self.exception)


@contextmanager
def supressor_gen(exception) -> None:
    try:
        yield
    except exception:
        pass
