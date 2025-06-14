def is_palindrome(num: str) -> bool:
    return num == num [:: -1]

numbers = input().split(', ')
for current_number in numbers:
    print(is_palindrome(current_number))

