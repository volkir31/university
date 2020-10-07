from random import randint
count_attempt = []
for i in range(10):
    result_list = []
    count_iter = 0
    while True:
        result_list.append(randint(0, 1))
        count_iter += 1
        if len(result_list) >= 3 and result_list[-1] == result_list[-2] == result_list[-3]:
            count_attempt.append(count_iter)
            break
print(sum(count_attempt) / 10)
