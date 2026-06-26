from pydantic import BaseModel
from typing import List, Optional

# COURSE

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True


# STUDENT

class StudentCreate(BaseModel):
    name: str
    email: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# ENROLLMENT

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True

class CourseReplace(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class ErrorResponse(BaseModel):
    error: dict

class CourseListResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[CourseResponse]