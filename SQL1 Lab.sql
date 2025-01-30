-- SQL Exercises (With Answers)

-- 1. Retrieve all students who enrolled in 2023.
SELECT*FROM students
WHERE enrollmentdate like "%2023%";

-- 2. Find students whose email contains 'gmail.com'.
SELECT*FROM students
WHERE Email like "%gmail.com%";

-- 3. Count how many students are enrolled in the database.
SELECT COUNT(*) AS TotalStudents
FROM students;


-- 4. Find students born between 2000 and 2005.
SELECT*FROM students
WHERE DateOfBirth BETWEEN '2000-01-01' AND '2005-12-31';

-- 5. List students sorted by last name in descending order.

SELECT*FROM students
ORDER BY LastName DESC;

-- 6. Find the names of students and the courses they are enrolled in.

SELECT students.FirstName, students.LastName, courses.CourseName
FROM students
JOIN enrollments ON students.StudentID = enrollments.StudentID
JOIN courses ON enrollments.CourseID = courses.CourseID;




-- 7. List all students and their courses, ensuring students without courses are included (LEFT JOIN).

SELECT students.FirstName, students.LastName, courses.CourseName
FROM students
LEFT JOIN enrollments ON students.StudentID = enrollments.StudentID
LEFT JOIN courses ON enrollments.CourseID = courses.CourseID;

-- 8. Find all courses with no students enrolled (LEFT JOIN).

SELECT courses.CourseName
FROM courses
LEFT JOIN enrollments ON courses.CourseID = enrollments.CourseID
WHERE enrollments.StudentID IS NULL;


-- 10. List courses and show the number of students enrolled in each course.

SELECT courses.CourseName, COUNT(enrollments.StudentID) AS StudentCount
FROM courses
LEFT JOIN enrollments ON courses.CourseID = enrollments.CourseID
GROUP BY courses.CourseName;


