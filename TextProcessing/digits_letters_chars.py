text = input()
digits = ''
letters = ''
chars = ''

for symbol in text:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        chars += symbol

print(digits)
print(letters)
print(chars)