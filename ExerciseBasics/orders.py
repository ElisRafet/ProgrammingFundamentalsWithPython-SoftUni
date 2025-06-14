n = int(input())
total = 0

for i in range(n):
    price_for_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price = price_for_capsule * days * capsules_per_day
    total += price
    if price > 0:
        print(f"The price for the coffee is: ${price: .2f}")

print(f"Total: ${total: .2f}")

number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif 1 < days < 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    price = days * price_per_capsule * capsule_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")