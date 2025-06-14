n = int(input())
students = {}
for i in range(n):
    count = 1
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = grade
    elif name in students:
        count += 1
        students[name] += grade
        students[name] /= count
    if students[name] < 4.50:
        del students[name]

for key, value in students.items():
    print(f'{key} ->{value: .2f}')

