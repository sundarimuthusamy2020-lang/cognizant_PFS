from typing import List, Optional

from fastapi import (
    FastAPI,
    Depends,
    status,
    Response,
    BackgroundTasks,
    Request
)

from fastapi.responses import JSONResponse

from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db
from models import Base, Course, Student, Enrollment

from schemas import (
    CourseCreate,
    CourseReplace,
    CourseUpdate,
    CourseResponse,
    CourseListResponse,
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
)

# -------------------------------------------------------
# API Versioning
# URL Versioning : /api/v1/
# Alternative:
# Header Versioning
# Accept: application/vnd.api+json;version=1
# -------------------------------------------------------

app = FastAPI(
    title="Course Management API",
    description="""
Course Management API using FastAPI

Features
• Async SQLAlchemy
• CRUD Operations
• Background Tasks
• Pagination
• Search
• OpenAPI Documentation
""",
    version="2.0.0",
    contact={
        "name": "Digital Nurture Team",
        "email": "support@example.com"
    }
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


def error_response(message: str):
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "NOT_FOUND",
                "message": message,
                "field": None
            }
        }
    )


@app.get("/")
async def root():
    return {"message": "API Running"}

#########################################################
# COURSES
#########################################################

@app.post(
    "/api/v1/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Course",
    response_description="Created Course"
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(**course.model_dump())

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"

    return new_course


@app.get(
    "/api/v1/courses/",
    tags=["Courses"],
    response_model=CourseListResponse,
    summary="List Courses"
)
async def get_courses(
    request: Request,
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    total = await db.scalar(
        select(func.count()).select_from(query.subquery())
    )

    offset = (page - 1) * page_size

    query = query.offset(offset).limit(page_size)

    result = await db.execute(query)

    courses = result.scalars().all()

    next_url = None
    previous_url = None

    if offset + page_size < total:
        next_url = str(
            request.url.include_query_params(
                page=page + 1,
                page_size=page_size
            )
        )

    if page > 1:
        previous_url = str(
            request.url.include_query_params(
                page=page - 1,
                page_size=page_size
            )
        )

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }


@app.get(
    "/api/v1/courses/{id}",
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
        return error_response(
            f"Course with id {id} does not exist"
        )

    return course


@app.put(
    "/api/v1/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def replace_course(
    id: int,
    course: CourseReplace,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    obj = result.scalar_one_or_none()

    if not obj:
        return error_response(
            f"Course with id {id} does not exist"
        )

    obj.name = course.name
    obj.code = course.code
    obj.credits = course.credits
    obj.department_id = course.department_id

    await db.commit()

    await db.refresh(obj)

    return obj


@app.patch(
    "/api/v1/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse,
    summary="Partial Update Course"
)
async def patch_course(
    id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == id)
    )

    obj = result.scalar_one_or_none()

    if not obj:
        return error_response(
            f"Course with id {id} does not exist"
        )

    updates = course.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(obj, key, value)

    await db.commit()

    await db.refresh(obj)

    return obj


@app.delete(
    "/api/v1/courses/{id}",
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
        return error_response(
            f"Course with id {id} does not exist"
        )

    await db.delete(course)

    await db.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
# ==========================================================
# STUDENTS
# ==========================================================

@app.post(
    "/api/v1/students/",
    tags=["Students"],
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Student"
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    obj = Student(**student.model_dump())

    db.add(obj)

    await db.commit()
    await db.refresh(obj)

    response.headers["Location"] = f"/api/v1/students/{obj.id}"

    return obj


@app.get(
    "/api/v1/students/{id}",
    tags=["Students"],
    response_model=StudentResponse,
    summary="Get Student"
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
        return error_response(
            f"Student with id {id} does not exist"
        )

    return student


@app.put(
    "/api/v1/students/{id}",
    tags=["Students"],
    response_model=StudentResponse,
    summary="Replace Student"
)
async def replace_student(
    id: int,
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == id)
    )

    obj = result.scalar_one_or_none()

    if not obj:
        return error_response(
            f"Student with id {id} does not exist"
        )

    obj.name = student.name
    obj.email = student.email

    await db.commit()
    await db.refresh(obj)

    return obj


@app.patch(
    "/api/v1/students/{id}",
    tags=["Students"],
    response_model=StudentResponse,
    summary="Partially Update Student"
)
async def patch_student(
    id: int,
    student: StudentUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == id)
    )

    obj = result.scalar_one_or_none()

    if not obj:
        return error_response(
            f"Student with id {id} does not exist"
        )

    updates = student.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(obj, key, value)

    await db.commit()
    await db.refresh(obj)

    return obj


@app.delete(
    "/api/v1/students/{id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == id)
    )

    obj = result.scalar_one_or_none()

    if not obj:
        return error_response(
            f"Student with id {id} does not exist"
        )

    await db.delete(obj)

    await db.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


# ==========================================================
# ENROLLMENTS
# ==========================================================

@app.post(
    "/api/v1/enrollments/",
    tags=["Enrollments"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Enrollment"
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    response: Response,
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
        return error_response(
            f"Student with id {enrollment.student_id} does not exist"
        )

    obj = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(obj)

    await db.commit()
    await db.refresh(obj)

    response.headers["Location"] = f"/api/v1/enrollments/{obj.id}"

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return obj


@app.get(
    "/api/v1/courses/{id}/students/",
    tags=["Enrollments"],
    response_model=List[StudentResponse],
    summary="Students Enrolled in Course"
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


@app.delete(
    "/api/v1/enrollments/{id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Enrollment"
)
async def delete_enrollment(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == id
        )
    )

    enrollment = result.scalar_one_or_none()

    if not enrollment:
        return error_response(
            f"Enrollment with id {id} does not exist"
        )

    await db.delete(enrollment)

    await db.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )