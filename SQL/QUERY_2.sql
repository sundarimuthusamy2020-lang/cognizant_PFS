
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

SELECT
    c.course_id,
    c.course_name,
    c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND (e.grade <> 'A' OR e.grade IS NULL)
);


SELECT
    p.professor_id,
    p.prof_name,
    p.department_id,
    p.salary
FROM professors p
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

SELECT *
FROM
(
    SELECT  
        d.department_id,
        d.dept_name,
        ROUND(AVG(p.salary),2) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) AS dept_avg
WHERE avg_salary > 85000;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS gpa
FROM students s
LEFT JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY
    s.student_id,
    s.first_name,
    s.last_name,
    d.dept_name;

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY
    c.course_id,
    c.course_name,
    c.course_code;

SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3.0;

UPDATE vw_student_enrollment_summary
SET total_courses = 5
WHERE student_id = 1;

SELECT * FROM vw_course_stats;

DROP VIEW IF EXISTS vw_student_enrollment_summary;
DROP VIEW IF EXISTS vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id
FROM students
WHERE department_id IS NOT NULL
WITH CHECK OPTION;


DELIMITER $$

CREATE PROCEDURE sp_enroll_student
(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    IF EXISTS
    (
        SELECT *
        FROM enrollments
        WHERE student_id = p_student_id
          AND course_id = p_course_id
    )
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate enrollment not allowed';
    ELSE
        INSERT INTO enrollments
        (
            student_id,
            course_id,
            enrollment_date
        )
        VALUES
        (
            p_student_id,
            p_course_id,
            p_enrollment_date
        );
    END IF;

END $$

DELIMITER ;


CALL sp_enroll_student(1,2,'2025-06-17');


CREATE TABLE department_transfer_log
(
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student
(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN

    DECLARE v_old_department INT;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (
        student_id,
        old_department_id,
        new_department_id
    )
    VALUES
    (
        p_student_id,
        v_old_department,
        p_new_department
    );

    COMMIT;

END $$

DELIMITER ;

CALL sp_transfer_student(1,2);

CALL sp_transfer_student(1,999);



START TRANSACTION;

INSERT INTO enrollments
(student_id, course_id, enrollment_date)
VALUES
(1,3,CURDATE());

SAVEPOINT sp1;


INSERT INTO enrollments
(student_id, course_id, enrollment_date)
VALUES
(9999,4,CURDATE());

ROLLBACK TO sp1;

COMMIT;


SELECT *
FROM enrollments
WHERE student_id = 1
  AND course_id = 3;
