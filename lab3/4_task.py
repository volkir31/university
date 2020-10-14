input_string = input()
if 'f' in input_string:
    if input_string.count('f') >= 2:
        print(input_string.index('f'), input_string.rindex('f'))
    else:
        print(input_string.index('f'))
