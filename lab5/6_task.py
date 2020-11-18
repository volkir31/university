def printLetterPercentage(file):
    alpha_dict = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
        'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,
    }
    with open(file, 'r') as f:
        count_word = 0
        for line in f:
            for word in line.split():
                wrd = []
                count_word += 1
                for alpha in word:
                    if alpha != ' ' and alpha.isalpha():
                        if alpha.upper() in wrd:
                            pass
                        else:
                            alpha_dict[alpha.upper()] += 1
                            wrd.append(alpha.upper())
    alpha_list = sorted(list(alpha_dict.items()))
    for item in alpha_list:
        print(item[0], 'occurs in %.2f percent of words' % (item[1]/count_word * 100))


if __name__ == '__main__':
    printLetterPercentage('1.txt')