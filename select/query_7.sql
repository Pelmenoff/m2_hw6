SELECT students.name, grades.grade
FROM students
INNER JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 1;