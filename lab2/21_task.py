input_str = input().split()
count_str, count_column = int(input_str[0]), int(input_str[1])
list1 = []
for i in range(count_str):
    list1.append(input().split())
input_str = input().split()
replaceable_string,replacement_string = int(input_str[0]), int(input_str[1])
for i in range(count_str):
    str = ''
    for j in range(count_column):
        if j == replaceable_string:
            str += f'{list1[i][replacement_string]} '
        elif j == replacement_string:
            str += f'{list1[i][replaceable_string]} '
        else:
            str += f'{list1[i][j]} '
    print(str)
