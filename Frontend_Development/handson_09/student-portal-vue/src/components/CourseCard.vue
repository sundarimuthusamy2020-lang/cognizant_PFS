<template>

<div

class="card"

tabindex="0"

@keydown.enter="$emit('enroll')"

>

<h2>{{ name }}</h2>

<p>

<b>Code:</b>

{{ code }}

</p>

<p>

<b>Credits:</b>

{{ credits }}

</p>

<p>

<b>Grade:</b>

{{ grade }}

</p>

<button
@click="$emit('enroll')">

Enroll

</button>

</div>

</template>

<script setup>

defineProps({

name:String,
code:String,
credits:Number,
grade:String

})

defineEmits(["enroll"])

</script>

<style scoped>

.card{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0 5px 15px rgba(0,0,0,.15);

transition:.3s;

}

.card:hover{

transform:translateY(-5px);

}

button{

margin-top:20px;

width:100%;

padding:12px;

border:none;

border-radius:8px;

background:#2563eb;

color:white;

cursor:pointer;

}

button:hover{

background:#1d4ed8;

}

.card:focus{

outline:3px solid #2563eb;

}

</style>