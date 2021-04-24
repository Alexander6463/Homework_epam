from datetime import datetime, timedelta

from homework3.hw.task02 import *


def test_multiprocessing_calculate_time_and_value():
    start = datetime.now()
    value = multiprocessing_calculate(slow_calculate)
    end = datetime.now()
    assert end - start < timedelta(seconds=60)
    assert value == 1024259
