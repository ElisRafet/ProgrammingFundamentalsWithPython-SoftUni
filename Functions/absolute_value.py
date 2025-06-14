numbers = input().split()
abs_numbers = []

for number in numbers:
    current_number = abs(float(number))
    abs_numbers.append(current_number)

print(abs_numbers)