list_of_digit = input().split()
for i in range(1, len(list_of_digit)):
    if int(list_of_digit[i]) > 0 and int(list_of_digit[i - 1]) > 0 or int(list_of_digit[i]) < 0 and \
            int(list_of_digit[i - 1]) < 0:
        print(list_of_digit[i - 1], list_of_digit[i])
        break
