courses = {}
while True:
    data = input()
    if data == 'end':
        break
    name, student = data.split(' : ')
    if name not in courses:
        courses[name] = []
    courses[name].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f'-- {value[i]}')
