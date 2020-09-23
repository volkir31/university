# digits = [int(input()) for i in range(2)]
# sequence = [str(i) for i in range(min(digits), max(digits) + 1)]
# print(' '.join(sequence) if digits[0] < digits[1] else ' '.join(sequence[::-1]))

left_border, right_border = int(input()), int(input())
if left_border < right_border:
    for i in range(left_border, right_border + 1):
        print(i, end=' ')
else:
    for i in range(left_border, right_border - 1, -1):
        print(i, end=' ')