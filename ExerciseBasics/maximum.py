divisor = int(input())
boundary = int(input())

for n in range(boundary + 1, 0, -1):
    if 0 < n <= boundary and n % divisor == 0:
        print(n)
        break