
   INSERT into students (name, second_name) VALUES ('Julia', 'Baranova')

   INSERT into books (title) VALUES ('Julia_book1')
   INSERT into books (title) VALUES ('Julia_book2')

   UPDATE books SET taken_by_student_id = 20280 WHERE title = 'Julia_book1'
   UPDATE books SET taken_by_student_id = 20280 WHERE title = 'Julia_book2'

   INSERT into `groups` (title, start_date, end_date) VALUES ('Julia_group', 'oct24', 'oct_25')
   UPDATE students SET group_id = 5011 WHERE id = 20280

   INSERT into subjets (title) VALUES ('Julia_sub1')
   INSERT into subjets (title) VALUES ('Julia_sub2')

   INSERT into lessons (title, subject_id) VALUES ('lesson1', 10223)
   INSERT into lessons (title, subject_id) VALUES ('lesson2', 10223)

   INSERT into lessons (title, subject_id) VALUES ('lesson1', 10224)
   INSERT into lessons (title, subject_id) VALUES ('lesson2', 10224)

   INSERT into marks (value, lesson_id, student_id) VALUES (10, 9653, 20280)
   INSERT into marks (value, lesson_id, student_id) VALUES (10, 9654, 20280)
   INSERT into marks (value, lesson_id, student_id) VALUES (10, 9655, 20280)
   INSERT into marks (value, lesson_id, student_id) VALUES (10, 9656, 20280)

   SELECT * FROM marks WHERE student_id = 20280
   SELECT * FROM books WHERE taken_by_student_id = 20280

   SELECT students.id, students.name, students.second_name, books.title, groups.title, subjets.title, lessons.title, marks.value FROM students
   JOIN books on students.id = books.taken_by_student_id
   JOIN `groups` on students.group_id = groups.id
   JOIN marks on students.id = marks.student_id
   JOIN lessons on lessons.id = marks.lesson_id
   JOIN subjets on lessons.subject_id = subjets.id
   WHERE students.id = 20280
   GROUP BY subjets.id, books.id, marks.id