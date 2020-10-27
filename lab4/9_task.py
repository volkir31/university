dict = {
    1: '.,?!:',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' ',
}
input_str = input().upper()
for symb in input_str:
    for key, value in dict.items():
        if symb in value:
            for subvalue in value:
                if symb != subvalue:
                    print(key, end='')
                if symb == subvalue:
                    print(key, end='')
                    break
            break
