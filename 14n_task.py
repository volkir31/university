# print(min([int(input()) for i in range(3)]))
min_digit = int(input())
for i in range(2):
    digit = int(input())
    if digit < min_digit:
        min_digit = digit
print(min_digit)