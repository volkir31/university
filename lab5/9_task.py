from string import ascii_lowercase


def frequencies_is_same(dict1: dict):
    for value in dict1.values():
        if value != list(dict1.values())[0]:
            return False
    return True


def getFreq(file):
    alpha_dict = dict(zip(ascii_lowercase, [0] * len(ascii_lowercase)))

    with open(file, 'r') as f:
        count_alpha = 0
        for line in f:
            for alpha in line:
                if alpha.isalpha():
                    count_alpha += 1
                    alpha_dict[alpha.lower()] += 1
    if frequencies_is_same(alpha_dict):
        alpha_list = sorted(list(alpha_dict.items()))
        for item in alpha_list:
            ferq = '%.2f' % (item[1] / count_alpha * 100)
            if len(ferq) == 4:
                ferq += ' '
            print('letter {}: '.format(item[0]) + ferq + \
                  ' percent of {}'.format(count_alpha))
    else:
        alpha_list = list(alpha_dict.items())
        alpha_list.sort(key=lambda list1: (-list1[1], list1[0]))
        for item in alpha_list:
            ferq = '%.2f' % (item[1] / count_alpha * 100)
            if len(ferq) == 4:
                ferq += ' '
            print('letter {}: '.format(item[0]) + ferq + \
                  ' percent of {}'.format(count_alpha))
    return alpha_dict

# x = float('{:.3f}'.format(x))
# print(item[0], 'occurs in %.2f percent of words' % (item[1] / count_word * 100))


if __name__ == '__main__':
    getFreq('1.txt')
