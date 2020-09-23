digit = int(input())
grade = 0
while digit // 2 > 0:
    digit //= 2
    grade += 1
right_digit = 1
for iter in range(grade):
    right_digit *= 2
print(grade, right_digit)