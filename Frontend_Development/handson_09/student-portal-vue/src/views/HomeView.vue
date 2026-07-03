<template>
  <section class="hero">
    <h1>Welcome to Student Portal</h1>

    <h2>Your Learning Journey Starts Here</h2>

    <p>
      Browse available courses, enroll, and monitor your academic progress.
    </p>

    <RouterLink to="/courses">
      <button>Explore Courses</button>
    </RouterLink>
  </section>
</template>

<script setup>
</script>

<style scoped>

.hero{
    text-align:center;
    background:white;
    padding:70px 30px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
}

.hero h1{
    color:#2563eb;
}

.hero h2{
    color:#444;
}

button{

margin-top:20px;
padding:15px 30px;
background:#2563eb;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
font-size:16px;

}

button:hover{

background:#1d4ed8;

}

button:focus{

outline:3px solid #2563eb;

}

</style>