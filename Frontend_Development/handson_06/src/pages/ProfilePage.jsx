import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div className="container">
      <h2 className="title">My Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p className="empty">
          📚 You haven't enrolled in any courses yet.
        </p>
      ) : (
        enrolledCourses.map((course) => (
          <div className="card" key={course.id}>
            <h3>{course.title}</h3>

            <p>{course.description}</p>

            <button
              className="remove-btn"
              onClick={() => dispatch(unenroll(course.id))}
            >
              Remove Course
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;