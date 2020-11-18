import string
alphabet = string.ascii_lowercase


def encrypt(line, key):
    output_str = ''
    for symb in line:
        if symb == ' ' or symb == '\n' or symb in '.,\\`:;-_0123456789&!?)(\'"':
            output_str += symb
        else:
            new_index = alphabet.index(symb.lower()) + key
            if symb.isupper():
                try:
                    output_str += alphabet[new_index].upper()
                except IndexError:
                    output_str += alphabet[new_index - len(alphabet)].upper()
            else:
                try:
                    output_str += alphabet[new_index]
                except IndexError:
                    output_str += alphabet[new_index - len(alphabet)]
    return output_str


def caesarEncrypt(message, key, source='string'):
    if source == 'string':
        return encrypt(message, key)
    elif source == 'file':
        try:
            with open(message, 'r') as f:
                output_str = ''
                for line in f:
                    output_str += encrypt(line, key)
            return output_str
        except FileNotFoundError:
            return 'Can\'t open file {}'.format(message)


if __name__ == '__main__':
    print(caesarEncrypt('1.txt', 3, source='file'))
    print(caesarEncrypt('hello,world', 2))
