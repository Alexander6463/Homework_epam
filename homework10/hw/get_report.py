import csv

from create_table import Homework, ResultHomework, Student, Teacher, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

res = session.query(ResultHomework, Student, Teacher, Homework)\
    .filter(ResultHomework.student_id == Student.id)\
    .filter(ResultHomework.teacher_id == Teacher.id)\
    .filter(ResultHomework.homework_id == Homework.id)
session.close()

with open('report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Student first name', 'Result created',
                     'Teacher first name'])
    for result, student, teacher, homework in res:
        writer.writerow([student.first_name, result.created,
                         teacher.first_name])
