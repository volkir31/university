right_border = int(input())
factorial = 1
factorial_sum = 0
for iter in range(1,right_border+1):
    factorial_sum += factorial * iter
    factorial *= iter
print(factorial_sum)