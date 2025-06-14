import re
n = int(input())
pattern = r'@#+([A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(n):
    barcode = input()
    match = re.match(pattern, barcode)
    if match:
        core = match.group(1)
        prod_group = ''.join(filter(str.isdigit, core)) or '00'
        print(f'Product group: {prod_group}')
    else:
        print(f'Invalid barcode')