list_of_digit = input().split()
count_digit = 0
for i in range(1, len(list_of_digit) - 1):
    if list_of_digit[i - 1] < list_of_digit[i] and list_of_digit[i] > list_of_digit[i + 1]:
        count_digit += 1
print(count_digit)