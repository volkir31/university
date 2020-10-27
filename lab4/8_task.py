input_str = input().split()
input_dict = {}
for str in input_str:
    str_list = str.split(':')
    input_dict[str_list[0]] = str_list[1]
needed_value = input()
key_list = []
for key, value in input_dict.items():
    if value == needed_value:
        key_list.append(key)
if len(key_list) != 0:
    key_list.sort()
    print(' '.join(key_list))
else:
    print('Not found!')