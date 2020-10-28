count_facets = int(input())
digit_dict = {}
for i in range(2 * count_facets, 1, -1):
    digit_dict[i] = []
for key, value in digit_dict.items():
    for i in range(1, count_facets + 1):
        for j in range(1, count_facets + 1):
            if i + j == key:
                digit_dict[key].append((i, j))
for key , value in sorted(list(digit_dict.items()), reverse=True):
    print('sum = {} rolls = {}'.format(key, value))
