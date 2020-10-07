import re
input_string = input()
result = re.findall(r"\w*.", input_string)
result[0], result[2] = result[2], result[0]
print(''.join(result))
