import string


def get_caesar_character(source_char, key):
    alphabet = string.ascii_uppercase
    if source_char.upper() not in alphabet:
        return source_char
    new_char = alphabet[(alphabet.index(source_char.upper()) + key) % len(alphabet)]
    return new_char.upper() if source_char.isupper() else new_char.lower()


def caesarEncrypt(string_to_encode, key):
    result = ''
    for char in string_to_encode:
        result += get_caesar_character(char, key)
    return result


def get_count_letter(letter, string1):
    count = 0
    for char in string1:
        if char.upper() == letter.upper():
            count += 1
    return count


def get_letters_count(string1):
    count = 0
    for char in string1:
        if char.isalpha():
            count += 1
    return count


def analyze_text(string_to_analyze):
    file_letter_count = get_letters_count(string_to_analyze)
    my_list = []
    for l in string.ascii_lowercase:
        letter_count = get_count_letter(l, string_to_analyze)
        freq = (letter_count / file_letter_count) * 100
        letter_position = len(string.ascii_lowercase) - string.ascii_lowercase.index(l.lower())
        my_list.append((freq, letter_position, l))
    my_list.sort(reverse=True)
    return my_list


def verify_string(string1, string_english):
    words = string1.split()
    verify_count = 0
    fail_count = 0
    for w in words:
        if fail_count >= 1:
            print(w)
            return False
        if verify_count >= 10:
            return True
        if '.' not in w and ',' not in w and '\'' not in w and ':' not in w:
            if string_english.find(w.upper() + '\n') >= 0:
                verify_count += 1
            else:
                fail_count += 1
    return False


def get_letter_position_in_alphabet(letter):
    return 1 + string.ascii_lowercase.index(letter.lower())


def breakCaesar(file, clean_text, dictionary=None):
    freq_caesar_data = analyze_text(open(file).read())
    freq_clear_data = analyze_text(open(clean_text).read())

    freq_caesar_letters = []
    freq_clear_letters = []
    for t in freq_caesar_data:
        freq_caesar_letters.append(t[2])
    for t in freq_clear_data:
        freq_clear_letters.append(t[2])

    for i in range(len(freq_caesar_letters)):
        clear_letter_pos = get_letter_position_in_alphabet(freq_clear_letters[i])
        caesar_letter_pos = get_letter_position_in_alphabet(freq_caesar_letters[i])
        key = caesar_letter_pos - clear_letter_pos
        source_string = caesarEncrypt(open(file).read(), -key)
        if key >= 0 and verify_string(source_string, open(dictionary).read()):
            print(key)
            print(source_string)
            return source_string


if __name__ == '__main__':
    # breakCaesar('2.txt', '1.txt')
    breakCaesar('2.txt', '1.txt', 'files/dictionary.txt')
