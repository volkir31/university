list_of_digit = input().split()
pairs_of_numbers = 0
for i in range(len(list_of_digit) - 1):
    for j in range(i + 1, len(list_of_digit)):
        if list_of_digit[i] == list_of_digit[j]:
            pairs_of_numbers += 1
print(pairs_of_numbers)
