def characters(first, second):
    character_list = []
    for char in range(ord(first) + 1, ord(second)):
        character_list.append(chr(char))
    return character_list

char1 = input()
char2 = input()
print(" ".join(characters(char1, char2)))