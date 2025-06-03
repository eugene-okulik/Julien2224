import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()
cursor.execute("INSERT into students (name, second_name) VALUES ('Julia15', 'Baranova15')")
student_id = cursor.lastrowid
cursor.execute("INSERT into books (title) VALUES ('Julia_book1.15')")
cursor.execute("INSERT into books (title) VALUES ('Julia_book2.15')")
db.commit()
cursor.execute("UPDATE books SET taken_by_student_id = %s  WHERE title = 'Julia_book1.15'", (student_id,))
cursor.execute("UPDATE books SET taken_by_student_id = %s WHERE title = 'Julia_book2.15'", (student_id,))
cursor.execute("INSERT into `groups` (title, start_date, end_date) VALUES ('Julia_group15', 'oct24', 'oct_25')")
group_id = cursor.lastrowid
db.commit()
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

cursor.execute("INSERT into subjets (title) VALUES ('Julia_sub15.1')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT into subjets (title) VALUES ('Julia_sub15.2')")
subject2_id = cursor.lastrowid
db.commit()
cursor.execute("INSERT into lessons (title, subject_id) VALUES ('lesson15.1', %s )", (subject1_id,))
lesson1_id = cursor.lastrowid
cursor.execute("INSERT into lessons (title, subject_id) VALUES ('lesson15.2', %s )", (subject1_id,))
lesson2_id = cursor.lastrowid
cursor.execute("INSERT into lessons (title, subject_id) VALUES ('lesson15.3', %s )", (subject2_id,))
lesson3_id = cursor.lastrowid
cursor.execute("INSERT into lessons (title, subject_id) VALUES ('lesson15.4', %s )", (subject2_id,))
lesson4_id = cursor.lastrowid
db.commit()
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (10, %s,%s)", (lesson1_id, student_id))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (10, %s,%s)", (lesson2_id, student_id))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (10, %s,%s)", (lesson3_id, student_id))
cursor.execute("INSERT into marks (value, lesson_id, student_id) VALUES (10, %s,%s)", (lesson4_id, student_id))
db.commit()
cursor.execute(" SELECT * FROM marks WHERE student_id = %s ", (student_id,))
print(cursor.fetchall())
cursor.execute(" SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())
select_query = '''
SELECT students.id, students.name, students.second_name, books.title, groups.title, subjets.title, lessons.title, marks.value
FROM students
JOIN books on students.id = books.taken_by_student_id
JOIN `groups` on students.group_id = groups.id
JOIN marks on students.id = marks.student_id
JOIN lessons on lessons.id = marks.lesson_id
JOIN subjets on lessons.subject_id = subjets.id
WHERE students.id = %s
GROUP BY
subjets.id, books.id, marks.id
'''
cursor.execute(select_query, (student_id,))
print(cursor.fetchall())
db.close()
