input_list = list(input())
count_symb = 0
while ' ' in input_list:
    input_list.remove(' ')
symb_str = '+-'
for i in range(len(input_list)):
    if input_list.count(')') != input_list.count('(') or input_list.count('(') == 1 and input_list.count(')') == 1:
        print('error')
        break
    if input_list[i] in symb_str and input_list[i + 1].isdigit():
        print(input_list[i]+input_list[i + 1])
    elif input_list[i - 1] in symb_str and input_list[i].isdigit() or input_list[i] == ' ':
        continue
    else:
        print(input_list[i])
