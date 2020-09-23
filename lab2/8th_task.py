list_of_digit = input().split()
for i in range(1, len(list_of_digit), 2):
    list_of_digit[i - 1], list_of_digit[i] = list_of_digit[i], list_of_digit[i - 1]
print(' '.join(list_of_digit))
