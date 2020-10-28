from sys import stdin

buyers_dict = {}
lines = stdin.read().splitlines()
for i in lines:
    input_str = i.split()
    if input_str[0] not in buyers_dict:
        buyers_dict[input_str[0]] = {input_str[1]: int(input_str[2])}
    else:
<<<<<<< HEAD
        if input_str[1] not in buyers_dict[input_str[0]]:
            buyers_dict[input_str[0]][input_str[1]] = int(input_str[2])
        else:
            buyers_dict[input_str[0]][input_str[1]] += int(input_str[2])
sorted_list = sorted(buyers_dict.items())
for item in sorted_list:
    print(item[0]+':')
    for product, count in sorted(item[1].items()):
        print(product, count)
=======
        buyers_dict[input_str[0]] += input_str[1:]
for name, products in buyers_dict.items():
    print(name+':')
    count_iter = 0
    for product in products:
        print(product, end=' ')
        count_iter += 1
        if count_iter == 2:
            print('')
            count_iter = 0
>>>>>>> 011d1f574595be3f269bab82deb5efea37b01536
