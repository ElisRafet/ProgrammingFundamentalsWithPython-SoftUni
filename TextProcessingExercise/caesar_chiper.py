text = input()
new_text = ''
for index in text:
    new_text += chr(ord(index) + 3)
print(new_text)