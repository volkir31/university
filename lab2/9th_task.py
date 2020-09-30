# list_of_digit = input().split()
# index_of_delete = int(input())
# list_of_digit.pop(index_of_delete)
# print(' '.join(list_of_digit))

list_of_digit, index_of_delete= input().split(), int(input())
list_of_digit = list_of_digit[:index_of_delete] + list_of_digit[index_of_delete + 1:]
print(' '.join(list_of_digit))

# for i in range(len(list_of_digit)):
#     if i == index_of_delete:
#         list_of_digit = list_of_digit[1:] + list_of_digit[:1]
#         list_of_digit.pop()
#     else:
#         list_of_digit = list_of_digit[1:] + list_of_digit[:1]
