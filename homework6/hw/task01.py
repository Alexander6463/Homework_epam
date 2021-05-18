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

        @classmethod
        def __init__(cls):
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
    pass


if __name__ == "__main__":

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    user.reset_instances_counter()  # 3
    print(user.get_created_instances())
