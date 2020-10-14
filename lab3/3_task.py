# import re
# input_string = input()
# result = re.findall(r"\w*.", input_string)
# result[0], result[-1] = result[-1] + ' ', result[0]
# print(''.join(result))

input_string = input()
first_word, second_word = input_string[:input_string.find(' ')], input_string[input_string.find(' ') + 1:]
print(second_word + ' ' + first_word)