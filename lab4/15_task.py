digit_to_word_dict = {
<<<<<<< HEAD
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '20': 'twenty', '30': 'thirty',
    '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety',
=======
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
        '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '20': 'twenty',
        '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety',
>>>>>>> 011d1f574595be3f269bab82deb5efea37b01536
}
input_digit = input().strip()
output_str = ''
if len(input_digit) == 1:
    print(digit_to_word_dict[input_digit])
elif len(input_digit) == 2:
    if input_digit[0] == '1':
        if input_digit in digit_to_word_dict:
            print(digit_to_word_dict[input_digit])
        else:
            print(digit_to_word_dict[input_digit[1]] + 'teen')
    elif input_digit[1] != '0':
        print(digit_to_word_dict[input_digit[0]+'0'] + '-' + digit_to_word_dict[input_digit[1]])
    else:
        print(digit_to_word_dict[input_digit[0]+'0'])
elif len(input_digit) == 3:
    if input_digit[2] == '0' and input_digit[1] != '0':
        print(digit_to_word_dict[input_digit[0]] + ' hundred ' + digit_to_word_dict[input_digit[1] + '0'])
    elif input_digit[1] == '1':
        if input_digit[1:] not in digit_to_word_dict:
            print(digit_to_word_dict[input_digit[0]] + ' hundred ' + digit_to_word_dict[input_digit[2]] + 'teen')
        else:
            print(digit_to_word_dict[input_digit[0]] + ' hundred ' + digit_to_word_dict[input_digit[1:]])
    elif input_digit[1:] == '00':
        print(digit_to_word_dict[input_digit[0]] + ' hundred ')
    elif input_digit[1] == '0':
        print(digit_to_word_dict[input_digit[0]] + ' hundred ' + digit_to_word_dict[input_digit[0]])
    else:
        print(digit_to_word_dict[input_digit[0]] + ' hundred ' + digit_to_word_dict[input_digit[1] + '0'] + '-' +
              digit_to_word_dict[input_digit[2]])
