morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': 'p'
}
input_list = []
while True:
    input_str = input().upper()
    if input_str == '@':
        break
    else:
        input_list.append(input_str)
output_list = []
for str in input_list:
    new_str, decode_str, decoded_str = '', '', ''
    if str[0].isalpha() == False:
        for symb in str + ' ':
            if symb != ' ':
                decode_str += symb.lower()
            else:
                for key, value in morse_dict.items():
                    if decode_str == value:
                        decoded_str += key
                        decode_str = ''
                        break
        output_list.append(decoded_str.lower().strip())
    else:
        if str[0].isalpha():
            for symb in str:
                for key, value in morse_dict.items():
                    if symb == key:
                        new_str += value + ' '
                    elif symb in '.,?!:;' and str[str.index(symb) - 1].isdigit() and str[str.index(symb) - 1] != 'p':
                        continue
            output_list.append(new_str)
print('\n'.join(output_list))
