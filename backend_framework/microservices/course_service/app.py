from flask import Flask, request, jsonify
from database import db
from models import Course

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify({
        "id": course.id,
        "name": course.name,
        "department": course.department
    })


@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Request must be JSON"}), 400

    course = Course(
        name=data["name"],
        department=data["department"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({"message": "Course Added"}), 201


if __name__ == "__main__":
    app.run(port=5001, debug=True)