products = {}

while True:
    new_products = input().split(": ")
    if new_products[0] == "statistics":
        break

    prod = new_products[0]
    quantity = new_products[1]
    if prod in products:
        products[prod] += int(quantity)
    else:
        products[prod] = int(quantity)

print(f"Products in stock:")

for prod, quantity in products.items():
    print(f'- {prod}: {quantity}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')

