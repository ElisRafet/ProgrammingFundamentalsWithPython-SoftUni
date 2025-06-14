quantity_of_decorations = int(input())
left_days = int(input())
total_cost = 0
total_spirit = 0
ornaments = 2
skirt = 5
garland = 3
lights = 15

for day in range(1, left_days + 1):
    if day % 2 == 0:
        total_cost += quantity_of_decorations * ornaments
        total_spirit += 5
    if day % 3 == 0:
        total_cost += quantity_of_decorations * (skirt + garland)
        total_spirit += 13
    if day % 5 == 0:
        total_cost += quantity_of_decorations * lights
        total_spirit += 17
        if day % 3 == 0:
            total_cost += quantity_of_decorations * (skirt + garland)
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost = skirt + garland + lights
    if day % 11 == 0:
        quantity_of_decorations += 2

if left_days % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')