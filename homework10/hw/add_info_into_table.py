from datetime import datetime

from create_table import Homework, ResultHomework, Student, Teacher, engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all([Student(first_name='Nikolay', last_name='Fedorov'),
                     Teacher(first_name='Nina', last_name='Ivanova'),
                     Teacher(first_name='Miya', last_name='Gonzalez'),
                     Homework(text='first homework', created=datetime.now(),
                              deadline=datetime(year=2021, month=6, day=5))])
    session.commit()
    session.add_all([ResultHomework(homework_id=1, teacher_id=1,
                                    student_id=1, solve='too bad',
                                    created=datetime.now()),
                     ResultHomework(homework_id=1, teacher_id=2,
                                    student_id=1, solve='good work',
                                    created=datetime.now()),
                     ResultHomework(homework_id=1, teacher_id=2,
                                    student_id=1, solve='excellent',
                                    created=datetime.now())])
    session.commit()
    session.close()
