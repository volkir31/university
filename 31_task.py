max_digit = 0
index_of_digit = -1
max_digit_index = -1
while True:
    digit = int(input())
    index_of_digit += 1
    if digit > max_digit:
        max_digit = digit
        max_digit_index = index_of_digit
    if digit == 0:
        break
print(max_digit_index)