list_of_word = []
while True:
    word = input().strip()
    if word != '' and word not in list_of_word:
        list_of_word.append(word)
    elif word == '':
        break
print('\n'.join(list_of_word))