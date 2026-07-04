return (
    <div className="container">

        <h1 className="title">
            Course Management
        </h1>

        <div className="grid">

            {courses.map(course=>(
                <CourseCard
                    key={course.id}
                    course={course}
                />
            ))}

        </div>

    </div>
)