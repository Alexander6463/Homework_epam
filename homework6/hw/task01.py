"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""

    class Wrapper(cls):
        cls.counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            cls.counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            cls.counter = 0

    return Wrapper


@instances_counter
class User:
    def __init__(self, first_name):
        self.first_name = first_name

    def get_name(self):
        return self.first_name


if __name__ == "__main__":

    print(User.get_created_instances())  # 0
    user, _, _ = User('Petr'), User('Sasha'), User('Nikolay')
    print(user.get_created_instances(), user.get_name())  # 3
    user.reset_instances_counter()  # 3
    print(user.get_created_instances())
