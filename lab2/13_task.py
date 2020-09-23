list_of_word_in_str = input().split()
list_of_symbol = ';.,.`?!:'
for i in range(1, len(list_of_word_in_str)):
    if list_of_word_in_str[i][-1] in list_of_symbol:
        list_of_word_in_str[i] = list_of_word_in_str[i].replace(list_of_word_in_str[i][-1], '')
print(' '.join(list_of_word_in_str))
