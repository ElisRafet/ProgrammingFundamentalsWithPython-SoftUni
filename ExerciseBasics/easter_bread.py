budget = float(input())
price_for_kg_flour = float(input())
price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_liter_milk = price_for_kg_flour + price_for_kg_flour * 0.25
colored_eggs= 0
bread_count = 0

cost_of_one_bread = price_for_kg_flour + price_for_pack_eggs + price_for_liter_milk / 4

while budget > cost_of_one_bread:
    budget -= cost_of_one_bread
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs = colored_eggs - (bread_count - 2)

print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
