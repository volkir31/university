first_dict = {}
second_dict = {}
first_input_str, second_input_str = input(), input()
if first_input_str[0] != second_input_str[0] and first_input_str.lower() == second_input_str.lower():
    print('no')
else:
    for symb in first_input_str.lower():
        if symb.isalpha():
            if symb not in first_dict:
                first_dict[symb] = 1
            else:
                first_dict[symb] += 1
    for symb in second_input_str.lower():
        if symb.isalpha():
            if symb not in second_dict:
                second_dict[symb] = 1
            else:
                second_dict[symb] += 1
    if sorted(first_dict.keys()) == sorted(second_dict.keys()) and sum(first_dict.values()) == sum(second_dict.values()):
        print('yes')
    else:
        print('no')
