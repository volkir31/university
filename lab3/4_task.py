input_string = input()
if 'f' in input_string:
    print((input_string.index('f'), input_string.rindex('f')) if input_string.count('f') >= 2 else input_string.index('f'))
