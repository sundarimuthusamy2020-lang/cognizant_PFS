<template>
  <header class="header">
    <div>
      <h1>🎓 Student Portal</h1>
      <p>Manage your courses easily</p>
    </div>

    <div class="badge">
      Enrolled: {{ store.enrolledCourses.length }}
    </div>
  </header>
</template>

<script setup>
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();
</script>

<style scoped>
.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:#2563eb;
    color:white;
    padding:20px 40px;
}

.header h1{
    margin:0;
}

.header p{
    margin-top:5px;
    opacity:.8;
}

.badge{
    background:white;
    color:#2563eb;
    padding:10px 20px;
    border-radius:25px;
    font-weight:bold;
}
</style>