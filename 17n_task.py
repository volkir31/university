max_digit = int(input())
prev_max_digit = 0
while True:
    digit = int(input())
    if digit > max_digit:
        prev_max_digit = max_digit
        max_digit = digit
    if prev_max_digit < digit < max_digit:
        prev_max_digit = digit
    if digit == 0:
        break
print(prev_max_digit)