first_digit, second_digit = 0, 1
index_of_digit = 0
current_digit = int(input())
while True:
    new_digit = first_digit + second_digit
    first_digit, second_digit = second_digit, new_digit
    index_of_digit += 1
    if first_digit == current_digit:
        print(index_of_digit if current_digit != 0 else 0)
        break
    if first_digit > current_digit:
        print(-1)
        break
