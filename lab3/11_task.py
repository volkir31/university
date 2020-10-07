input_string = input().lower()
alphabet = 'poiuytrewqlkjhgfdsamnbvcxz'
for symb in input_string:
    alphabet = alphabet.replace(symb, '')
if len(alphabet) == 0:
    print('yes')