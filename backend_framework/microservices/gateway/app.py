from flask import Flask, request, Response
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://localhost:5001"
STUDENT_SERVICE = "http://localhost:5002"


@app.route("/api/courses", methods=["GET", "POST"])
@app.route("/api/courses/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def course_proxy(path=""):

    url = f"{COURSE_SERVICE}/api/courses"

    if path:
        url += f"/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True)
    )

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get(
            "Content-Type",
            "application/json"
        )
    )


@app.route("/api/students", methods=["GET", "POST"])
@app.route("/api/students/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def student_proxy(path=""):

    url = f"{STUDENT_SERVICE}/api/students"

    if path:
        url += f"/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True)
    )

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get(
            "Content-Type",
            "application/json"
        )
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)