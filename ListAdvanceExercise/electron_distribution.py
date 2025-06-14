electrons_number = int(input())
factor = 0
shells = []

while electrons_number > 0:
    factor += 1
    current_shell_electrons = 2 * factor ** 2
    if 0 < current_shell_electrons <= electrons_number:
        shells.append(current_shell_electrons)
    else:
        shells.append(electrons_number)
        break
    electrons_number -= current_shell_electrons


print(shells)