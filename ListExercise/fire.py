fire_data = input().strip()
water_available = int(input().strip())

fire_cells = fire_data.replace('#', ' ').split()
total_fire = 0
effort = 0
extinguished_cells = []

for cell in fire_cells:
    if '=' in cell:
        fire_type, value_str = cell.split('=')
        value_str = value_str.strip()
        if value_str:
            try:
                fire_level = int(value_str)
            except ValueError:
                continue

            if (fire_type == "High" and 81 <= fire_level <= 125) or \
                    (fire_type == "Medium" and 51 <= fire_level <= 80) or \
                    (fire_type == "Low" and 1 <= fire_level <= 50):
                if water_available >= fire_level:
                    water_available -= fire_level
                    extinguished_cells.append(fire_level)
                    effort += fire_level * 0.25
                    total_fire += fire_level
print("Cells:")
for cell in extinguished_cells:
    print(cell)
print(f"Effort: {effort:.2f}")  # Форматирано до две десетични знака
print(f"Total Fire: {total_fire}")  # Форматирано изход
