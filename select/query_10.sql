SELECT subjects.name
FROM subjects
INNER JOIN grades ON subjects.id = grades.subject_id
INNER JOIN students ON grades.student_id = students.id
WHERE students.id = 1 AND subjects.teacher_id = 1;