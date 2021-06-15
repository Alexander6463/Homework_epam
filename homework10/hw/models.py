from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///main.db')
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Student first_name={self.first_name}, ' \
               f'last_name={self.last_name}'


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Teacher first_name={self.first_name}, ' \
               f'last_name={self.last_name}'


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    result = relationship('ResultHomework')

    def __repr__(self):
        return f'Homework text={self.text}, deadline = {self.deadline}, ' \
               f'created = {self.created}'


class ResultHomework(Base):
    __tablename__ = 'Result'
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homeworks.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    solve = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'ResultHomework homework={self.homework_id}, ' \
               f'teacher={self.teacher_id}, student={self.student_id}, ' \
               f'solve={self.solve}, created={self.created}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
