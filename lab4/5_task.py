count_str = int(input())
input_list = []
input_str = ''
input_dict = {}
for _ in range(count_str):
    input_str += input() + ' '
input_str = input_str.split()
for i in range(len(input_str)):
    input_dict[input_str[i]] = input_str.count(input_str[i])
input_list = list(input_dict.items())
input_list.sort(key=lambda list_item: (-list_item[1], list_item[0]))
for i in input_list:
    print(i[0])




    # if input_str[i] not in input_list:
        # input_list.append((input_str.count(input_str[i]), input_str[i]))
    # else:
    #     continue
# sorted_list = sorted(set(input_list), reverse=True)
# print(sorted_list)
# for i in sorted_list:
#     for j in sorted_list[-1:sorted_list.index(i):-1]:
#         if i[0] > j[0]:
#             print(i[1])
#             break
#         elif i[0] == j[0]:
#             print(j[1])
#             break
