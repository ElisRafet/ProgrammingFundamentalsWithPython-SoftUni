def add(stops_, index_, string_):
    if index_ in range(len(stops_)):
        stops_ = stops_[:index] + string + stops_[index:]
    return stops_

def remove(stops_, start, end):
    if start in range(len(stops_)) and end in range(len(stops_)):
        stops_ = stops_[:start] + stops_[end +1:]
    return stops_

def switch(stops_, old, new):
    if old in stops_:
        stops_ = stops_.replace(old, new)
    return stops_

stops = input()
while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break

    if command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        stops = add(stops, index, string)
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove(stops, start_index, end_index)
    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)

print(f'Ready for world tour! Planned stops: {stops}')

