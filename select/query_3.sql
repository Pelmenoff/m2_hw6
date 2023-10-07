SELECT groups.name, AVG(grades.grade) AS average_grade
FROM groups
INNER JOIN students ON groups.id = students.group_id
INNER JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 1
GROUP BY groups.name;