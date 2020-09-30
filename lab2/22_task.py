input_str = input().split()
count_str1, count_column1_count_str2, count_column2 = int(input_str[0]), int(input_str[1]), int(input_str[2])
list1 = []
list2 = []
list3 = [[0 for m in range(count_column2)] for n in range(count_str1)]
for i in range(count_str1):
    list1.append(input().split())
for i in range(count_column1_count_str2):
    list2.append(input().split())
for i in range(count_str1):
    for j in range(count_column2):
        for k in range(count_column1_count_str2):
            list3[i][j] += int(list1[i][k]) * int(list2[k][j])
for i in range(count_str1):
    str1 = ''
    for j in range(count_column2):
        str1 += str(list3[i][j]) + ' '
    print(str1)
    
# from random import randint
# from numpy import dot

# for j in range(count_column1_count_str2):
#     for k in range(count_column2):
#         for i in range(count_str1):
#           str1 += f'{str(int(list1[i][j]) * int(list2[j][k]))} '
#     print(str1)


# print(list1, list2)
# for i in range(len(list1)):
#     for j in range(len(list2[0])):
#         for k in range(len(list2)):
#             list3[i][j] += int(list1[i][k]) * int(list2[k][j])
# for i in range(count_str1):
#     str1 = ''
#     for j in range(count_column2):
#         str1 += f'{list3[i][j]} '
#     print(str1)



