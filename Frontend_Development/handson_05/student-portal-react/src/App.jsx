import { useEffect, useState } from "react";
import "./App.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        const courseNames = [
          "Frontend Development",
          "React Development",
          "Java Programming",
          "Database Systems",
          "Cloud Computing",
        ];

        const grades = ["A", "A+", "B+", "A", "A+"];

        const mappedCourses = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: courseNames[index],
          code: `CSE-${101 + index}`,
          credits: 4,
          grade: grades[index],
        }));

        setCourses(mappedCourses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchCourses();
  }, []);

  // Runs only when the courses array changes.
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  const handleEnroll = (id) => {
    if (!enrolledCourses.includes(id)) {
      setEnrolledCourses([...enrolledCourses, id]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main className="container">
        <div className="search-container">
          <input
            className="search-box"
            type="text"
            placeholder="🔍 Search courses..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {loading && <h2 className="loading">Loading Courses...</h2>}

        {error && <h2 className="error">{error}</h2>}

        {!loading && !error && (
          <>
            <div className="course-grid">
              {filteredCourses.length > 0 ? (
                filteredCourses.map((course) => (
                  <CourseCard
                    key={course.id}
                    {...course}
                    isEnrolled={enrolledCourses.includes(course.id)}
                    onEnroll={handleEnroll}
                  />
                ))
              ) : (
                <div className="no-course">
                  No courses found.
                </div>
              )}
            </div>

            <StudentProfile />
          </>
        )}
      </main>

      <Footer />
    </>
  );
}

export default App;