likes = {}
dislikes_count = 0

while True:
    command = input().split('-')
    if command[0] == 'Stop':
        break

    if command[0] == 'Like':
        guest, meal = command[1], command[2]
        if guest not in likes.keys():
            likes[guest] = []
            likes[guest].append(meal)
        if meal not in likes[guest]:
            likes[guest].append(meal)
    elif command[0] == 'Dislike':
        guest, meal = command[1], command[2]
        if guest not in likes:
            print(f'{guest} is not at the party.')
        else:
            if meal not in likes[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                likes[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                dislikes_count += 1

for guest in likes.keys():
    print(f'{guest}: {", ".join(likes[guest])}')
print(f'Unliked meals: {dislikes_count}')


