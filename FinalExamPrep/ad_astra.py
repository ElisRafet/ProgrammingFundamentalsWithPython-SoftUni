import re

string_ = input()
pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{,5})\1'
matches = re.findall(pattern, string_)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for match in matches:
    item_name = match[1]
    date = match[2]
    calories = match[3]
    print(f'Item: {item_name}, Best before: {date}, Nutrition: {calories}')