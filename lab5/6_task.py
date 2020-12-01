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
    # print(count_word, len(alpha_dict), alpha_dict)

# def printLetterPercentage1(file):
#     alphabet = {}
#     signs = """.,!?/"';:-#№%^&*()[]}{<>"""
#     temp = []
#     amountOfWords = 0
#     with open(file) as f:
#         temp = f.read().split()
#     for word in temp:
#         for char in word:
#             if ord('A') <= ord(char) <= ord('Z') \
#                     or ord('a') <= ord(char) <= ord('z'):
#                 if not (char.upper() in alphabet.keys()):
#                     alphabet[char.upper()] = []
#                     alphabet[char.upper()].append(1)
#                     alphabet[char.upper()].append(False)
#                 elif char.upper() in alphabet.keys() and alphabet[char.upper()][1] == True:
#                     alphabet[char.upper()][0] += 1
#                     alphabet[char.upper()].append(False)
#         for char in range(ord('A'), ord('Z') + 1):
#             if chr(char) in alphabet.keys():
#                 alphabet[chr(char)][1] = True
#         amountOfWords += 1
#     for char in range(ord('A'), ord('Z') + 1):
#         if chr(char) in alphabet.keys():
#             print(chr(char),
#                   'occurs in {0:.2f}'.format(float(alphabet[chr(char)][0] * 100 / amountOfWords)),
#                   'percent of words')
#         else:
#             print(chr(char), 'occurs in {0:.2f}'.format(float(0)), 'percent of words')
#     alphabet_list = list(alphabet.items())
#     new_alphabet_list = map(lambda list1: (list1[0], list1[1][0]), alphabet_list)
#     print(amountOfWords, len(alphabet), sorted(new_alphabet_list))


if __name__ == '__main__':
    printLetterPercentage('1.txt')
    # printLetterPercentage1('1.txt')
