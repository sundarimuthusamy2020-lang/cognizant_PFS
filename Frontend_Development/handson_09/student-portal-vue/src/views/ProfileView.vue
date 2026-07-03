<template>

<section>

<h1>Student Profile</h1>

<div class="summary">

<h2>Total Credits</h2>

<h1>{{ store.totalCredits }}</h1>

</div>

<h2>Enrolled Courses</h2>

<div
v-if="store.enrolledCourses.length"
class="courses"
>

<div
class="course"
v-for="course in store.enrolledCourses"
:key="course.id"
>

<h3>{{ course.name }}</h3>

<p>{{ course.code }}</p>

<p>{{ course.credits }} Credits</p>

<button
@click="store.unenroll(course.id)"
>

Remove

</button>

</div>

</div>

<p v-else>

No courses enrolled yet.

</p>

</section>

</template>

<script setup>

import { useEnrollmentStore }

from "../stores/enrollment";

const store=useEnrollmentStore();

</script>

<style scoped>

.summary{

background:#2563eb;

color:white;

padding:30px;

text-align:center;

border-radius:15px;

margin-bottom:30px;

}

.courses{

display:grid;

grid-template-columns:

repeat(auto-fit,minmax(250px,1fr));

gap:20px;

}

.course{

background:white;

padding:20px;

border-radius:12px;

box-shadow:0 4px 12px rgba(0,0,0,.15);

}

button{

margin-top:15px;

padding:10px 15px;

background:#dc2626;

color:white;

border:none;

border-radius:6px;

cursor:pointer;

}

button:hover{

background:#b91c1c;

}

</style>