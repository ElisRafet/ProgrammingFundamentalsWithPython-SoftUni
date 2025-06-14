import re

n = int(input())
pattern = r'(.+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^<>]+)<\1'

for _ in range(n):
    password = input()
    match = re.fullmatch(pattern, password)
    if match:
        numbers = match.group(2)
        lower_chars = match.group(3)
        upper_chars = match.group(4)
        symbols = match.group(5)
        encrypted_password = numbers + lower_chars + upper_chars + symbols
        print(f'Password: {encrypted_password}')
    else:
        print(f'Try another password!')
