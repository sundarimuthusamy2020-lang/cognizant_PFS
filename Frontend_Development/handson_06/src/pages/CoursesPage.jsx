import { Link } from "react-router-dom";
import courses from "../data/courses";

function CoursesPage() {
  return (
    <div className="container">
      <h2 className="title">Available Courses</h2>

      {courses.map((course) => (
        <div className="card" key={course.id}>
          <h3>{course.title}</h3>

          <p>{course.description}</p>

          <Link
            className="details-link"
            to={`/courses/${course.id}`}
          >
            View Details →
          </Link>
        </div>
      ))}
    </div>
  );
}

export default CoursesPage;