import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enroll = (course) => {
    const exists = enrolledCourses.find((c) => c.id === course.id);

    if (!exists) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const remove = (id) => {
    setEnrolledCourses(
      enrolledCourses.filter((course) => course.id !== id)
    );
  };

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enroll,
        remove,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}