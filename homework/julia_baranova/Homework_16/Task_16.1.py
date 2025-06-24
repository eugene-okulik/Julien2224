import csv
import dotenv
import os
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_file_path))))
file_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
info_from_file = []
with open(file_path) as csv_file:
    file_data = csv.reader(csv_file)
    next(file_data)
    for row in file_data:
        info_from_file.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

cursor = db.cursor()
select_query = '''
SELECT
    students.name,
    students.second_name,
    groups.title,
    books.title,
    subjets.title,
    lessons.title,
    marks.value
FROM students
JOIN books on students.id = books.taken_by_student_id
JOIN `groups` on students.group_id = groups.id
JOIN marks on students.id = marks.student_id
JOIN lessons on lessons.id = marks.lesson_id
JOIN subjets on lessons.subject_id = subjets.id
GROUP BY
subjets.id, books.id, marks.id
'''
cursor.execute(select_query)
info_from_db = cursor.fetchall()
for row in info_from_file:
    if row in info_from_db:
        print(f"Есть в базе: {row}")
    else:
        print(f"Нет в базе: {row}")
