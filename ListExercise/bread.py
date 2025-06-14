energy = 100
coins = 100
events = input().split('|')
gained_energy = 0

for event in events:
    current_event = event.split("-")
    event_string = current_event[0]
    event_int = int(current_event[1])
    if event_string == 'rest':
        energy += event_int
        if energy > 100:
            energy = 100
            gained_energy = 0
        else: gained_energy += event_int
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_string == 'order':
        if energy >= 30:
            print(f"You earned {event_int} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
            continue
        energy -= 30
        coins += event_int
    else:
        if coins >= event_int:
            print(f"You bought {event_string}.")
            coins -= event_int
        else:
            print(f"Closed! Cannot afford {event_string}.")
            break
else:
    print("Day completed!")
    print(f'Coins: {coins}')
    print(f"Energy: {energy}")