import re

n = int(input())
cars = {}
for _ in range(n):
    car_data = input().split('|')
    car, millage, fuel = car_data[0], int(car_data[1]), int(car_data[2])
    cars[car] = {'millage': millage, 'fuel': fuel}

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break

    if command[0] == 'Drive':
        car, distance, needed_fuel = command[1], int(command[2]), int(command[3])
        if cars[car]['fuel'] < needed_fuel:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['millage'] += distance
            cars[car]['fuel'] -= needed_fuel
            print(f'{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.')
        if cars[car]['millage'] < 100000:
            print(f'Time to sell the {car}!')
            del cars[car]
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        current_fuel = cars[car]['fuel']
        added_fuel = min(75 - current_fuel, fuel)
        cars[car]['fuel'] += added_fuel
        print(f'{car} refueled with {added_fuel} liters')
    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        if cars[car]['millage'] - kilometers < 10000:
            cars[car]['millage'] = 10000
        else:
            cars[car]['millage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['millage']} kms, Fuel in the tank: {data['fuel']} lt.")