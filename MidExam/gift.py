side_size = float(input())
sheets_num = int(input())
area_sum = 0

gift_area = side_size * side_size * 6

for sheet in range(1, sheets_num + 1):
    length_of_side = float(input())
    width_of_side = float(input())
    side_area = length_of_side * width_of_side

    if sheet % 3 == 0:
        side_area -= side_area * 0.25
    if sheet % 5 == 0:
        side_area = 0

    area_sum += side_area

area_sum = round(area_sum, 2)
if area_sum >= gift_area:
    covered_area = round(((area_sum - gift_area) / area_sum) * 100, 2)
    print(f"You've covered the gift box!")
    print(f"{covered_area: .2f}% wrap paper left.")
else:
    covered_area = (area_sum / gift_area) * 100
    diff = abs(100 - round(covered_area, 2))
    print(f"You are out of paper!")
    print(f"{diff: .2f}% of the box is not covered.")


