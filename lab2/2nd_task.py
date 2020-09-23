list_of_digit = input().split()
for i in range(len(list_of_digit)):
    if int(list_of_digit[i]) % 2 == 0:
        print(list_of_digit[i], end=' ')
