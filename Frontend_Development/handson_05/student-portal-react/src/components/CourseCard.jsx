function CourseCard({
  id,
  name,
  code,
  credits,
  grade,
  onEnroll,
  isEnrolled,
}) {
  return (
    <div className="card">
      <div className="card-header">
        <h2>📘 {name}</h2>

        <span className="grade">
          Grade: <strong>{grade}</strong>
        </span>
      </div>

      <div className="course-info">
        <p>
          <strong>Course Code:</strong> {code}
        </p>

        <p>
          <strong>Credits:</strong> {credits}
        </p>
      </div>

      <button
        className={isEnrolled ? "btn enrolled" : "btn"}
        disabled={isEnrolled}
        onClick={() => onEnroll(id)}
      >
        {isEnrolled ? "✔ Enrolled" : "Enroll"}
      </button>
    </div>
  );
}

export default CourseCard;