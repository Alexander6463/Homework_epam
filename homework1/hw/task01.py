def check_power_of_2(a: int) -> bool:
    if a == 0:
        return False
    while a % 2 != 1:
        a /= 2
    if a != 1:
        return False
    else:
        return True
