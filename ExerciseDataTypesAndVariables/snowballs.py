num_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broken = num_of_lost_fights // 2
total_sword_broken = num_of_lost_fights // 3
total_shield_broken = num_of_lost_fights // (2 * 3)
total_armor_broken = num_of_lost_fights // (2 * 6)

expenses = total_armor_broken * armor_price + \
          total_shield_broken * shield_price +  total_helmet_broken * helmet_price + \
          total_sword_broken * sword_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
