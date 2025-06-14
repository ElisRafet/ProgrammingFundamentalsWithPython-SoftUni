def is_even(n):
    return n % 2 == 0

numbers = input().split()
int_numbers = []
for num in numbers:
    current_number = int(num)
    int_numbers.append(current_number)

EVEN_NUMBERS = list(filter(is_even, int_numbers))
print(EVEN_NUMBERS)