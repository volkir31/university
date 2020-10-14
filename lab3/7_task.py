input_string = input()
first_index, last_index = input_string.index('h'), input_string.rindex('h')
print(input_string[0: first_index] + input_string[last_index:first_index: -1] + input_string[last_index:])
