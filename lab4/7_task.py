from sys import stdin

buyers_dict = {}
lines = stdin.read().splitlines()
for i in lines:
    input_str = i.split()
    if input_str[0] not in buyers_dict:
        buyers_dict[input_str[0]] = {input_str[1]: int(input_str[2])}
    else:
        if input_str[1] not in buyers_dict[input_str[0]]:
            buyers_dict[input_str[0]][input_str[1]] = int(input_str[2])
        else:
            buyers_dict[input_str[0]][input_str[1]] += int(input_str[2])
sorted_list = sorted(buyers_dict.items())
for item in sorted_list:
    print(item[0]+':')
    for product, count in sorted(item[1].items()):
        print(product, count)
