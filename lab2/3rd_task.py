list_of_digit = input().split()
for i in range(1, len(list_of_digit)):
    if int(list_of_digit[i]) > int(list_of_digit[i - 1]):
        print(list_of_digit[i], end=' ')
