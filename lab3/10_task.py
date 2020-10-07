input_string = input()
first_index = input_string.index('h')
last_index = input_string.rindex('h')
input_string = input_string[0: first_index + 1] + input_string[first_index + 1: last_index].replace('h', 'H') \
               + input_string[last_index:]
print(input_string)