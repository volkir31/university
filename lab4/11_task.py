first_input_str, second_input_str, count = sorted(list(input().lower())), sorted(list(input().lower())), 0
symb_dict = {}
symb_dict2 = {}
for symb in first_input_str:
    if symb not in symb_dict:
        symb_dict[symb] = 0
    else:
        symb_dict[symb] += 1
for symb in second_input_str:
    if symb not in symb_dict2:
        symb_dict2[symb] = 0
    else:
        symb_dict2[symb] += 1
if len(symb_dict) == len(symb_dict2):
    for key1, value1 in symb_dict.items():
        for key2, value2 in symb_dict2.items():
            if key1 == key2 and value1 == value2:
                count += 1
    if count == len(symb_dict):
        print('yes')
    else:
        print('no')
else:
    print('no')
