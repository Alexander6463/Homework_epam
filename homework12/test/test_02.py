from homework12.hw.task02 import Order, elder_discount, morning_discount


def test_morning_discount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50


def test_elder_discount():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_change_strategy():
    order_3 = Order(100, morning_discount)
    order_3.strategy = elder_discount
    assert order_3.final_price() == 10
