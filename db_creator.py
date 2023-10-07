import sqlite3
from faker import Faker
import random

# Create a connection to the database
conn = sqlite3.connect('m2_hw6.db')
cursor = conn.cursor()

# Create a table for students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER,
                    birthdate DATE
                )''')

# Create a table for groups
cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# Create a table for teachers
cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# Create a table for subjects
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER
                )''')

# Create a table for students' grades
cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date DATE
                )''')

# Create a Faker object for generating fake data
fake = Faker()

# Populate the groups table with data
groups = [('Group A',), ('Group B',), ('Group C',)]
cursor.executemany('INSERT INTO groups (name) VALUES (?)', groups)

# Populate the teachers table with data
teachers = [('Teacher 1',), ('Teacher 2',), ('Teacher 3',)]
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', teachers)

# Generate students and insert them into the table
students = []
for _ in range(50):
    students.append((fake.name(), random.randint(1, 3), fake.date_of_birth(minimum_age=18, maximum_age=30).strftime('%Y-%m-%d')))
cursor.executemany('INSERT INTO students (name, group_id, birthdate) VALUES (?, ?, ?)', students)

# Populate the subjects table with data
subjects = []
for _ in range(8):
    subjects.append((fake.word(), random.randint(1, 3)))
cursor.executemany('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', subjects)

# Generate grades for students
grades = []
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        grades.append((student_id, subject_id, random.randint(1, 10), fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')))
cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', grades)

# Save the changes and close the connection
conn.commit()
conn.close()

print("The database has been successfully created and populated with data.")