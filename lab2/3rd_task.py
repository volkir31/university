list_of_digit = input().split()
for i in range(1, len(list_of_digit)):
    if list_of_digit[i] > list_of_digit[i - 1]:
        print(list_of_digit[i], end=' ')
