import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header() {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <nav
      style={{
        display: "flex",
        gap: "20px",
        padding: "15px",
        backgroundColor: "#1976d2",
      }}
    >
      <Link style={{ color: "white" }} to="/">
        Home
      </Link>

      <Link style={{ color: "white" }} to="/courses">
        Courses
      </Link>

      <Link style={{ color: "white" }} to="/profile">
        Profile ({enrolledCourses.length})
      </Link>
    </nav>
  );
}

export default Header;