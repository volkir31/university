first_digit, second_digit = int(input()), int(input())
while first_digit != 0 and second_digit != 0:
    if first_digit > second_digit:
        first_digit %= second_digit
    else:
        second_digit %= first_digit
print(first_digit + second_digit)