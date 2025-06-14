stock = input().split()
bakery = {}

for i in range(0, len(stock), 2):
    product = stock[i]
    quantity = stock[i + 1]
    bakery[product] = int(quantity)

print(bakery)