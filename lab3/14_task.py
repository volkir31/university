from random import randint, choice
count_attempt = []
choice_list = ['H', 'T']
for i in range(10):
    result_list = []
    count_iter = 0
    while True:
        result_list.append(choice(choice_list))
        count_iter += 1
        if len(result_list) >= 3 and result_list[-1] == result_list[-2] == result_list[-3]:
            count_attempt.append(count_iter)
            break
    print(''.join(result_list), len(result_list))
print(sum(count_attempt) / 10)