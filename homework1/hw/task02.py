from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    if len(data) == 1 and data[0] == 0:
        return True
    elif len(data) == 2 and data[0] == 0 and data[1] == 1:
        return True
    else:
        for index in range(2, len(data)):
            if data[index] == data[index - 1] + data[index - 2]:
                continue
            else:
                return False
        return True
