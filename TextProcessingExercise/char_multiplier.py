def diff_len_multiplier(first_, second_):
    min_len = min(first_, second_)
    total_sum = 0
    max_len = max(first_,second_)
    for index in range(len(min_len)):
        total_sum += ord(first[index]) * ord(second[index])
    for index in range(len(min_len), len(max_len)):
        total_sum += ord(max_len[index])
    return total_sum

def equal_len_multiplier(first_, second_):
    total_sum = 0
    for index in range(len(second)):
        total_sum += ord(first_[index]) * ord(second_[index])
    return total_sum

first, second = input().split()
total = 0

if len(first) == len(second):
    print(equal_len_multiplier(first, second))
else:
    print(diff_len_multiplier(first, second))

