word_list = input().split(' ')

filtered_list = [word for word in word_list if len(word) % 2 == 0]
print('\n'.join(filtered_list))