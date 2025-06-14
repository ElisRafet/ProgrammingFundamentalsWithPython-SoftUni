products_price = {}
products_quantities = {}
command = input()
while command != 'buy':
    name, price, quantity = command.split()
    if name not in products_price.keys():
        products_price[name] = float(price)
    else:
        products_price[name] = float(price)
    if name not in products_quantities:
        products_quantities[name] = int(quantity)
    else:
        products_quantities[name] += int(quantity)
    command = input()

products_total = {}
for prod in products_price.keys():
    for product in products_quantities:
        if prod == product:
            products_total[prod] = products_price[prod] * products_quantities[product]
for key, value in products_total.items():
    print(f'{key} ->{value: .2f}')