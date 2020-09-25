input_str = input().split()
count_str, count_column = input_str[0], input_str[1]
for i in range(int(count_str)):
    str = ''
    for j in range(int(count_column)):
        if (i + j) % 2 == 0:
            str += '. '
        else:
            str += '* '
    print(str.strip())