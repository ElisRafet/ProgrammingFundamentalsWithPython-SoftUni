string = input()


for index in range(len(string)):
    if string[index] == ':':
        result = ':'
        result += string[index + 1]
        print(result)
