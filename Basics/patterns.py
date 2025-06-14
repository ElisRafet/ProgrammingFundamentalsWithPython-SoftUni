num = int(input())

for i in range(1, num + 1):
    for j in range(i):
        print('*', end= '')
    print('')

for m in range(num - 1, 0, -1):
    for n in range(m):
        print('*', end= '')
    print('')