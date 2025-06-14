money_as_string = input().split(', ')
beggars = int(input())
money_as_int = []

for money in money_as_string:
    moneys = int(money)
    money_as_int.append(moneys)

start_index = 0
beggars_sums = []
for current_beggar in range(beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_int), beggars):
        current_beggar_sum += money_as_int[current_index]
    beggars_sums.append(current_beggar_sum)
    start_index += 1

print(beggars_sums)