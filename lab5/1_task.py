def getNLines(file, n, tail=False):
    output_list = []
    try:
        counter = 0
        with open(file, 'r') as f:
            if tail:
                lines_list = []
                for line in f:
                    lines_list.append(line)
                for line in lines_list[len(lines_list):len(lines_list)-n-1:-1]:
                    line = line.replace('\n', '')
                    output_list.append(line.strip())
            else:
                for line in f:
                    if counter == n:
                        break
                    line = line.replace('\n', '')
                    output_list.append(line.strip())
                    counter += 1
            return output_list
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    print(getNLines('files/cipher2.txt',3, True))