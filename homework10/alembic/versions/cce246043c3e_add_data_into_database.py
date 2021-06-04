"""add data into database

Revision ID: cce246043c3e
Revises: 71405c3773d1
Create Date: 2021-06-04 21:22:14.862385

"""
from datetime import datetime

from alembic import op
from sqlalchemy import Date, Integer, String
from sqlalchemy.sql import column, table

# revision identifiers, used by Alembic.
revision = 'cce246043c3e'
down_revision = '71405c3773d1'
branch_labels = None
depends_on = None


def upgrade():
    students_table = table('students',
                           column('id', Integer),
                           column('first_name', String),
                           column('last_name', String)
                           )
    op.bulk_insert(students_table,
                   [
                       {'id': 1, 'first_name': 'Nikolay',
                        'last_name': 'Fedorov'}
                   ]
                   )

    teacher_table = table('teachers',
                          column('id', Integer),
                          column('first_name', String),
                          column('last_name', String)
                          )
    op.bulk_insert(teacher_table,
                   [
                       {"id": 1, "first_name": "Nina",
                        "last_name": "Ivanova"},
                       {"id": 2, 'first_name': 'Miya',
                        'last_name': 'Gonzalez'}
                   ]
                   )
    homework_table = table('homeworks',
                           column('id', Integer),
                           column('text', String),
                           column('deadline', Date),
                           column('created', Date)
                           )
    op.bulk_insert(homework_table,
                   [
                       {'id': 1, 'text': 'first homework',
                        'created': datetime.now(),
                        'deadline': datetime(year=2021, month=6, day=5)}
                   ])
    result_table = table('Result',
                         column('id', Integer),
                         column('homework_id', Integer),
                         column('teacher_id', Integer),
                         column('student_id', Integer),
                         column('solve', String),
                         column('created', Date)
                         )
    op.bulk_insert(result_table,
                   [
                       {'id': 1, 'homework_id': 1, 'teacher_id': 1,
                        'student_id': 1, 'solve': 'too bad',
                        'created': datetime.now()},
                       {'id': 2, 'homework_id': 1, 'teacher_id': 2,
                        'student_id': 1, 'solve': 'good work',
                        'created': datetime.now()},
                       {'id': 3, 'homework_id': 1, 'teacher_id': 2,
                        'student_id': 1, 'solve': 'excellent',
                        'created': datetime.now()},
                   ])


def downgrade():
    op.execute("delete from students")
    op.execute("delete from teachers")
    op.execute("delete from homeworks")
    op.execute("delete from Result")
