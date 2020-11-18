current_str = ''
while True:
    input_str = input()
    if input_str == '':
        break
    else:
        current_str += input_str
sum = 0
for symb in current_str:
    if symb != ' ' and symb != '.':
        try:
            sum += int(symb)
        except ValueError:
            print('{} is not a number'.format(symb))
    elif symb == '.':
        sum += float(current_str[current_str.index(symb)-1] + '.' + current_str[current_str.index(symb) + 1])
        sum -= int(current_str[current_str.index(symb)-1]) + int(current_str[current_str.index(symb) + 1])
print(sum)