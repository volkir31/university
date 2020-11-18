def findLongestWord(file):
    try:
        with open(file, 'r') as f:
            max_len = 0
            for line in f:
                word_list = line.split()
                for word in word_list:
                    word_len = 0
                    for alpha in word:
                        if alpha.isalpha():
                            word_len += 1
                        elif alpha != ' ':
                            word = word.replace(word[word.index(alpha)], '')
                    if word_len > max_len:
                        max_len = word_len
                        max_len_list = []
                        max_len_list.append(word)
                    elif word_len == max_len:
                        max_len_list.append(word)
        return sorted(max_len_list)[0]
    except FileNotFoundError:
        pass


print(findLongestWord('1.txt'))
