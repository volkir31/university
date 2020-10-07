input_string = input()
if len(input_string) <= 3:
    print(input_string)
elif input_string[-3:] == 'ing':
    print(input_string + 'ly')
else:
    print(input_string + 'ing')