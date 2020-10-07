input_string = input()
if len(input_string) > 4:
    count = 0
    for i in range(0, 4):
        if input_string[i].isupper():
            count += 1
    if count >= 2:
        print(input_string.upper())
    else:
        print(input_string[:-1] + input_string[-1].upper())
