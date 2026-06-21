alter table students add column
phone_number varchar(15);

alter table courses add column 
max_seats int default 60;

alter table departments rename column hod_name  
to head_of_department

alter table students 
drop column phone_number;

UPDATE enrollments
SET grade = 'B'
WHERE student_id = 5
  AND course_id = 1
  AND grade = 'C';

DELETE FROM enrollments
WHERE grade IS NULL

select * from enrollments ;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM enrollments
WHERE grade IS NULL;

SET SQL_SAFE_UPDATES = 1;

select * from students 
where enrollment_year = 2022
order by last_name;

select * from courses
where credits >3
order by credits DESC;

select* from professors
where salary between 80000 and 95000;

select * from students 
where email like '%@college.edu';

select enrollment_year,count(student_id) from students 
group by enrollment_year
order by count(student_id);


SELECT
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

SELECT
    e.enrollment_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_name,
    e.enrollment_date,
    e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;


SELECT
    c.course_id,
    c.course_name,
    COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;


SELECT
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id;


SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;


SELECT
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name;


SELECT
    department_id,
    dept_name,
    budget
FROM departments
WHERE budget > 600000;


SELECT
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c
ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;


SELECT
    d.dept_name,
    COUNT(DISTINCT e.student_id) AS total_students
FROM departments d
JOIN courses c
ON d.department_id = c.department_id
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(DISTINCT e.student_id) > 2;


