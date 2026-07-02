<template>
  <h1>My Profile</h1>

  <div class="summary">
    <h2>Total Credits</h2>
    <h1>{{ store.totalCredits }}</h1>
  </div>

  <div class="courses">
    <div
      class="course"
      v-for="course in store.enrolledCourses"
      :key="course.id"
    >
      <h3>{{ course.name }}</h3>
      <p>{{ course.code }}</p>
      <p>{{ course.credits }} Credits</p>
    </div>

    <p v-if="store.enrolledCourses.length === 0">
      No courses enrolled yet.
    </p>
  </div>
</template>

<script setup>
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();
</script>

<style scoped>
.summary {
  background: #2563eb;
  color: white;
  padding: 30px;
  border-radius: 15px;
  margin-bottom: 30px;
  text-align: center;
}

.courses {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.course {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
}
</style>