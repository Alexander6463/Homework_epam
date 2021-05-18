from homework6.hw.task01 import instances_counter


@instances_counter
class User:
    pass


def test_get_created_instances_method_with_0_instances():
    assert User.get_created_instances() == 0


def test_get_created_instances_method_with_3_instances():
    _, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances_method():
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert User.get_created_instances() == 0
