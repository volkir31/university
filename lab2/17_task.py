list_size = int(input())

for i in range(list_size):
    str = ''
    for j in range(list_size):
        if j == i or list_size - i - 1 == j:
            str += '* '
        elif (j + 1) * 2 - list_size == 1 or (i + 1) * 2 - list_size == 1:
            str += '* '
        else:
            str += '. '
    print(str.strip())
