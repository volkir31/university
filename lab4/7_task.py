from sys import stdin

buyers_dict = {}
lines = stdin.read().splitlines()
for i in lines:
    input_str = i.split()
    if input_str[0] not in buyers_dict:
        buyers_dict[input_str[0]] = input_str[1:]
    else:
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
