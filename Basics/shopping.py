budget = int(input())
command = input()

while command != 'End':
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')


#while budget > 0:
#    command = input()
#   if command == 'End':
#        print('You bought everything needed.')
#        break
#
#    budget -= int(command)
#else:
#    print('You went in overdraft!')

