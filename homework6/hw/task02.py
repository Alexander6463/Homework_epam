"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

import datetime
from collections import defaultdict
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class HomeworkResult:
    def __init__(self, student, homework, solve):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solve
        self.author = student
        self.created = datetime.datetime.now()


class Homework:
    def __init__(self, text_of_task, deadline_days):
        self.text = text_of_task
        self.deadline = datetime.timedelta(deadline_days)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < (self.created + self.deadline)


class Student(Human):
    def do_homework(self, homework, result):
        if homework.is_active():
            return HomeworkResult(self, homework, result)
        else:
            raise DeadlineError("You are late")


class Teacher(Human):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].add(
                (homework_result.author, homework_result.solution)
            )
            return True
        return False

    @classmethod
    def reset_results(cls, homework_result=None):
        if homework_result is not None:
            cls.homework_done.pop(homework_result)
        else:
            cls.homework_done = defaultdict()


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    result_5 = lazy_student.do_homework(oop_hw,
                                        "Lazy student have done this work")

    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    opp_teacher.check_homework(result_5)
    print(Teacher.homework_done)
    print((good_student, "I have done this hw too") in
          Teacher.homework_done[docs_hw])
    Teacher.reset_results(oop_hw)
    print(Teacher.homework_done)
