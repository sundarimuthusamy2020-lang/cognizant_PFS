<template>
  <h1>Available Courses</h1>

  <input
    v-model="searchTerm"
    placeholder="🔍 Search courses..."
    class="search"
  />

  <div class="grid">
    <div
      v-for="course in filteredCourses"
      :key="course.id"
    >
      <CourseCard
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
        @enroll="store.enroll(course)"
      />

      <RouterLink
        class="details"
        :to="'/courses/' + course.id"
      >
        View Details →
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import CourseCard from "../components/CourseCard.vue";
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();

const courses = ref([]);
const searchTerm = ref("");

onMounted(() => {
  courses.value = [
    {
      id: 1,
      name: "Web Development",
      code: "CS101",
      credits: 4,
      grade: "A",
    },
    {
      id: 2,
      name: "Java Programming",
      code: "CS102",
      credits: 3,
      grade: "A+",
    },
    {
      id: 3,
      name: "Python",
      code: "CS103",
      credits: 4,
      grade: "B+",
    },
    {
      id: 4,
      name: "Database",
      code: "CS104",
      credits: 3,
      grade: "A",
    },
    {
      id: 5,
      name: "Cloud Computing",
      code: "CS105",
      credits: 4,
      grade: "A+",
    },
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.search {
  width: 100%;
  padding: 15px;
  font-size: 16px;
  margin-bottom: 25px;
  border-radius: 10px;
  border: 1px solid #ddd;
}

.details {
  display: block;
  text-align: center;
  margin-top: 10px;
  text-decoration: none;
  font-weight: bold;
  color: #2563eb;
}
</style>