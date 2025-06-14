numbers = list(map(int, input().split(', ')))
current_group = 10

while numbers:
    filtered_numbers = [number for number in numbers if number <= current_group]
    numbers = [number for number in numbers if number not in filtered_numbers]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10