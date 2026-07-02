<template>

<div class="detail">

<h1>Course {{ id }}</h1>

<p>

This page displays the selected course details.

</p>

<button @click="enroll">

Enroll Now

</button>

</div>

</template>

<style scoped>

.detail{

background:white;
padding:50px;
text-align:center;
border-radius:15px;
box-shadow:0 5px 15px rgba(0,0,0,.15);

}

button{

margin-top:20px;
padding:15px 35px;
background:#16a34a;
color:white;
border:none;
border-radius:8px;
cursor:pointer;

}

button:hover{

background:#15803d;

}

</style>