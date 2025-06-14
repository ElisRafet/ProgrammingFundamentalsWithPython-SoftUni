def symbols(some_number: int) -> str:
    percent_count = some_number // 10
    dots = 10 - percent_count
    return percent_count * '%' + dots *'.'

number = int(input())
result = symbols(number)
if number == 100:
    print('100% Complete!')
    print(f'[{result}]')
else:
    print(f'{number}% [{result}]')
    print('Still loading...')