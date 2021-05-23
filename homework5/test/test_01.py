import datetime

from homework5.hw.task01 import Homework, Student, Teacher


def test_names_in_class_teacher():
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_names_in_class_student():
    student = Student("Roman", "Petrov")
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_attrs_class_homework_and_method_create_homework():
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert expired_homework.deadline == datetime.timedelta(0)
    assert expired_homework.text == "Learn functions"
    assert isinstance(expired_homework, Homework)


def test_method_do_homework_from_class_student():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(days=5)
    # 5 days, 0:00:00
    assert student.do_homework(oop_homework) is oop_homework
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert student.do_homework(expired_homework) is None
