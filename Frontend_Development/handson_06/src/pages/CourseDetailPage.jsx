import { useParams, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

import courses from "../data/courses";
import { enroll } from "../redux/enrollmentSlice";

function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return (
      <div className="container">
        <h2 className="title">Course Not Found</h2>
      </div>
    );
  }

  const handleEnroll = () => {
    dispatch(enroll(course));
    alert("Course Enrolled Successfully!");
    navigate("/profile");
  };

  return (
    <div className="container">
      <div className="card">
        <h2>{course.title}</h2>

        <p>{course.description}</p>

        <button onClick={handleEnroll}>
          Enroll Now
        </button>
      </div>
    </div>
  );
}

export default CourseDetailPage;