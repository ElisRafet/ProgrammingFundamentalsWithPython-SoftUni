wagons = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]

    if current_command == 'End':
        print(wagons)
        break

    if current_command== 'add':
        people_count = int(command[1])
        wagons[-1] += people_count
    elif current_command == 'insert':
       index = int(command[1])
       people_count = int(command[2])
       wagons[index] += people_count
    elif current_command == 'leave':
        index = int(command[1])
        people_count = int(command[2])
        wagons[index] -= people_count