from fastapi import APIRouter, Depends

from auth import get_current_user

router = APIRouter(
    prefix="/api/v1/courses",
    tags=["Courses"]
)

courses = []


@router.get("/")
def get_courses():
    return courses


@router.post("/")
def create_course(
    course: dict,
    current_user=Depends(get_current_user)
):
    courses.append(course)
    return course


@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    current_user=Depends(get_current_user)
):

    return {
        "message": f"Course {course_id} deleted."
    }