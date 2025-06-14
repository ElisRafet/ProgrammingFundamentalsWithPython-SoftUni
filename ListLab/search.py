n = int(input())
special_word = input()
just_list = []

for text in range(n):
    current_text = input()
    just_list.append(current_text)

print(just_list)

for i in range(len(just_list) -1, -1, -1):
    element = just_list[i]
    if special_word not in element:
        just_list.remove(element)

print(just_list)