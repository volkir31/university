def cat(file1, file2, out):
    with open(out, 'w') as output_file:
        try:
            with open(file1, 'r') as f1:
                for line in f1:
                    output_file.write(line)
        except FileNotFoundError:
            print('can\'t open {}'.format(file1))
        try:
            with open(file2, 'r') as f2:
                for line in f2:
                    output_file.write(line)
        except FileNotFoundError:
            print('can\'t open {}'.format(file2))


if __name__ == '__main__':
    cat('1.txt', '2.txt', '3.txt')
