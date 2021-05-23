from homework6.hw.task01 import instances_counter


@instances_counter
class User:
    def __init__(self, first_name):
        self.first_name = first_name

    def get_name(self):
        return self.first_name


def test_get_created_instances_method_with_0_instances():
    assert User.get_created_instances() == 0


def test_get_created_instances_method_with_3_instances():
    _, _, _ = User('Petr'), User('Sasha'), User('Nikolay')
    assert User.get_created_instances() == 3


def test_reset_instances_method():
    user, _, _ = User('Petr'), User('Sasha'), User('Nikolay')
    user.reset_instances_counter()
    assert User.get_created_instances() == 0
