string_of_stars = ''
for iter in range(1, 10):
    if iter <= 5:
        string_of_stars += ('* ' * iter).strip() + '\n'
    else:
        string_of_stars += ('* ' * (10 - iter)).strip() + '\n'
print(string_of_stars)
