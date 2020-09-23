# first_digit, second_digit = int(input()), int(input())
# while first_digit != 0 and second_digit != 0:
#     if first_digit > second_digit:
#         first_digit %= second_digit
#     else:
#         second_digit %= first_digit
# print(first_digit + second_digit)

first_digit, second_digit = int(input()), int(input())
if first_digit == 0:
    print(second_digit)
elif second_digit == 0:
    print(first_digit)
else:
    while first_digit > 0 or second_digit > 0:
        if first_digit >= second_digit:
            first_digit %= second_digit
        elif first_digit == second_digit:
            print(first_digit)
        else:
            second_digit %= first_digit
        if second_digit == 0:
            print(first_digit)
            break
        elif first_digit == 0:
            print(second_digit)
            break
