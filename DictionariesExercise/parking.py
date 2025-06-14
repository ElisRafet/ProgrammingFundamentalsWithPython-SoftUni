n = int(input())
registrations = {}
for i in range(n):
    command = input().split()
    action = command[0]
    if action == 'register':
        username = command[1]
        plate_num = command[2]
        if username not in registrations:
            registrations[username] = plate_num
            print(f'{username} registered {plate_num} successfully')
        elif username in registrations:
            print(f'ERROR: already registered with plate number {plate_num}')
    elif action == 'unregister':
        username = command[1]
        if username not in registrations:
            print(f'ERROR: user {username} not found')
        elif username in registrations:
            del registrations[username]
            print(f'{username} unregistered successfully')

for key, value in registrations.items():
    print(f'{key} => {value}')