# digits = [int(input()) for i in range(3)]
# print( 3 if len(set(digits)) == 1 else 2 if len(set(digits)) == 2 else 0)
first_digit, second_digit, third_digit = int(input()), int(input()), int(input())
if first_digit == second_digit == third_digit:
    print(3)
elif first_digit == second_digit or first_digit == third_digit or second_digit == third_digit:
    print(2)
else:
    print(0)