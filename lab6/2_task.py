def make_data_set(file_name):
    output_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if '?' in line:
                continue
            else:
                new_line = line.split(',')
                out_list = [new_line[0], 'z' if int(new_line[-1]) == 4 else 'd']
                for index in range(1, len(new_line)-1):
                    out_list.append(int(new_line[index]))
            output_list.append(tuple(out_list))
    return output_list


def train_classifier(training_set_list):
    z_list, d_list, count_z, count_d = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0
    out_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in training_set_list:
        for index in range(2, len(item)):
            if item[1] == 'd':
                count_d += 1
                for sec_index in range(len(d_list)):
                    if index - 2 == sec_index:
                        d_list[sec_index] += item[index]
                    else:
                        continue
            else:
                count_z += 1
                for sec_index in range(len(z_list)):
                    if index - 2 == sec_index:
                        z_list[sec_index] += item[index]
                    else:
                        continue
    for i in range(len(out_list)):
        out_list[i] = (z_list[i] / (count_z // 9) + d_list[i] / (count_d // 9)) / 2
    return out_list


def main():
    # data = make_data_set('files/TrainingData.txt')
    data2 = make_data_set('files/SmallTrainingData.txt')
    # print(train_classifier(data))
    print(train_classifier(data2))


if __name__ == '__main__':
    main()
