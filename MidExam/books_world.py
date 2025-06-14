old_favorites = input().split(" | ")

while True:
    command = input().split()
    command_new = command[0]
    if command_new == 'Stop!':
        break
    if command_new == 'Join':
        genre = command[1]
        if genre not in old_favorites:
            old_favorites.append(genre)
    elif command_new == 'Drop':
        genre = command[1]
        if genre in old_favorites:
            old_favorites.remove(genre)
    elif command_new == 'Replace':
        old_genre = command[1]
        new_genre = command[2]
        if old_genre in old_favorites and new_genre not in old_favorites:
            index = old_favorites.index(old_genre)
            old_favorites.remove(old_genre)
            old_favorites.insert(index, new_genre)
    elif command_new == 'Prefer':
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(old_favorites) and 0 <= index2 < len(old_favorites):
            old_favorites[index1], old_favorites[index2] = old_favorites[index2], old_favorites[index1]


print(" ".join(old_favorites))