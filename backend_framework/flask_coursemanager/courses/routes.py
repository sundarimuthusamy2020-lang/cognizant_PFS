from flask import Blueprint, jsonify, request

from extensions import db

from courses.models import (
    Course,
    Student,
    Enrollment
)

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


def make_error_response(message, status_code):
    return jsonify({
        "status": "error",
        "message": message
    }), status_code


# ==================================================
# STEP 52
# GET ALL COURSES
# ==================================================
@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return make_response_json(
        [course.to_dict() for course in courses]
    )


# ==================================================
# STEP 55
# GET COURSE BY ID
# ==================================================
@courses_bp.route("/<int:id>/", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return make_response_json(
        course.to_dict()
    )


# ==================================================
# STEP 54
# CREATE COURSE
# ==================================================
@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if data is None:
        return make_error_response(
            "Request body must be JSON",
            400
        )

    required_fields = [
        "name",
        "code",
        "credits"
    ]

    for field in required_fields:
        if field not in data:
            return make_error_response(
                f"{field} is required",
                400
            )

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data.get("department_id")
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(
        course.to_dict(),
        201
    )


# ==================================================
# STEP 55
# UPDATE COURSE
# ==================================================
@courses_bp.route("/<int:id>/", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    if data is None:
        return make_error_response(
            "Request body must be JSON",
            400
        )

    course.name = data.get(
        "name",
        course.name
    )

    course.code = data.get(
        "code",
        course.code
    )

    course.credits = data.get(
        "credits",
        course.credits
    )

    course.department_id = data.get(
        "department_id",
        course.department_id
    )

    db.session.commit()

    return make_response_json(
        course.to_dict()
    )


# ==================================================
# STEP 55
# DELETE COURSE
# ==================================================
@courses_bp.route("/<int:id>/", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return make_response_json({
        "message": "Course deleted successfully"
    })


# ==================================================
# STEP 56
# GET STUDENTS ENROLLED IN A COURSE
# ==================================================
@courses_bp.route(
    "/<int:id>/students/",
    methods=["GET"]
)
def get_course_students(id):

    course = Course.query.get_or_404(id)

    students = (
        Student.query
        .join(Enrollment)
        .filter(
            Enrollment.course_id == id
        )
        .all()
    )

    return make_response_json({
        "course": course.name,
        "students": [
            student.to_dict()
            for student in students
        ]
    })