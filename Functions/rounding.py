def round_numbers(input_string):
    rounded_numbers = []
    for num in input_string.split():
        rounded_numbers.append(round(float(num)))

    return rounded_numbers

numbers = input()
print(round_numbers(numbers))
