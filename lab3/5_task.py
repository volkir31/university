input_string = input()
if input_string.count('f') == 1:
    print(-1)
elif input_string.count('f') == 0:
    print(-2)
else:
    print(input_string.index('f', input_string.index('f') + 1))
    # count = 1
    # for i in range(len(input_string)):
    #     if count == 2:
    #         print(i)
    #         break
    #     if input_string[i] == 'f':
    #         count += 1
