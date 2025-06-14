string_ = input()

while True:
    command = input().split()
    if command[0] == 'Done':
        break

    if command[0] == 'Change':
        char, replacement = command[1], command[2]
        string_ = string_.replace(char, replacement)
        print(string_)
    elif command[0] == 'Includes':
        substring = command[1]
        if substring in string_:
            print(True)
        else:
            print(False)
    elif command[0] == 'End':
        substring = command[1]
        print(string_.endswith(substring))
    elif command[0] == 'Uppercase':
        string_ = string_.upper()
        print(string_)
    elif command[0] == 'FindIndex':
        char = command[1]
        index = string_.find(char)
        print(index)
    elif command[0] == 'Cut':
        start_index, count = int(command[1]), int(command[2])
        cut_string = string_[start_index:start_index + count]
        print(cut_string)

