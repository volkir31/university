def comment_line(line):
    if not line:
        return False
    return line[0] == '#'


def comment_in_line(line: str):
    code_line = []
    for symb in range(len(line)):
        if line[symb] == '\'' or line[symb] == '"':
            code_line.append(symb)

    if not code_line and '#' in line:
        return True, line.find('#')

    for i in range(len(line)):
        if line[i] == '#':
            for j in range(len(code_line) - 1):
                if code_line[j] < i < code_line[j + 1]:
                    if j % 2 == 1:
                        return True, i
                elif i < code_line[0] or i > code_line[len(code_line) - 1]:
                    return True, i

    return False, -1


def removeComments(file):
    with open(file, 'r') as f:
        output_string = []
        for line in f:
            line = line.strip("\n")
            if comment_line(line):
                continue
            comment = comment_in_line(line)
            if comment[0]:
                pos = comment[1]
                new_line = line[:-(len(line) - pos)]
                if len(new_line) >= 3:
                    output_string.append(new_line)
            else:
                output_string.append(line)
        return '\n'.join(output_string)


if __name__ == '__main__':
    print(removeComments('1.txt'))
