ticket_price = 150
items = input().split('|')
budget = float(input())
money_for_shopping = 0
money_from_selling = 0
selling_prices_list = []

for item in items:
    current_item = item.split('->')
    item_type = current_item[0]
    item_price = float(current_item[1])
    if item_type == 'Clothes':
        if not (item_price > 50.00 or item_price > budget):
            budget -= item_price
            selling_price = item_price * 1.4
            money_for_shopping += item_price
            money_from_selling += selling_price
            selling_prices_list.append(f'{selling_price: .2f}')
    elif item_type == 'Shoes':
        if not (item_price > 35.00 or item_price > budget):
            budget -= item_price
            selling_price = item_price * 1.4
            money_for_shopping += item_price
            money_from_selling += selling_price
            selling_prices_list.append(f'{selling_price: .2f}')
    elif item_type == 'Accessories':
        if not (item_price > 20.50 or item_price > budget):
            budget -= item_price
            selling_price = item_price * 1.4
            money_for_shopping += item_price
            money_from_selling += selling_price
            selling_prices_list.append(f'{selling_price: .2f}')

profit = money_from_selling - money_for_shopping

print(''.join(selling_prices_list))
print(f'Profit:{profit: .2f}')
if (money_from_selling + budget) >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')