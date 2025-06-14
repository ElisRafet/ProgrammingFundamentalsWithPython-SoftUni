paintings_num = list(map(int, input().split()))

while True:
    command = input().split()
    command_new = command[0]
    if command_new == 'END':
        break
    if command_new == 'Change':
        paint = int(command[1])
        new_paint = int(command[2])
        if paint in paintings_num:
            index = paintings_num.index(paint)
            paintings_num.remove(paint)
            paintings_num.insert(index, new_paint)
    elif command_new == 'Hide':
        paint = int(command[1])
        if paint in paintings_num:
            paintings_num.remove(paint)
    elif command_new == 'Switch':
        paint = int(command[1])
        new_paint = int(command[2])
        if paint in paintings_num and new_paint in paintings_num:
            index1 = paintings_num.index(paint)
            index2 = paintings_num.index(new_paint)
            if 0 <= index1 < len(paintings_num) and 0 <= index2 < len(paintings_num):
                paintings_num[index1], paintings_num[index2] = paintings_num[index2], paintings_num[index1]
    elif command_new == 'Insert':
        index = int(command[1])
        paint = int(command[2])
        if 0 <= index < len(paintings_num):
            paintings_num.insert(index, paint)
    elif command_new == 'Reverse':
        paintings_num.reverse()

print(" ".join(map(str, paintings_num)))