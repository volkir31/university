list_of_digit = input().split()
count = 0
for i in range(1, len(list_of_digit)-1):
    if int(list_of_digit[i - 1]) < int((list_of_digit[i])) < int(list_of_digit[i + 1]) or int(list_of_digit[i - 1]) > \
            int(list_of_digit[i]) > int(list_of_digit[i + 1]):
        count += 1
    else:
        break
print('yes' if len(list_of_digit)-count == 2 or len(list_of_digit) == 1 else 'no')
