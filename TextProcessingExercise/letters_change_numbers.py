some_string = input()
rage_message = ''
substring  = ''
repetitions = ''
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        substring += some_string[index].upper()
    else:
        for next_digit in range(index, len(some_string)):
            if not some_string[next_digit].isdigit():
                break
            repetitions += some_string[next_digit]
        rage_message += substring * int(repetitions)
        substring = ''
        repetitions = ''

print(f'Unique symbols used: {len(set(rage_message))}')
print(rage_message)
