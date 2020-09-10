max_digit = int(input())
index_of_the_max_digit = 1
while True:
    digit = int(input())
    if digit > max_digit:
        if index_of_the_max_digit >= 2:
            continue
        else:
            max_digit = digit
            index_of_the_max_digit = 2
    if digit == 0:
        break
print(max_digit)