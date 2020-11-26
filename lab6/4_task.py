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


def classify_test_set_list(test_set_list, classifier_list):
    out_list = []
    for item in test_set_list:
        d_vote = 0
        z_vote = 0
        for i in range(2, len(item)):
            for j in range(len(classifier_list)):
                if i - 2 == j:
                    if classifier_list[j] < item[i]:
                        z_vote += 1
                    else:
                        d_vote += 1
                else:
                    continue
        out_list.append((item[0], d_vote, z_vote, item[1]))
    return out_list


def report_results(result_list):
    miss = 0
    for item in result_list:
        if item[1] > item[2] and item[3] == 'z' or item[1] < item[2] and item[3] == 'd':
            miss += 1
    print('of {} patients there were {} inaccuracies'.format(len(result_list), miss))


def main():
    training_list = make_data_set("files/SmallTrainingData.txt")
    classifier_list = train_classifier(training_list)
    test_set_list = make_data_set("files/SmallTrainingData1.txt")
    result_list = classify_test_set_list(test_set_list, classifier_list)
    report_results(result_list)


if __name__ == '__main__':
    main()
