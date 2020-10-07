input_string = input()
alphabet = 'poiuytrewqlkjhgfdsamnbvcxz'
condition_list = [0, 0, 0, 0]
for symb in input_string:
    if symb in alphabet:
        condition_list[0] += 1
    elif symb in alphabet.upper():
        condition_list[1] += 1
    elif symb == '@' or symb == '#' or symb == '$':
        condition_list[2] += 1
    elif symb.isdigit():
        condition_list[3] += 1
if condition_list[0] * condition_list[1] * condition_list[2] * condition_list[3] != 0 and 6 <= len(input_string) <= 12:
    print(input_string)

