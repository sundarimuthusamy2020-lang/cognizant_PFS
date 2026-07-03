<template>

  <Header />

  <nav aria-label="Main navigation">

    <RouterLink to="/">Home</RouterLink>

    <RouterLink to="/courses">Courses</RouterLink>

    <RouterLink to="/profile">Profile</RouterLink>

  </nav>

  <div class="container">

    <RouterView />

  </div>

</template>

<script setup>
import Header from "./components/Header.vue";
</script>

<style>

body{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f4f6fb;
    color:#222;
}

.container{
    width:90%;
    margin:auto;
    margin-top:30px;
}

nav{

display:flex;
justify-content:center;
gap:30px;
padding:20px;
background:white;
box-shadow:0 3px 10px rgba(0,0,0,.1);

}

nav a{

text-decoration:none;
font-weight:bold;
color:#333;

}

.router-link-active{

color:#2563eb;

}

/* Accessibility */

a:focus,
button:focus,
input:focus{

outline:3px solid #2563eb;
outline-offset:3px;

}

</style>