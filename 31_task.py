max_digit = 0
index_of_max_digit = -1
while True:
    digit = int(input())
    if digit == 0:
        break
    if digit > max_digit:
        max_digit = digit
        index_of_max_digit += 1
print(index_of_max_digit)