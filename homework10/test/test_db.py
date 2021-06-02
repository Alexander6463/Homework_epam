import os

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from homework10.hw.create_table import Homework, Student, Teacher

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "main.db")


def create_connection():
    engine = create_engine('sqlite:///'+db_path)
    Session = sessionmaker(bind=engine)
    return engine, Session()


def close_connection(session):
    session.close()


def test_created_tables():
    engine, session = create_connection()
    inspector = inspect(engine)
    assert inspector.get_table_names() == ['Result', 'homeworks',
                                           'students', 'teachers']
    close_connection(session)


def test_info_student():
    engine, session = create_connection()
    assert session.query(Student.first_name).scalar() == 'Nikolay'
    assert session.query(Student.last_name).scalar() == 'Fedorov'
    close_connection(session)


def test_info_teacher():
    engine, session = create_connection()
    assert session.query(Teacher.first_name).\
        filter(Teacher.first_name == 'Miya').scalar() == 'Miya'
    assert session.query(Teacher.last_name).\
        filter(Teacher.last_name == 'Gonzalez').scalar() == 'Gonzalez'
    close_connection(session)


def test_info_homework():
    engine, session = create_connection()
    assert session.query(Homework.text).scalar() == 'first homework'
    close_connection(session)
