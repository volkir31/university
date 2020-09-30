list_of_digit = input().split()
count_digit = 0
for i in range(1, len(list_of_digit) - 1):
    if int(list_of_digit[i - 1]) < int(list_of_digit[i]) and int(list_of_digit[i]) > int(list_of_digit[i + 1]):
        count_digit += 1
print(count_digit)