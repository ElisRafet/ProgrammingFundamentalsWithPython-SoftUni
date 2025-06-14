coffee_count = 0
event = input()
while event != 'END':
    if event == 'dog' or event == 'cat' or event == 'coding' or event == 'movie':
        coffee_count += 1
    elif event =='DOG' or event == 'CAT' or event == 'CODING' or event == 'MOVIE':
        coffee_count += 2

    event = input()

if coffee_count > 5:
    print('You need extra sleep')
else:
    print(coffee_count)