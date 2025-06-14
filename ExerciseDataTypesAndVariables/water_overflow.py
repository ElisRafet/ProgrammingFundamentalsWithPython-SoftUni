capacity_of_tank = 255
n = int(input())
water = 0

for line in range(n):
    litres = int(input())
    if capacity_of_tank - litres < 0:
        print('Insufficient capacity!')
        continue
    capacity_of_tank -= litres

print(255 - capacity_of_tank)
