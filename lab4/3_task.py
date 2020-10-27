count_str = int(input())
input_list = []
for _ in range(count_str):
    input_str = input().split()
    for i in range(len(input_str)):
        if input_str[i] not in input_list:
            input_list.append((input_str.count(input_str[i]), input_str[i]))
        else:
            continue
sorted_list = sorted(set(input_list), reverse=True)
print(sorted_list[1][1] if sorted_list[0][0] == sorted_list[1][0] else sorted_list[0][1])

