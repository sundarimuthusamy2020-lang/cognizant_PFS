<template>

<header class="header">

<div>

<h1>🎓 Student Portal</h1>

<p>Manage Your Courses</p>

</div>

<div class="count">

Enrolled:
{{ store.enrolledCourses.length }}

</div>

</header>

</template>

<script setup>

import { useEnrollmentStore } from "../stores/enrollment";

const store=useEnrollmentStore();

</script>

<style scoped>

.header{

display:flex;
justify-content:space-between;
align-items:center;

padding:20px 40px;

background:#2563eb;

color:white;

}

.header h1{

margin:0;

}

.count{

background:white;
color:#2563eb;
padding:10px 20px;
border-radius:30px;
font-weight:bold;

}

</style>