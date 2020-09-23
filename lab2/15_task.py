input_list = list(input())
symb_str = '+-'
for i in range(len(input_list)):
    if input_list[i] in symb_str and input_list[i + 1].isdigit():
        print(input_list[i]+input_list[i + 1])
    elif input_list[i - 1] in symb_str and input_list[i].isdigit():
        continue
    else:
        print(input_list[i])
