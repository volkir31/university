dict_couples = {}
for i in range(int(input())):
    input_string = input().split()
    dict_couples[input_string[0]] = input_string[1]
first_word = input()
if first_word in dict_couples.keys():
    print(dict_couples[first_word])
else:
    for key, value in dict_couples.items():
        if value == first_word:
            print(key)
            break
