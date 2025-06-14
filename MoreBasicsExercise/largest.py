#number = input()
#max_num = 0
#largest_num = []

#for num in range(len(number) + 1):
#    n = int(number(num))
#    largest_num += [number(num)]

#largest_num.reverse()

#for i in range(len(number)):
#    print(largest_num[i], end ='')


number = int(input())
num_str = str(number)
sorted_digits = sorted(num_str, reverse=True)
largest_num_str = ''.join(sorted_digits)
largest_num = int(largest_num_str)

print(largest_num)
