import { useSelector } from "react-redux";

function HomePage() {

  const enrolledCourses = useSelector(
    state => state.enrollment.enrolledCourses
  );

  return (

    <div className="container">

      <div className="hero">

        <h1>🎓 React Student Portal</h1>

        <p>
          Learn new skills, enroll in courses and
          manage your learning journey.
        </p>

      </div>

      <div className="stats">

        <div className="stat-card">

          <h3>Available Courses</h3>

          <h1>3</h1>

        </div>

        <div className="stat-card">

          <h3>Enrolled Courses</h3>

          <h1>{enrolledCourses.length}</h1>

        </div>

      </div>

    </div>

  );

}

export default HomePage;