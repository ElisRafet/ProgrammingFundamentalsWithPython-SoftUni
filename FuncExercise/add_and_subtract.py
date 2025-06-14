def sum_numbers(a, b):
    return a + b

def subtract(a, b, c):
    result = sum_numbers(a, b) - c
    return result

first = int(input())
second = int(input())
third = int(input())

print(subtract(first, second, third))