import { courses } from "./data.js";

/* ==========================
   DOM Elements
========================== */

const courseGrid = document.querySelector(".course-grid");

const totalCredits =
document.querySelector("#total-credits");

const loadingMessage =
document.querySelector("#loading-message");

const spinner =
document.querySelector("#spinner");

const notificationList =
document.querySelector("#notification-list");

const errorMessage =
document.querySelector("#error-message");

const retryButton =
document.querySelector("#retry-btn");


/* ==========================
Task 45
Promise with .then()
========================== */

function fetchUser(id){

    return fetch(
    `https://jsonplaceholder.typicode.com/users/${id}`
    )
    .then(response=>response.json())
    .then(user=>{

        console.log("User Name :",user.name);

        return user;

    });

}

fetchUser(1);


/* ==========================
Task 46
Async Await
========================== */

async function fetchUserAsync(id){

    try{

        const response =
        await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const user =
        await response.json();

        console.log(
        "Async User :",
        user.name
        );

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);


/* ==========================
Task 47
Network Delay
========================== */

function fetchAllCourses(){

    return new Promise(resolve=>{

        setTimeout(()=>{

            resolve(courses);

        },1000);

    });

}


/* ==========================
Render Courses
========================== */

function renderCourses(courseArray){

    courseGrid.innerHTML="";

    courseArray.forEach(course=>{

        const article =
        document.createElement("article");

        article.className="course-card";

        article.innerHTML=`

        <h3>${course.name}</h3>

        <p>Code : ${course.code}</p>

        <p>Credits : ${course.credits}</p>

        <p>Grade : ${course.grade}</p>

        `;

        courseGrid.appendChild(article);

    });

    const total =
    courseArray.reduce(

    (sum,course)=>sum+course.credits,

    0

    );

    totalCredits.textContent =
    `Total Credits : ${total}`;

}


/* ==========================
Task 48
Loading Courses
========================== */

loadingMessage.style.display="block";

fetchAllCourses()

.then(courseArray=>{

    loadingMessage.style.display="none";

    renderCourses(courseArray);

});


/* ==========================
Task 49
Promise.all()
========================== */

Promise.all([

fetchUser(1),

fetchUser(2)

])

.then(users=>{

console.log(

users[0].name,

users[1].name

);

});

/* ==========================
Task 56
Axios apiFetch()
========================== */

async function apiFetch(url){

    try{

        const response =
        await axios.get(url);

        return response.data;

    }

    catch(error){

        throw new Error(

            error.response
            ? `HTTP Error ${error.response.status}`
            : "Network Error"

        );

    }

}


/* ==========================
Task 51 & 52
Notifications
========================== */

async function loadNotifications(){

spinner.classList.remove("hidden");

notificationList.innerHTML="";

errorMessage.textContent="";

retryButton.classList.add("hidden");

try{

const posts =
await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=5"

);

spinner.classList.add("hidden");

posts.forEach(post=>{

const card =
document.createElement("div");

card.className=
"notification-card";

card.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

notificationList.appendChild(card);

});

}

catch(error){

spinner.classList.add("hidden");

errorMessage.textContent=
error.message;

retryButton.classList.remove("hidden");

}

}

loadNotifications();


/* ==========================
Task 53
404 Error
========================== */

async function simulateError(){

try{

await apiFetch(

"https://jsonplaceholder.typicode.com/nonexistent"

);

}

catch(error){

errorMessage.textContent=
"Unable to load notifications.";

retryButton.classList.remove("hidden");

}

}

/* Uncomment to test 404 */

// simulateError();


/* ==========================
Task 54
Retry Button
========================== */

retryButton.addEventListener(

"click",

()=>{

loadNotifications();

}

);

/* ==========================
Task 57
Axios Params
========================== */

async function loadUserPosts(){

    try{

        const posts =
        await axios.get(

        "https://jsonplaceholder.typicode.com/posts",

        {

            params:{
                userId:1
            }

        }

        );

        console.log("User 1 Posts");

        posts.data.forEach(post=>{

            console.log(post.title);

        });

    }

    catch(error){

        console.log(error);

    }

}

loadUserPosts();

/* ==========================
Task 58
Axios Interceptor
========================== */

axios.interceptors.request.use(

(config)=>{

    console.log(

    `API call started: ${config.url}`

    );

    return config;

},

(error)=>{

    return Promise.reject(error);

}

);
await axios.get(

"https://jsonplaceholder.typicode.com/posts",

{

    timeout:5000

}

);
/*

==============================
Fetch vs Axios
==============================

1. Fetch
   - Built into modern browsers
   - Axios requires an external library

2. Fetch
   - Requires response.json()
   - Axios automatically converts JSON

3. Fetch
   - Does NOT throw errors for HTTP 404/500
   - Axios automatically throws errors for non-2xx responses

*/
