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

