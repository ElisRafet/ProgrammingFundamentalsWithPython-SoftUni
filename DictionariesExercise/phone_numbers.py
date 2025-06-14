phonebook = {}

while True:
    contact = input()
    if len(contact) < 2:
        n = int(contact)
        break
    name, number = contact.split('-')
    if name not in phonebook.keys():
        phonebook[name] = number

for i in range(n):
    searched_person = input()
    if searched_person in phonebook.keys():
        print(f'{searched_person} -> {phonebook[searched_person]}')
    else:
        print(f'Contact {searched_person} does not exist.')

