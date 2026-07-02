<template>

<Header/>

<nav>

<RouterLink to="/">Home</RouterLink>

<RouterLink to="/courses">Courses</RouterLink>

<RouterLink to="/profile">Profile</RouterLink>

</nav>

<div class="container">

<RouterView/>

</div>

</template>

<script setup>
import Header from "./components/Header.vue";
</script>

<style>

body{
    margin:0;
    background:#f4f6fb;
    font-family:Arial, Helvetica, sans-serif;
}

nav{
    display:flex;
    justify-content:center;
    gap:30px;
    background:white;
    padding:18px;
    box-shadow:0 3px 8px rgba(0,0,0,.1);
}

nav a{
    text-decoration:none;
    color:#444;
    font-weight:bold;
}

.router-link-active{
    color:#2563eb;
}

.container{
    width:90%;
    margin:auto;
    margin-top:30px;
}

</style>