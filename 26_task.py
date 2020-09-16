right_border = int(input())
factorial = 1
for iter in range(1, right_border + 1):
    factorial *= iter
print(factorial)