list_size = int(input())

for i in range(list_size):
    str = ''
    for j in range(list_size):
        if list_size - i - 1 == j:
            str += '1 '
        elif list_size - i - 1 < j:
            str += '2 '
        else:
            str += '0 '
    print(str.strip())
