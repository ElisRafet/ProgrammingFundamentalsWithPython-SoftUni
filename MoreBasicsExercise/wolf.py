string = input()
list_of_animals = string.split(', ')
count = 0
last_animal = ''

for animal in range(0, len(list_of_animals)):
    last_animal = list_of_animals[animal]
    if list_of_animals[animal] == 'sheep':
        count += 1

if last_animal == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    print(f'Oi! Sheep number {count}! You are about to be eaten by a wolf!')