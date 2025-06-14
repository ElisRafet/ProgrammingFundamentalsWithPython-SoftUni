string_list = input().split(' ')
num = int(input())
int_list = []

for element in string_list:
    elements = int(element)
    int_list.append(elements)

for element in range(num):
    int_list.remove(min(int_list))

strings = []
for element in int_list:
    elements = str(element)
    strings.append(elements)

print(", ".join(strings))
