str_of_input = input().split()
line, column = str_of_input[0], str_of_input[1]
max_digit = 0
coord_x_of_max_digit = -1
for i in range(int(line)):
    digit_in_line = input().split()
    for digit in digit_in_line:
        if int(digit) > max_digit:
            max_digit = int(digit)
            coord_y_of_max_digit = i
            coord_x_of_max_digit += 1
print(coord_y_of_max_digit, coord_x_of_max_digit)

