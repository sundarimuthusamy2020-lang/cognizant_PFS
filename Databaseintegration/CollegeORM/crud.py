"""
N+1 Problem Analysis

Without joinedload():
1 query fetches enrollments
N queries fetch students
N queries fetch courses

For 4 enrollments:
1 + 4 + 4 = 9 queries

With joinedload():
Only 1 SQL query is executed.

Performance improves significantly by reducing
database round-trips.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from datetime import date

from models import (
    Department,
    Student,
    Course,
    Enrollment
)

engine = create_engine(
    "mysql+pymysql://root:Pavi_10@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# ==================================
# INSERT DEPARTMENTS
# ==================================

d1 = Department(
    dept_name="Computer Science",
    hod_name="Dr. Kumar",
    budget=1000000
)

d2 = Department(
    dept_name="Mechanical",
    hod_name="Dr. Singh",
    budget=800000
)

d3 = Department(
    dept_name="Electronics",
    hod_name="Dr. Rao",
    budget=900000
)

session.add_all([d1, d2, d3])
session.commit()


# ==================================
# INSERT STUDENTS
# ==================================

s1 = Student(
    first_name="Rahul",
    last_name="Sharma",
    email="rahul@gmail.com",
    date_of_birth=date(2003, 5, 10),
    department=d1,
    enrollment_year=2022
)

s2 = Student(
    first_name="Priya",
    last_name="Kumar",
    email="priya@gmail.com",
    date_of_birth=date(2003, 7, 12),
    department=d1,
    enrollment_year=2022
)

s3 = Student(
    first_name="Amit",
    last_name="Verma",
    email="amit@gmail.com",
    date_of_birth=date(2002, 8, 20),
    department=d2,
    enrollment_year=2021
)

s4 = Student(
    first_name="Anjali",
    last_name="Reddy",
    email="anjali@gmail.com",
    date_of_birth=date(2003, 2, 15),
    department=d3,
    enrollment_year=2022
)

s5 = Student(
    first_name="Kiran",
    last_name="Patel",
    email="kiran@gmail.com",
    date_of_birth=date(2002, 11, 5),
    department=d1,
    enrollment_year=2021
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()


# ==================================
# INSERT COURSES
# ==================================

c1 = Course(
    course_name="Database Systems",
    course_code="CS101",
    credits=4,
    department=d1
)

c2 = Course(
    course_name="Java Programming",
    course_code="CS102",
    credits=3,
    department=d1
)

c3 = Course(
    course_name="Operating Systems",
    course_code="CS103",
    credits=4,
    department=d1
)

session.add_all([c1, c2, c3])
session.commit()


# ==================================
# INSERT ENROLLMENTS
# ==================================

e1 = Enrollment(
    student=s1,
    course=c1,
    enrollment_date=date.today(),
    grade="A"
)

e2 = Enrollment(
    student=s1,
    course=c2,
    enrollment_date=date.today(),
    grade="B"
)

e3 = Enrollment(
    student=s2,
    course=c1,
    enrollment_date=date.today(),
    grade="A"
)

e4 = Enrollment(
    student=s3,
    course=c3,
    enrollment_date=date.today(),
    grade="C"
)

session.add_all([e1, e2, e3, e4])
session.commit()


# ==================================
# READ
# ==================================

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name
        == "Computer Science"
    )
    .all()
)

print("\nComputer Science Students\n")

for s in students:
    print(
        s.first_name,
        s.last_name
    )


# ==================================
# N+1 QUERY
# ==================================

print("\nN+1 Query\n")

enrollments = (
    session.query(Enrollment)
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        e.course.course_name
    )


# ==================================
# FIX USING JOINEDLOAD
# ==================================

print("\nUsing joinedload\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(
            Enrollment.student
        ),
        joinedload(
            Enrollment.course
        )
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        e.course.course_name
    )


# ==================================
# UPDATE
# ==================================

student = (
    session.query(Student)
    .filter(
        Student.email
        == "rahul@gmail.com"
    )
    .first()
)

if student:
    student.enrollment_year = 2023
    session.commit()
    print("Student Updated")


# ==================================
# DELETE
# ==================================

enrollment = (
    session.query(Enrollment)
    .first()
)

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("Enrollment Deleted")


session.close()