list_size = int(input())
for i in range(list_size):
    str = f'{i } '
    for j in range(1, list_size):
        if i == j:
            str += '0 '
        else:
            str += f'{abs(i - j)} '
    print(str.strip())
