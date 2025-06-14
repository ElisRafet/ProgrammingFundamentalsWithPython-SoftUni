students = []
searched_course = ''

while True:
    student_info = input()
    if ':' not in student_info:
        searched_course = student_info
        break

    name, id_, course = student_info.split(':')
    students.append({'name': name, 'id': id_, 'course': course})

for student in students:
    if searched_course.startswith(student['course'][0:5]):
        print(f"{student['name']} - {student['id']}")
