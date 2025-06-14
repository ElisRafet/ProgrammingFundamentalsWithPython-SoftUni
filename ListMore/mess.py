int_list = input().split(" ")
text = list(input())
message = []

for num in numbers:
    digit_sum = sum(int(digit) for digit in num)
    index = digit_sum % len(text)
    message.append(text[index])
    text.pop(index)

print("".join(message))
