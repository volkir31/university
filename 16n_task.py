first_digit, second_digit = int(input()), int(input())
sequence = ''
if first_digit < second_digit:
    for digit in range(first_digit, second_digit + 1):
        sequence += str(digit) + ' '
else:
    for digit in range(first_digit, second_digit + 1, -1):
        sequence += str(digit) + ' '
print(sequence.strip())