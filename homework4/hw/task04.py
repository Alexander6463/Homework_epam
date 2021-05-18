"""
Write a function that takes a number N as an
input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions
>>> fizzbuzz(5)
['1', '2', 'Fizz', '4', 'Buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return list fizzbuzz, for run doctest with pytest
    use command pytest --doctest-modules

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(10)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz',
    'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']

    """
    result = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("Fizz Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
