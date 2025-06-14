factor = int(input())
count = int(input())
my_lis = []

for number in range(1, count + 1):
    num = number * factor
    my_lis.append(num)

print(my_lis)