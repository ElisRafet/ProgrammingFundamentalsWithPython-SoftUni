my_list = input().split(", ")
searched_element = 0
new_list =[]
zero_list = []
non_zero_list = []

for element in my_list:
    current_element = int(element)
    if current_element == searched_element:
        zero_list.append(current_element)
    else:
        non_zero_list.append(current_element)

new_list = non_zero_list + zero_list


print(new_list)
