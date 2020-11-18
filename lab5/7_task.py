def avgSunspot(file, year_tuple, month_tuple):
    sun_dict = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    }
    with open(file, 'r') as f:
        for line in f:
            data = line.split()
            keys = list(sun_dict.keys())
            for k in range(len(keys)):
                for d in range(len(data)):
                    if data[d][0].isdigit():
                        if k == d:
                            if k == 0:
                                sun_dict[keys[k]].append(int(data[d]))
                            else:
                                sun_dict[keys[k]].append(float(data[d]))
    sum = 0
    count = 0
    sun_list = list(sun_dict.items())
    sun_list.sort()
    if len(set(year_tuple)) == 1:
        for month in range(month_tuple[0], month_tuple[1] + 1):
            count += 1
            index = sun_list[0][1].index(year_tuple[0])
            sum += sun_list[month][1][index]
    else:
        for year in range(year_tuple[0], year_tuple[1] + 1):
            for month in range(month_tuple[0], month_tuple[1] + 1):
                count += 1
                index = sun_list[0][1].index(year)
                sum += sun_list[month][1][index]
    return '%.1f' % (sum/count)


# if len(set(year_tuple)) == 1:
    #     for month in range(month_tuple[0], month_tuple[1] + 1):
    #         count += 1
    #         sum += sun_dict[month][sun_dict[0].index(year_tuple[0])]
    # else:
    #     for year in range(year_tuple[0], year_tuple[1] + 1):
    #         for month in range(month_tuple[0], month_tuple[1] + 1):
    #             sum += sun_dict[month][sun_dict[0].index(year)]
    #             count += 1
    # return '%.1f' % (sum/count)



if __name__ == '__main__':
    # print(avgSunspot('sunspot_data.txt', (1800, 1809), (1, 3)))
    # print(avgSunspot('sunspot_data.txt', (1749, 1749), (1, 12)))
    print(avgSunspot('sunspot_data.txt', (1749, 1764), (1, 1)))