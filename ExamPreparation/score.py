student_num = int(input())
lectures_num = int(input())
bonus = int(input())
attendances =[]

for student in range(1, student_num + 1):
    attendance = int(input())
    attendances.append(attendance)

total_bonus = max(attendances) / lectures_num * (5 + bonus)

print(f'Max Bonus: {round(total_bonus)}.')
print(f'The student has attended {max(attendances)} lectures.')