first_list = input().split(', ')
second_list = input().split(', ')
substrings = [first_string for first_string in first_list if any(first_string in second_string for second_string in second_list)]

print(substrings)