def factorial(num: int) -> int:
    for multiplier in range(1, num):
        num *= multiplier
    return num

first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial((second_number))
result = first_factorial / second_factorial
print(f'{result: .2f}')