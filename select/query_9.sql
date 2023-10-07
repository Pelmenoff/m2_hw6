SELECT subjects.name
FROM subjects
INNER JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 1;