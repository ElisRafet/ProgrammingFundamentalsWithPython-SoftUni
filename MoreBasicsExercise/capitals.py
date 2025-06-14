
string = input()
new_string = []

for index in range(0, len(string)):
    if string[index].isupper():
        new_string += [index]

print(new_string[:])
