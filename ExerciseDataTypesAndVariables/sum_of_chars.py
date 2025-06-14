n = int(input())
total = 0

for character in range(n):
    current_character = input()
    total += ord(current_character)

print(f'The sum equals: {total}')