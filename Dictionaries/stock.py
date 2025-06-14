products = input().split()
stock = {}

for i in range(0, len(products), 2):
    product = products[i]
    quantity = int(products[i + 1])
    stock[product] = quantity

searched_products = input().split()

for prod in searched_products:
    if prod in stock:
        print(f"We have {stock[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")
