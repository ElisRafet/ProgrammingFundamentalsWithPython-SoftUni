companies = {}
while True:
    command = input()
    if command == 'End':
        break
    company_name, employee_id = command.split(' -> ')
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company in companies:
    print(f'{company}')
    for i in range(len(companies[company])):
        print(f'-- {companies[company][i]}')