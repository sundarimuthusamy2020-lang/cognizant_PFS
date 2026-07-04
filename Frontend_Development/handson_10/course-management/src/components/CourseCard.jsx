function CourseCard({ course }) {
  return (
    <div className="card">
      <h2>{course.title}</h2>

      <p>{course.body}</p>

      <button>Enroll</button>
    </div>
  );
}

export default CourseCard;