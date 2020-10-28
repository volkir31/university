count_str = int(input())
input_str = ''
input_list = []
output_list = []
for _ in range(count_str):
    input_str += input() + ' '
input_list = input_str.split()
for i in range(len(input_list)):
    if input_list[i] not in output_list:
        output_list.append((input_list.count(input_list[i]), input_list[i]))
    else:
        continue
output_list.sort(key=lambda list_item: (-list_item[0], list_item[1]))
print(output_list[0][1])
