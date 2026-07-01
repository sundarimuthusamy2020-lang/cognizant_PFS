import { useState } from "react";

function StudentProfile() {
  const [student, setStudent] = useState({
    name: "",
    email: "",
    semester: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setStudent((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div className="profile-card">
      <h2>👤 Student Profile</h2>

      <div className="profile-form">
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={student.name}
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={student.email}
          onChange={handleChange}
        />

        <input
          type="text"
          name="semester"
          placeholder="Semester"
          value={student.semester}
          onChange={handleChange}
        />
      </div>

      <div className="profile-preview">
        <h3>Welcome {student.name || "Student"} 👋</h3>

        <p>
          <strong>Email:</strong>{" "}
          {student.email || "Not Provided"}
        </p>

        <p>
          <strong>Semester:</strong>{" "}
          {student.semester || "-"}
        </p>
      </div>
    </div>
  );
}

export default StudentProfile;