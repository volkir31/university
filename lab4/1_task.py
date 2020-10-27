input_list = input().split()
word_dict = {}
for word in input_list:
    if word not in word_dict.keys():
        word_dict[word] = 0
    else:
        word_dict[word] += 1
    print(word_dict[word], end=' ')