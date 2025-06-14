companions_num = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1 ):
    if current_day % 10 == 0:
        companions_num -= 2
    if current_day % 15 == 0:
        companions_num += 5
    if current_day % 3 == 0:
        coins -= 3 * companions_num
    if current_day % 5 == 0:
        coins += 20 * companions_num
        if current_day % 3 == 0:
            coins -= 2* companions_num
    coins += 50
    coins -= 2 * companions_num

coins = coins // companions_num
print(f"{companions_num} companions received {coins} coins each.")