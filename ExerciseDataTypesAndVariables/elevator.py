people_num = int(input())
capacity = int(input())

courses = people_num // capacity
people_num -= courses * capacity
if people_num > 0:
    courses += 1

print(f'{courses}')