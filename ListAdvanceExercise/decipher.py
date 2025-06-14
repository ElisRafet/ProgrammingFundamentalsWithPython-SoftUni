message = input().split()
word = []
decoded_message = []

while len(message):
    current_word = message[0]
    first_letter_code = ''.join([char for char in current_word if char.isdigit()])
    first_letter = chr(int(first_letter_code))
    rest_of_word = current_word[len(first_letter_code):]
    if len(rest_of_word) > 1:
        rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
    word = first_letter + rest_of_word
    decoded_message.append(word)
    message.remove(current_word)

print(' '.join(decoded_message))

