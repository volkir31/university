list_size = int(input())
for i in range(list_size):
    str1 = str(i)+' '
    for j in range(1, list_size):
        if i == j:
            str1 += '0 '
        else:
            str1 += str(abs(i - j)) + ' '
    print(str1.strip())
