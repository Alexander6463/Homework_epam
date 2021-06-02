from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///main.db')
base = declarative_base()


class Student(base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Student first_name={self.first_name}, ' \
               f'last_name={self.last_name}'


class Teacher(base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Teacher first_name={self.first_name}, ' \
               f'last_name={self.last_name}'


class Homework(base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    deadline = Column(DateTime)
    created = Column(DateTime)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Homework text={self.text}, deadline = {self.deadline}, ' \
               f'created = {self.created}'


class ResultHomework(base):
    __tablename__ = 'Result'
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homeworks.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    solve = Column(String)
    created = Column(DateTime)

    def __repr__(self):
        return f'ResultHomework homework={self.homework_id}, ' \
               f'teacher={self.teacher_id}, student={self.student_id}, ' \
               f'solve={self.solve}, created={self.created}'


if __name__ == '__main__':
    base.metadata.create_all(engine)
