input_str = input().split()
cats1 = []
cats2 = []
cats_dict = {
    'same': '',
    'only 1': '',
    'only 2': ''
}
for _ in range(int(input_str[0])):
    cats1.append(input())
for _ in range(int(input_str[1])):
    cats2.append(input())
for cat in cats1:
    if cat in cats2:
        cats_dict['same'] += cat + ' '
        cats2.pop(cats2.index(cat))
    elif cat not in cats2:
        cats_dict['only 1'] += cat + ' '
cats_dict['only 2'] += ' '.join(cats2)
for key, value in cats_dict.items():
    print(len(value.split()))
    value = [int(i) for i in value.split()]
    value = sorted(value)
    for subvalue in value:
        print(subvalue)