<template>

<div class="card">

<h2>{{ name }}</h2>

<p><b>Code:</b> {{ code }}</p>

<p><b>Credits:</b> {{ credits }}</p>

<p><b>Grade:</b> {{ grade }}</p>

<button @click="$emit('enroll')">

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

transform:translateY(-6px);

}

button{

width:100%;
padding:12px;
border:none;
background:#2563eb;
color:white;
font-size:16px;
border-radius:8px;
cursor:pointer;
margin-top:15px;

}

button:hover{

background:#1d4ed8;

}

</style>