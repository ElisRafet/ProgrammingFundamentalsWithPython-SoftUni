def solve(prod, count):
    result = None
    if prod == 'coffee':
        result = count * 1.50
    elif prod == 'water':
        result = count * 1.00
    elif prod == 'coke':
        result = count * 1.40
    elif prod == 'snacks':
        result = 2.00
    return f'{result: .2f}'

product = input()
count_of_product = int(input())
print(solve(product, count_of_product))
