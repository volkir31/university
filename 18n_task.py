max_digit = int(input())
count_max_elements = 0
while True:
    digit = int(input())
    if digit == max_digit:
        count_max_elements += 1
    elif digit > max_digit:
        max_digit = digit
        count_max_elements = 0
    if digit == 0:
        break
print(count_max_elements)