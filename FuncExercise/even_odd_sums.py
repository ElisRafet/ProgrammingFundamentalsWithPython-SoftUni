def even(number: int):
    even_sum = 0
    while number > 0:
        num = number % 10
        if num % 2 == 0:
            even_sum += num
        number = number // 10
    return even_sum

def odd(number: int):
    odd_sum = 0
    while number > 0:
        num = number % 10
        if num % 2 != 0:
            odd_sum += num
        number = number // 10
    return odd_sum

n = int(input())
print(f'Odd sum = {odd(n)}, Even sum = {even(n)}')
