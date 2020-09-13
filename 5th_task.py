count_desks = 0
for iter in range(3):
    count_students = int(input())
    count_desks += count_students // 2 if count_students % 2 == 0 else count_students // 2 + 1
print(count_desks)
