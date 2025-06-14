vowels = ['a', 'o', 'u', 'e', 'i']
upper_vowels = [vowel.upper() for vowel in vowels]
vowels.extend(upper_vowels)
string_ = input()

result = ''.join([char for char in string_ if char not in vowels])
print(result)