input_str = input().split()
cats1 = []
cats2 = []
cats_list = [[], [], []]
for _ in range(int(input_str[0])):
    cats1.append(input())
for _ in range(int(input_str[1])):
    cats2.append(input())
for cat in cats1:
    if cat in cats2:
        cats_list[0].append(cat)
        cats2.pop(cats2.index(cat))
    elif cat not in cats2:
        cats_list[1].append(cat)
for cat in cats2:
    if cat not in cats1:
        cats_list[2].append(cat)
for item in cats_list:
    print(len(item))
    if len(item) == 0:
        print('')
    else:
        value = [int(i) for i in item]
        for subitem in sorted(value):
            print(subitem)
