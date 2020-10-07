import re
input_string = input()
prototype = r'[ABEKMHOPCTYX]\d\d\d[ABEKMHOPCTYX]{2}\d{2,3}'
print('yes' if len(re.findall(prototype, input_string)) == 1 else 'no')
