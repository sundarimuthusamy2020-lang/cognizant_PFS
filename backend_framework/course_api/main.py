from typing import List

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    Response,
    BackgroundTasks
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db
from models import Base, Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse
)

# -------------------------
# OpenAPI Customization
# -------------------------
app = FastAPI(
    title="Course Management API",
    description="""
    FastAPI application for managing Courses,
    Students and Enrollments.

    Features:
    - CRUD Operations
    - Async SQLAlchemy
    - Background Tasks
    - OpenAPI Documentation
    """,
    version="2.0.0",
)


# -------------------------
# Startup
# -------------------------
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# -------------------------
# Background Task
# -------------------------
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# -------------------------
# Root Endpoint
# -------------------------
@app.get("/")
async def root():
    return {"message": "API running"}


# ==================================================
# COURSES
# ==================================================

@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new course",
    response_description="The newly created course"
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(**course.model_dump())

    db.add(new_course)

    await db.commit()
    await db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=List[CourseResponse],
    summary="Get all courses"
)
async def get_courses(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Course))

    return result.scalars().all()


@app.get(
    "/api/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def get_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def update_course(
    id: int,
    data: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course


@app.delete(
    "/api/courses/{id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    course = result.scalar_one_or_none()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


# ==================================================
# STUDENTS
# ==================================================

@app.post(
    "/api/students/",
    tags=["Students"],
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):
    obj = Student(**student.model_dump())

    db.add(obj)

    await db.commit()
    await db.refresh(obj)

    return obj


@app.get(
    "/api/students/{id}",
    tags=["Students"],
    response_model=StudentResponse
)
async def get_student(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == id)
    )

    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ==================================================
# ENROLLMENTS
# ==================================================

@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Enroll a student in a course"
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(
            Student.id == enrollment.student_id
        )
    )

    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    obj = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(obj)

    await db.commit()
    await db.refresh(obj)

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return obj


@app.get(
    "/api/courses/{id}/students/",
    tags=["Enrollments"],
    response_model=List[StudentResponse]
)
async def get_course_students(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student)
        .join(
            Enrollment,
            Student.id == Enrollment.student_id
        )
        .where(
            Enrollment.course_id == id
        )
    )

    return result.scalars().all()