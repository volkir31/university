list_of_digit = input().split()
for elem in list_of_digit:
    if int(elem) % 2 == 0:
        print(int(elem), end=' ')
