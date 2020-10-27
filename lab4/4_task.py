count_files = int(input())
files_dict = {}
for _ in range(count_files):
    input_str = input().split()
    files_dict[input_str[0]] = input_str[1:]
count_files = int(input())
input_list = []
for _ in range(count_files):
    input_str = input().split()
    if input_str[0].lower() == 'read':
        input_str[0] = 'R'
    elif input_str[0].lower() == 'write':
        input_str[0] = 'W'
    elif input_str[0].lower() == 'execute':
        input_str[0] = 'X'
    input_list.append((input_str[0], input_str[1]))
for i in range(len(input_list)):
    if input_list[i][0] in files_dict[input_list[i][1]]:
        print('OK')
    else:
        print('Access denied')