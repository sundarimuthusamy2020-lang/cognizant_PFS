<template>

<div class="hero">

<h1>🎓 Welcome to Student Portal</h1>

<p>

Browse courses, enroll, and monitor your academic progress.

</p>

<RouterLink to="/courses">

<button>

Explore Courses

</button>

</RouterLink>

</div>

</template>

<style scoped>

.hero{

text-align:center;
padding:80px;
background:white;
border-radius:20px;
box-shadow:0 5px 15px rgba(0,0,0,.1);

}

button{

padding:15px 30px;
font-size:18px;
background:#2563eb;
color:white;
border:none;
border-radius:10px;
cursor:pointer;

}

button:hover{

background:#1d4ed8;

}

</style>