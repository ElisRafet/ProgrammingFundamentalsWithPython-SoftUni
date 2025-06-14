strings = input().split()
word = input()
count = 0
palindromes =[string for string in strings if string == ''.join(reversed(string))]
for palindrome in palindromes:
    if palindrome == word:
        count += 1

print(palindromes)
print(f'Found palindrome {count} times')

