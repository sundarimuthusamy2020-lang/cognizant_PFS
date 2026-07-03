<template>

<section class="detail">

<h1>Course Details</h1>

<h2>{{ course.name }}</h2>

<p>

<strong>Course Code:</strong>

{{ course.code }}

</p>

<p>

<strong>Credits:</strong>

{{ course.credits }}

</p>

<p>

<strong>Grade:</strong>

{{ course.grade }}

</p>

<button @click="enroll">

Enroll

</button>

</section>

</template>

<script setup>

import { computed } from "vue";

import { useRoute,useRouter } from "vue-router";

import { useEnrollmentStore } from "../stores/enrollment";

const route=useRoute();

const router=useRouter();

const store=useEnrollmentStore();

const courses=[

{
id:1,
name:"Web Development",
code:"CS101",
credits:4,
grade:"A"
},

{
id:2,
name:"Java Programming",
code:"CS102",
credits:3,
grade:"A+"
},

{
id:3,
name:"Python Programming",
code:"CS103",
credits:4,
grade:"A"
},

{
id:4,
name:"Database Management",
code:"CS104",
credits:3,
grade:"B+"
},

{
id:5,
name:"Cloud Computing",
code:"CS105",
credits:4,
grade:"A+"
}

]

const course=computed(()=>{

return courses.find(

c=>c.id==route.params.id

)

})

function enroll(){

store.enroll(course.value);

router.push("/profile");

}

</script>

<style scoped>

.detail{

background:white;

padding:40px;

border-radius:15px;

box-shadow:0 5px 15px rgba(0,0,0,.15);

}

button{

margin-top:20px;

padding:14px 25px;

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