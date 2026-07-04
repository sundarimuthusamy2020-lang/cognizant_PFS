import apiClient from "./apiClient";

export const getAllCourses = () => apiClient.get("/posts");

export const getCourseById = (id) =>
  apiClient.get(`/posts/${id}`);

export const enrollStudent = (studentId, courseId) =>
  apiClient.post("/posts", {
    studentId,
    courseId,
  });