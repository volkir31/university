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


print(make_data_set('files/TrainingData.txt'))
print(make_data_set('files/SmallTrainingData.txt'))