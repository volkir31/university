first_digit, second_digit = 0, 1
index_right_digit = int(input())
for iter in range(index_right_digit):
    new_digit = first_digit + second_digit
    first_digit, second_digit = second_digit, new_digit
print(first_digit)