str_of_input = input().split()
line, column = str_of_input[0], str_of_input[1]
max_digit = int(str_of_input[0])
coord_x_of_max_digit, coord_y_of_max_digit = 0, 0
for i in range(int(line)):
    digit_in_line = input().split()
    coord_x_of_digit = 0
    if i == 0:
        max_digit = int(digit_in_line[0])
    for digit in digit_in_line:
        if int(digit) > max_digit:
            max_digit = int(digit)
            coord_y_of_max_digit = i
            coord_x_of_max_digit = digit_in_line.index(digit)
print(coord_y_of_max_digit, coord_x_of_max_digit)
