import { courses } from "./data.js";

/* ===========================
   Task 30
=========================== */

courses.forEach(course => {

    const { name, credits } = course;

    console.log(name, credits);

});


/* ===========================
   Task 31
=========================== */

const formattedCourses = courses.map(course =>
`${course.code} — ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);


/* ===========================
   Task 32
=========================== */

const filteredCourses = courses.filter(course => course.credits >= 4);

console.log(filteredCourses.length);


/* ===========================
   Task 33
=========================== */

const totalCredits = courses.reduce(
(total, course) => total + course.credits,
0
);

console.log(totalCredits);


/* ===========================
   Task 36
=========================== */

const courseGrid = document.querySelector(".course-grid");

const totalCreditText =
document.querySelector("#total-credits");

const searchInput =
document.querySelector("#search-courses");

const sortButton =
document.querySelector("#sort-btn");

const selectedCourse =
document.querySelector("#selected-course");


/* ===========================
   Render Function
=========================== */

const renderCourses = (courseArray) => {

    courseGrid.innerHTML = "";

    const fragment = document.createDocumentFragment();

    courseArray.forEach(course => {

        const article =
        document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `

        <h3>${course.name}</h3>

        <p>Code : ${course.code}</p>

        <p>Credits : ${course.credits}</p>

        `;

        fragment.appendChild(article);

    });

    courseGrid.appendChild(fragment);

    const total = courseArray.reduce(
    (sum, course)=>sum+course.credits,
    0
    );

    totalCreditText.textContent =
    `Total Credits : ${total}`;

};

/* Initial Rendering */

renderCourses(courses);


/* ===========================
   Task 41
=========================== */

searchInput.addEventListener("input",(event)=>{

const keyword =
event.target.value.toLowerCase();

const result =
courses.filter(course=>

course.name
.toLowerCase()
.includes(keyword)

);

renderCourses(result);

});


/* ===========================
   Task 42
=========================== */

sortButton.addEventListener("click",()=>{

const sortedCourses =
[...courses].sort(

(a,b)=>

b.credits-a.credits

);

renderCourses(sortedCourses);

});


/* ===========================
   Task 44
=========================== */

courseGrid.addEventListener("click",(event)=>{

const card =
event.target.closest(".course-card");

if(!card) return;

const id =
Number(card.dataset.id);

const selected =
courses.find(

course=>course.id===id

);

selectedCourse.textContent =
`Selected Course: ${selected.name} | Grade: ${selected.grade}`;

// You can also use:
// alert(`${selected.name} - Grade: ${selected.grade}`);

});